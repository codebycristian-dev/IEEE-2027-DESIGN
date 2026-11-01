# N-02 — Estado del arte y análisis de vacío

Nota técnica de respaldo. Estado: vigente. Es la **lista maestra de referencias** del proyecto: si
un documento cita `[n]`, el número es el de este archivo. Reemplaza la numeración de DOC-02.

## 1. Método de la revisión

- **Pregunta que guía la búsqueda:** ¿existe un ESPAR de 7 elementos con conmutación binaria por
  diodos PIN, en 2.4 GHz, usado como **receptor** para detección y comunicaciones simultáneas?
- **Criterios de inclusión:** prototipo construido y medido; banda de microondas/ISM; mecanismo de
  reconfiguración explícito; aporte metodológico verificable (geometría, plano de tierra, nulos,
  control).
- **Criterios de exclusión:** resultados solo simulados sin validación; arreglos con alimentación
  por elemento; ESPAR en bandas milimétricas sin relación con el diseño.
- **Fecha de la búsqueda:** 2026-10-14.
- **Límite declarado y honesto:** de las referencias listadas se verificó la **existencia y los
  metadatos** (DOI, venue, autores, año). **No se leyó el texto completo de todas.** La columna
  «lectura» del §11 dice cuáles están pendientes y por qué importan. Una referencia sin leer no
  debe sostener una cifra de la propuesta: para eso están las mediciones propias.

## 2. Línea 1 — ESPAR de carga reactiva continua

El origen es Harrington [1]: un arreglo de directividad controlada reactivamente demuestra que
variando la reactancia de terminación de los elementos no alimentados se puede sintetizar un
patrón directivo con un solo puerto de RF. Es la base teórica de todo lo que sigue y el sustento
del modelo de la ec. (1) de `N-01`.

Ohira y Gyoda [2] llevan la idea a un prototipo de 5 elementos y reportan 9 dBi ± 1 dB de ganancia
de haz y nulos más profundos que −50 dB en dirección arbitraria. Esa cifra de nulos **no es
trasladable** a este proyecto: usa varactores con control analógico continuo. La cita sirve para
dos cosas: mostrar el techo de la arquitectura y explicar qué se pierde al bajar a un PIN binario.

## 3. Línea 2 — Parásitos conmutados discretos

Vaughan [4] y Thiel, O'Keefe y Lu [5] establecen el control discreto: conmutar un parásito entre
cortocircuito y circuito abierto en el punto de máxima corriente inducida alcanza para dirigir el
haz. Es exactamente la operación del PIN de este proyecto.

Schlub [6], en su tesis, sistematiza la realización práctica: monopolos parásitos con carga
estática, simetría para reproducir el haz en todo el azimut, y el conjunto de efectos parásitos que
arruinan la coincidencia entre simulación y medición. Es la referencia más útil para `DOC-04`
porque está centrada en **monopolos sobre plano de tierra**, no en parches.

Schlub, Lu y Ohira [8] aplican optimización genética con método de elementos finitos a un ESPAR de
**7 elementos** —la misma cuenta de elementos que este proyecto— con falda de plano de tierra y
reportan el procedimiento de diseño completo. Es la referencia de método: no se copia su geometría,
se copia la disciplina de optimizar con variables declaradas en vez de fijar cotas a ojo.

## 4. Línea 3 — ESPAR en 2.4 GHz / banda ISM

Caluyo y Ballado [3] diseñan, fabrican y miden un ESPAR de **7 elementos para la banda ISM**, con
ganancia, HPBW, SWR y pérdida de retorno medidas, y concluyen capacidad de rechazo de interferencia.
Es el antecedente más cercano al proyecto en banda y número de elementos, y fija la expectativa
realista de ganancia de `N-01` §6.

Komiyama, Ohira y Tanaka [14] documentan el uso de ESPAR en redes ad hoc a 2.4 GHz, lo que aporta
el argumento de aplicación: la antena inteligente de bajo costo tiene un caso de uso real en redes
de paquetes, que es el escenario de ISAC del concurso.

## 5. Línea 4 — Conmutación: PIN frente a MEMS y varactores

Jusoh et al. [10] comparan PIN (HPND-4005) y MEMS (RMSW101) en un parásito conmutado a 2.38 GHz con
cuatro parásitos alrededor de un elemento activo. Confirma dos cosas: que el PIN es suficiente para
conmutar el patrón, y que introduce pérdida y una inductancia de lazo que corre la resonancia.
Ambas consecuencias están en `DOC-05`.

Kang, Choi y Lee [11] presentan un ESPAR compacto con **ocho parásitos controlados por diodos PIN**
que produce ocho haces de azimut y cuatro de elevación, para UAV. Es la evidencia más reciente de
que un arreglo PIN discreto y liviano es construible por un grupo pequeño — el argumento de
viabilidad de cronograma que DOC-02 usa a favor del ESPAR.

Cetiner et al. [19] muestran el extremo opuesto: reconfigurabilidad multifunción con RF-MEMS. Se
cita solo para explicar por qué no se usa MEMS (costo, drivers de alta tensión, fragilidad), no
como alternativa real bajo la restricción del mentor.

## 6. Línea 5 — Plano de tierra y directividad de elevación

Ojiro, Kawakami y Gyoda [7] cuantifican el efecto que más se subestima: el plano de tierra finito
**baja el ángulo de máxima radiación** y degrada la directividad en elevación; la falda en el borde
lo corrige. Schlub, Lu y Ohira [8] adoptan esa falda en su ESPAR de 7 elementos.

Para este proyecto implica que el diámetro del plano es una variable de diseño (`DV-03`) con
compromiso explícito entre directividad en elevación y tamaño de transporte (`C3.3`), y que la
falda es plan B, no diseño base. Ver `DOC-04` §5.

## 7. Línea 6 — Nulos y control de interferencia

Konch et al. [13] diseñan un arreglo de parásitos conmutados de 8 elementos con foco explícito en
**null steering**, incluido un elemento activo octagonal con parásitos rectangulares. Aporta el
vocabulario y las métricas para describir nulos discretos.

Han y Ohira [12] evalúan estadísticamente decenas de ESPAR medidos y muestran cómo extraer
parámetros reales para **predecir** el comportamiento adaptativo. Es la referencia metodológica de
`DOC-07`: medir un número suficiente de unidades y estados para reportar dispersión, en vez de un
caso favorable único.

## 8. Línea 7 — Alternativas ya descartadas (solo contraste)

RIS de 1 bit [16], [17] y antena de píxeles [18] quedaron fuera por decisión `D-05`/`D-06` de
DOC-02 y este repositorio **no las reevalúa**. Se citan únicamente para dos frases de la propuesta:

- **RIS**: los lóbulos de cuantización de 1 bit y el requisito de campo lejano son la razón técnica
  del descarte, no una preferencia [16]. La evalución completa está en DOC-01.
- **Píxeles**: la reconfigurabilidad existe hace más de una década [18]; el problema es la
  variabilidad entre copias y el cableado, no la idea.

## 9. Análisis de vacío: qué no está resuelto

Comparación de los antecedentes que de verdad compiten con este diseño:

| Trabajo | Elementos | Mecanismo | Banda | Resultado reportado | Papel en nuestro diseño |
| --- | --- | --- | --- | --- | --- |
| Harrington [1] | N parásitos | reactivo continuo | — | prueba de concepto teórica | base del modelo |
| Gyoda y Ohira [2] | 5 | varactores | ~2.5 GHz | 9 dBi ± 1 dB, nulos < −50 dB | techo de la arquitectura |
| Caluyo y Ballado [3] | 7 | conmutación | ISM 2.4 GHz | ganancia, HPBW y SWR medidos | expectativa realista de ganancia |
| Schlub et al. [8] | 7 | conmutación + falda | ~2.4 GHz | diseño por GA/FEM | método de optimización |
| Kang et al. [11] | 8 parásitos | PIN | UAV | 8 haces azimut + 4 elevación | evidencia de viabilidad |
| Konch et al. [13] | 8 | conmutación | parche | control de nulos | métricas de nulos |
| **Este proyecto** | **6 parásitos + 1 activo** | **PIN binario** | **2400–2483.5 MHz** | por medir (`A1`–`A5`) | — |

Lo que **falta** en la literatura revisada, y por eso el proyecto tiene algo que decir:

1. **El ESPAR como receptor, no como radiador.** Prácticamente todos los antecedentes optimizan la
   antena de transmisión. Acá la antena recibe, y lo que se optimiza es la **relación entre dos
   señales recibidas**: la del TX deseado y la del interferente (`A3`). Eso cambia el criterio de
   diseño: importa el rechazo, no la ganancia absoluta.
2. **El nulo dirigido al iluminador como mecanismo de sensado.** La literatura de ESPAR discute
   nulos para cancelar interferencia, no para **suprimir el trayecto directo** y dejar visible la
   energía reflejada por un cuerpo en movimiento. Este es el aporte conceptual original del
   proyecto, y es lo que sostiene `C1.1` y `C1.2` en la evaluación del concurso.
3. **Modos conmutados en el tiempo sobre un receptor comercial.** La alternancia estado a estado
   entre paquetes de Wi-Fi, con métrica por MAC, no aparece en la literatura de ESPAR, que asume
   un receptor dedicado con control propio.
4. **Trazabilidad de diseño a nivel de aula.** Los trabajos citados reportan resultados; ninguno
   publica el paquete completo de requisitos, decisiones, variables y protocolos de verificación
   que permita a otro grupo replicarlo. Eso es exactamente `C4.2` (replicabilidad) y es lo que este
   repositorio produce.

## 10. Competencia: qué premian los jueces

Del historial del concurso recogido en DOC-02 §4.3 y en las fuentes [22]–[26]:

- 2021: ganó un arreglo con visualización extremadamente simple (una franja de luz que seguía al
  transmisor).
- 2023: tema RIS; ganaron soluciones con aplicación clara (agricultura inteligente) y montaje
  robusto.
- 2025: primero un sistema mecánico; segundo un SDR con arreglo de antenas.
- Competencia: 30 propuestas en 2022, 34 equipos en 2024, para 6 cupos de semifinalista.

Patrón: **premia lo robusto, lo visual y lo replicable por encima de la sofisticación del
hardware.** Un RIS de 64 diodos es más vistoso que un ESPAR de 6 y perdió por frágil. Esta lectura
es la que justifica insistir en visualización (anillo de LEDs, panel en tiempo real) como parte del
diseño y no como adorno.

## 11. Referencias

Estado de lectura: **[L]** leída completa · **[M]** metadatos verificados (DOI/venue), texto
pendiente · **[W]** fuente web/documentación técnica.

| # | Referencia | Estado |
| --- | --- | --- |
| [1] | R. F. Harrington, «Reactively controlled directive arrays», *IEEE Trans. Antennas Propag.*, vol. 26, n.º 3, pp. 390–395, 1978. | [M] |
| [2] | K. Gyoda y T. Ohira, «Design of electronically steerable passive array radiator (ESPAR) antennas», *IEEE AP-S Int. Symp.*, 2000. DOI 10.1109/APS.2000.875370. | [M] |
| [3] | F. S. Caluyo y A. H. Ballado, «Design of a 7-element Electronically Steerable Passive Array Radiator (ESPAR) antenna for the ISM band», *COMCAS*, 2011. DOI 10.1109/COMCAS.2011.6105844. | [M] |
| [4] | R. Vaughan, «Switched parasitic elements for antenna diversity», *IEEE Trans. Antennas Propag.*, vol. 47, n.º 2, pp. 399–405, 1999. | [M] |
| [5] | D. V. Thiel, S. G. O'Keefe y J. Lu, «Electronic beam steering in wire and patch antenna systems using switched parasitic elements», *IEEE AP-S Int. Symp.*, 1996. DOI 10.1109/APS.1996.549655. | [M] |
| [6] | R. Schlub, *Practical Realization of Switched and Adaptive Parasitic Monopole Radiating Structures*, tesis doctoral, Griffith University, 2004. DOI 10.25904/1912/3832. | [M] |
| [7] | Y. Ojiro, H. Kawakami, K. Gyoda et al., «Improvement of elevation directivity for ESPAR antennas with finite ground plane», *IEEE AP-S Int. Symp.*, 2001. DOI 10.1109/APS.2001.959390. | [M] |
| [8] | R. Schlub, J. Lu y T. Ohira, «Seven-element ground skirt monopole ESPAR antenna design from a genetic algorithm and the finite element method», *IEEE Trans. Antennas Propag.*, vol. 51, n.º 11, pp. 3033–3039, 2003. DOI 10.1109/TAP.2003.818790. | [M] |
| [9] | Skyworks Solutions, «SMP1345 Series: Very Low Capacitance, Plastic Packaged Silicon PIN Diodes», hoja de datos 200046U. | [W] |
| [10] | M. Jusoh, M. F. Jamlos, M. Nawawi et al., «Switchable parasitic antenna using PIN Diode- and MEMS-switches», *IEEE RFM*, 2013. DOI 10.1109/RFM.2013.6757283. | [M] |
| [11] | M. Kang, Y.-S. Choi y W.-S. Lee, «Compact-size lightweight beam-reconfigurable ESPAR antenna with parasitic elements for UAV applications», *ACES Journal*, 2024. DOI 10.13052/2024.aces.j.390507. | [M] |
| [12] | Q. Han y T. Ohira, «Statistical evaluation of ESPAR antennas and adaptive beamforming performance prediction using extracted parameters», *APMC*, 2005. DOI 10.1109/APMC.2005.1606984. | [M] |
| [13] | R. Konch, A. Sarma, S. Goswami et al., «Design of a pattern reconfigurable switched parasitic array for null steering application», *IEMENTech*, 2018. DOI 10.1109/IEMENTECH.2018.8465337. | [M] |
| [14] | B. Komiyama, T. Ohira y S. Tanaka, «ESPAR antenna: an adaptive antenna for mobile terminals and its application to wireless ad hoc networks», *SPIE*, 2004. DOI 10.1117/12.560664. | [M] |
| [15] | J. Lu, D. Ireland y R. Schlub, «Dielectric embedded ESPAR (DE-ESPAR) antenna array for wireless communications», *IEEE Trans. Antennas Propag.*, 2005. DOI 10.1109/TAP.2005.852517. | [M] |
| [16] | T. J. Cui, M. Q. Qi, X. Wan, J. Zhao y Q. Cheng, «Coding metamaterials, digital metamaterials and programmable metamaterials», *Light: Science & Applications*, vol. 3, e218, 2014. | [M] |
| [17] | Y. Liu y C. Sarris, «Harnessing mutual coupling to suppress quantization lobes in 1-bit reconfigurable intelligent surfaces», *IEEE AP-S/URSI 2025*. | [M] |
| [18] | D. Rodrigo y L. Jofre, «Frequency and radiation pattern reconfigurability of a multi-size pixel antenna», *IEEE Trans. Antennas Propag.*, vol. 60, n.º 5, pp. 2219–2225, 2012. | [M] |
| [19] | B. A. Cetiner et al., «Multifunctional reconfigurable MEMS integrated antennas for adaptive MIMO systems», *IEEE Commun. Mag.*, vol. 42, n.º 12, pp. 62–70, 2004. | [M] |
| [20] | S. M. Hernandez, «ESP32 CSI Tool», https://github.com/StevenMHernandez/ESP32-CSI-Tool | [W] |
| [21] | Espressif Systems, «ESP32 Series Datasheet» (GPIO, RSSI por paquete). | [W] |
| [22] | IEEE AP-S, «AP-S Student Design Contest Winners», https://ieeeaps.org/awards/ap-s-student-awards/ap-s-student-design-contest-winners | [W] |
| [23] | IEEE AP-S/URSI 2023, «2023 IEEE AP-S Student Design Contest: Reconfigurable Intelligent Surfaces», https://2023.apsursi.org/sdc.php | [W] |
| [24] | KAUST CEMSE, «KAUST students' research wins first place at IEEE AP-S/URSI 2022», 2022. | [W] |
| [25] | Boğaziçi University, «IEEE AP-S Student Design Contest» (BOUNtenna, 3.º de 34 equipos), 2024. | [W] |
| [26] | BYU Electrical & Computer Engineering, «BYU Capstone team creates world-champion educational device». | [W] |
| [27] | DigiKey, «SMP1345-079LF», precios por cantidad, consultado el 2026-10-13. | [W] |

### Referencias por verificar

No se incluyen en la lista maestra hasta confirmar metadatos. Se mencionan porque son candidatas
naturales para la lectura de `DOC-04` y `DOC-05`:

- C. Sun, A. Hirata, T. Ohira y H. Hirasawa, «Fast beamforming of electronically steerable passive
  array radiator antennas: theory and experiment» — *candidata*, año y volumen por confirmar.
- Literatura de estimación de CSI con ESP32 para detección de presencia: no se localizó todavía un
  trabajo revisado por pares que use conmutación de parásitos junto con CSI de ESP32. **Su ausencia
  es parte del argumento de originalidad** (§9.2), y por eso debe verificarse antes de afirmarlo en
  la propuesta.

## 12. Deuda de lectura

Antes de que una cifra de referencia entre a la propuesta, el trabajo pendiente es:

| Referencia | Qué hay que extraer | Bloquea a |
| --- | --- | --- |
| [3] | ganancia y HPBW medidos, geometría exacta, distancia entre elementos | `DOC-04` §4 (valores esperados) |
| [8] | variables del GA, diámetro de plano y falda, rango de radio de anillo | `DOC-04` §3 (rangos de `DV`) |
| [6] | efectos que rompen simulación vs. medición con monopolos parásitos | `DOC-07` (qué medir y con qué detalle) |
| [7] | cuantificación del tilt de elevación vs. diámetro de plano | `DOC-04` §5 |
| [2] | condiciones en que se obtienen los nulos profundos | `DOC-03` (declaración de expectativas) |

Mientras esa lectura no ocurra, toda cifra tomada de la literatura se marca como **expectativa**,
no como especificación. Las especificaciones se cierran con `A1`–`A5` medidas (`DOC-07`).
