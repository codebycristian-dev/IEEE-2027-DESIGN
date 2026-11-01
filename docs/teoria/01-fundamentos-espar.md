# N-01 — Fundamentos del ESPAR con elementos parásitos conmutados

Nota técnica de respaldo. Estado: vigente. Alimenta a `DOC-03` (§4, §5), `DOC-04` y `DOC-06`.
No se presenta al concurso: existe para que cada número de la propuesta tenga un origen.

## 1. Definición y por qué esta arquitectura

Un ESPAR (*Electronically Steerable Passive Array Radiator*) es un arreglo con **un solo elemento
alimentado** y **N elementos parásitos** cuya carga reactiva se controla para redirigir el haz. El
concepto viene del arreglo de directividad controlada reactivamente de Harrington [1]: si se
puede variar la reactancia de los elementos no alimentados, se puede sintetizar un patrón
directivo sin alimentar cada elemento por separado.

La diferencia con un arreglo de fase convencional es decisiva para este proyecto:

| | Arreglo de fase | ESPAR |
| --- | --- | --- |
| Puertos alimentados | N | 1 |
| Desfasadores / RF | N canales | ninguno |
| Control | RF de precisión | continua o digital, en banda base |
| Costo por elemento | alto | un diodo y una línea de polarización |

Con un receptor comercial de Wi-Fi como el ESP32, **no hay forma de controlar fase ni amplitud de
cada elemento**. Todo el control tiene que estar en la antena. Eso es exactamente lo que un ESPAR
ofrece, y es la razón por la que la arquitectura es coherente con `R7` (costo) y `R8`
(reproducible en aula).

## 2. Mecanismo físico

Cada parásito recibe la corriente que el elemento activo induce en él, y a su vez reirradia. El
patrón total es la superposición de los campos de todos los elementos, cada uno con su corriente.
Cambiar la carga en la base de un parásito cambia la fase y la magnitud de esa corriente inducida;
cambiar eso cambia el patrón.

En la forma clásica del circuito equivalente [1], [2], con el elemento 0 activo y N parásitos:

```
( Z + diag(Z_s, jX_1, ..., jX_N) ) · I = [ V_s, 0, ..., 0 ]ᵀ
```

donde `Z` es la matriz de impedancias de (N+1)×(N+1) (con los elementos propios y el acoplamiento
mutuo entre todos los pares), `Z_s` la impedancia de la fuente, `X_p` la reactancia de la carga del
parásito p e `I` el vector de corrientes de puerto. El patrón se obtiene por superposición:

```
E(θ, φ) ∝ Σ_n I_n · e^( j k r̂ · r_n )
```

De ahí salen las dos reglas que gobiernan el diseño:

- **Carga inductiva (X > 0)** → la corriente inducida se retrasa → el elemento se comporta como
  **reflector**. Es el caso del parásito cortocircuitado a tierra, cuya longitud λ/4 lo hace
  resonante y fuertemente acoplado.
- **Carga capacitiva (X < 0) o circuito abierto** → la corriente inducida se adelanta o se anula →
  el elemento se comporta como **director** o resulta casi transparente.

Una Yagi funcionando bien es esto mismo con cargas fijas: el reflector es más largo que el
radiador, los directores más cortos. El ESPAR es una Yagi cuyas longitudes eléctricas se cambian
en tiempo real.

## 3. El caso discreto: diodo PIN

La restricción del mentor fija **un diodo PIN por parásito** como único mecanismo de
reconfiguración. Un PIN no es una reactancia variable: es un interruptor. A 10 mA conduce
(`R_s ≈ 1.5 Ω`), en corte presenta `C ≈ 0.18 pF` [9].

| Estado | Carga en la base del parásito | Modelo | Papel en el patrón |
| --- | --- | --- | --- |
| PIN en conducción | cortocircuito | `X_p ≈ 0`, elemento resonante a λ/4 | reflector |
| PIN en corte | circuito abierto | `X_p → −∞`, `I_p → 0` | transparente |

Consecuencias que el diseño debe asumir, y que DOC-02 menciona pero no cuantifica:

1. **El espacio de configuraciones es finito**: 2⁶ = 64 estados. No hay ajuste fino.
2. **El control de nulos es grueso.** Con varactores, la literatura reporta nulos más profundos
   que −50 dB [2]; con PIN la profundidad depende de la superposición de pocos estados discretos y
   será del orden de 10–20 dB. Se declara en `DOC-03` y se mide en `A3`: prometer más sería
   indefendible ante los jueces.
3. **La reactancia no es exactamente cero ni exactamente infinita.** El PIN en conducción tiene
   1.5 Ω en serie más la inductancia del lazo (~1 nH), y en corte 0.18 pF no es un circuito abierto
   perfecto a 2.44 GHz (`|Z| ≈ 360 Ω`). Ambos efectos se declaran como error de modelo y se cubren
   con la medición, no con la simulación.
4. **Limitación del modelo de puerto único.** El modelo `(Z + diag(...))·I = v` supone un modo por
   elemento y representa mal un elemento abierto, que sigue reirradiando por su distribución de
   corriente. Por eso `DOC-04` no fija dimensiones finales con este modelo: fija **rangos** y un
   plan de barrido, y la geometría se cierra con simulación de onda completa y medición.

## 4. Simetría C6 y tamaño real del espacio de patrones

Los seis parásitos están sobre un anillo regular de 60°. La estructura tiene simetría rotacional
C6: girar el estado un sector produce el mismo patrón girado 60°. El número de patrones
**distintos** es entonces el número de órbitas de las cadenas binarias de longitud 6 bajo C6, que
se cuenta con el lema de Burnside:

```
|X/G| = (1/|G|) · Σ_{g∈G} |Fix(g)|

C6 gira en pasos de 1..6 sectores. Una cadena queda fija bajo un giro de k sectores solo si es
periódica con período mcd(6,k). Con g=6⁰,6¹,...,6⁵:

Órbitas = (1/6) · [ φ(1)·2⁶ + φ(2)·2³ + φ(3)·2² + φ(6)·2¹ ]
        = (1/6) · [ 1·64 + 1·8 + 2·4 + 2·2 ]
        = (1/6) · [ 64 + 8 + 8 + 4 ]
        = 14
```

Es el resultado que DOC-02 cita sin demostrar. La descomposición completa por cantidad de
parásitos activos (`k`) es 1 + 1 + 3 + 4 + 3 + 1 + 1 = 14, y el libro de códigos se construye
sobre ella en `DOC-06`.

Esta simetría es una **propiedad del modelo ideal**. En el prototipo se rompe por tolerancias de
fabricación, por el conector SMA descentrado y por las líneas de polarización. Por eso el plan de
verificación mide los seis sectores por separado en lugar de medir uno y suponer los otros cinco
(`T-03`).

## 5. El plano de tierra finito: el efecto que más se subestima

Un monopolo necesita plano de tierra. Si el plano fuera infinito, el máximo de radiación estaría
en el plano horizontal (elevación 0°). Con un plano finito, la corriente que llega al borde
difracta y el lóbulo **sube en elevación**: el máximo se inclina hacia arriba en un ángulo que
crece al reducir el diámetro del plano. En un ESPAR esto es doblemente crítico porque los
parásitos también usan ese plano como referencia [7], [8].

Implicaciones para el diseño:

- El plano de tierra es una **variable de diseño** (`DV-03`), no un detalle mecánico.
- DOC-02 propone 12–18 cm de diámetro (0.98λ–1.47λ). El extremo bajo inclina demasiado el haz para
  un enlace a la altura de la mesa; el extremo alto mejora la horizonte pero complica el montaje y
  el transporte (`C3.3`).
- La mitigación de la literatura es la **falda** (*ground skirt*): una pared conductora vertical en
  el borde del plano que recupera directividad cerca del horizonte sin agrandar el diámetro [7], [8].
  Se adopta como opción de reserva, no como diseño base: agrega piezas al montaje rápido.

## 6. Qué se espera en números

Para fijar expectativas antes de medir, con base en la literatura de arreglos de 7 elementos en
2.4 GHz [3], [5]:

| Magnitud | Expectativa realista | Fuente de la expectativa |
| --- | --- | --- |
| Ganancia en el sector activo | 6–9 dBi sobre el monopolo solo | [3] mide 7 elementos en ISM; [2] reporta 9 dBi para 5 elementos con varactores |
| Ancho de haz a −3 dB | 60–100° en azimut | 3 reflectores contiguos sobre 6 posiciones |
| Relación delante/detrás | 10–20 dB en el mejor sector | objetivo `A2` ≥ 10 dB; `T-03` |
| Profundidad de nulo | 10–20 dB, posición cuantizada a múltiplos de 30–60° | consecuencia del §3.2 |
| Cobertura | 360° en azimut por los 6 sectores | simetría C6, §4 |
| Ganancia en el sector opuesto | por debajo del omnidireccional | es lo que habilita el modo sensado |

Si la relación delante/detrás medida no llega a 10 dB, la respuesta no es cambiar de tecnología:
es la compuerta 1 de `DOC-08` (iterar longitud de parásitos y diámetro de plano antes de tocar la
topología).

## 7. Por qué esta arquitectura sirve a ISAC

El requisito `R4` pide haz hacia el transmisor deseado **y** supresión del interferente. El `R3`
pide detectar movimiento o posición. Los dos modos se reducen a lo mismo: **elegir un estado del
libro de códigos y medir la señal por dirección**.

- **Comunicación**: barrido de los seis sectores, se elige el de mayor RSSI del TX deseado por MAC
  y se mantiene. La ganancia de SIR viene de la relación delante/detrás.
- **Sensado**: se elige el estado que **minimiza** la señal del iluminador conocido (router), lo
  que suprime el trayecto directo y deja visible la energía reflejada por el cuerpo en movimiento;
  después se barre sector por sector y se compara la varianza temporal de RSSI.
- **Simultáneo**: alternancia estado a estado entre paquetes. Es viable porque la conmutación del
  PIN es de microsegundos y el intervalo entre paquetes de milisegundos (`A4`).

Lo que hace original al proyecto no es el ESPAR —existe desde 1978— sino **usar el nulo dirigido al
iluminador como mecanismo de sensado en un receptor pasivo de bajo costo**. El análisis de vacío
del estado del arte está en `docs/teoria/02-estado-del-arte.md` §9.

## Referencias

[1] R. F. Harrington, «Reactively controlled directive arrays», *IEEE Trans. Antennas Propag.*, vol. 26, n.º 3, pp. 390–395, 1978.
[2] K. Gyoda y T. Ohira, «Design of electronically steerable passive array radiator (ESPAR) antennas», *IEEE AP-S Int. Symp.*, 2000. DOI 10.1109/APS.2000.875370.
[3] F. S. Caluyo y A. H. Ballado, «Design of a 7-element Electronically Steerable Passive Array Radiator (ESPAR) antenna for the ISM band», *COMCAS*, 2011. DOI 10.1109/COMCAS.2011.6105844.
[7] Y. Ojiro, H. Kawakami, K. Gyoda et al., «Improvement of elevation directivity for ESPAR antennas with finite ground plane», *IEEE AP-S Int. Symp.*, 2001. DOI 10.1109/APS.2001.959390.
[8] R. Schlub, J. Lu y T. Ohira, «Seven-element ground skirt monopole ESPAR antenna design from a genetic algorithm and the finite element method», *IEEE Trans. Antennas Propag.*, vol. 51, n.º 11, pp. 3033–3039, 2003. DOI 10.1109/TAP.2003.818790.
[9] Skyworks Solutions, «SMP1345 Series: Very Low Capacitance, Plastic Packaged Silicon PIN Diodes», hoja de datos 200046U.

La numeración es la de `docs/teoria/02-estado-del-arte.md`, que es la lista maestra.
