# DOC-03 — Especificación de diseño del ESPAR de 7 elementos

| Código | DOC-03 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-02 v2.0, Registro del proyecto y decisión final de tecnología (2026-10-13) |
| Tipo | Especificación de diseño |
| Estado | Vigente. Reemplaza la propuesta técnica de DOC-02 |
| Autores | Equipo del proyecto (C. Dorado, J. Chivatá, S. Gonzalez) |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Primera especificación con decisiones trazables. Recoge la topología de DOC-02 §5.1 y la convierte en requisitos verificables con alternativas descartadas. |

## 1. Objeto y alcance

Este documento fija **qué se construye y por qué**, con una decisión por cada elección de diseño y
la alternativa que se descartó. Es el documento que un evaluador lee para saber si el diseño está
fundamentado o si salió de una corazonada.

Lo que este documento **no** hace:

- No reevalúa la tecnología: la decisión ESPAR frente a RIS y antenas de píxeles está cerrada en
  DOC-01 y DOC-02 (§7). Cambiarla requiere la compuerta 4 de `DOC-08`.
- No fija las cotas finales: eso es `DOC-04`, y se cierra con barrido y medición, no acá.
- No implementa: `DOC-05` (electrónica), `DOC-06` (códigos), `DOC-07` (verificación).

Lo que **sí** hace, y DOC-02 no hacía: convierte cada afirmación en un `DR-##` de
[`N-04`](../teoria/04-requisitos-y-trazabilidad.md) con criterio y protocolo, y declara las
expectativas numéricas antes de medir.

## 2. Arquitectura del sistema

```
                    ┌──────────────────────────────────────────────┐
                    │  Plano de tierra (PCB circular, DV-03)       │
                    │                                              │
                    │        P2        P3                          │
                    │          \      /                            │
                    │    P1 ── ( A ) ── P4      A = monopolo activo │
                    │          /      \            (λ/4)           │
                    │        P6        P5                          │
                    │      anillo r = DV-02, pasos de 60°          │
                    │                                              │
                    │  Base de cada Pn: PIN en serie a tierra (DEC-06)│
                    │  Línea de polarización por la cara inferior  │
                    └───────────────┬──────────────────────────────┘
                                    │ SMA (activo)
                    ┌───────────────┴──────────────┐
                    │  ESP32 (DEC-12)              │
                    │   · 6 GPIO → 6 líneas de bias│
                    │   · RSSI por paquete y MAC   │
                    │   · libro de códigos (DOC-06)│
                    │   · pin de monitoreo (T-05)  │
                    └───────────────┬──────────────┘
                                    │ USB 5 V
                    ┌───────────────┴──────────────┐
                    │  Interfaz: panel web + anillo│
                    │  de 6 LEDs (DEC-14)          │
                    └──────────────────────────────┘
```

Bloques y su documento:

| Bloque | Decide en | Detalla en |
| --- | --- | --- |
| Antena (elementos, anillo, plano) | DEC-01…DEC-10 | DOC-04 |
| Electrónica de control y polarización | DEC-06, DEC-08, DEC-09 | DOC-05 |
| Control y adquisición | DEC-12 | `firmware/espar-esp32/` |
| Libro de códigos | DEC-13 | DOC-06 |
| Verificación | — | DOC-07 |

## 3. Requisitos

Los requisitos de diseño son `DR-01`…`DR-18` de
[`N-04`](../teoria/04-requisitos-y-trazabilidad.md) §3. No se repiten acá para que exista una sola
fuente de verdad. Este documento es responsable de **satisfacerlos**, no de redefinirlos.

## 4. Decisiones de diseño

Cada decisión tiene alternativa descartada. Una decisión sin alternativa descartada es una
preferencia, y las preferencias no se defienden ante un jurado.

### DEC-01 — Topología: arreglo de parásitos conmutados con un solo elemento alimentado

**Decisión:** 1 monopolo activo central + 6 monopolos parásitos en anillo, un solo puerto de RF.

**Alternativas descartadas:**

| Alternativa | Por qué no |
| --- | --- |
| Arreglo de fase alimentado (2×2, 1×4) | requiere un canal de RF y un desfasador por elemento; incompatible con un receptor comercial y con `R7` |
| RIS de 1 bit | 64 diodos, panel de ~50 cm, campo lejano a 3.9 m y lóbulo de cuantización; descartada en DOC-01 |
| Antena de píxeles | hasta 60 uniones, adaptación variable por estado y variabilidad entre copias; descartada en DOC-01 |
| Yagi conmutada en azimut (varias Yagis y un switch) | más volumen, conmutación de RF (pérdida e aislamiento) y una sola dirección por rama |

**Motivo:** es la única topología que da control de patrón **sin control de RF**. Con el ESP32
recibiendo, la única forma de actuar es cambiar la antena; el ESPAR hace exactamente eso y además
usa seis interruptores de continua como única electrónica de mando.

**Consecuencia:** la ganancia por sector será moderada (6–9 dBi esperados, `N-01` §6) y los nulos
serán discretos. Se acepta: la propuesta no compite por ganancia sino por capacidad de elegir
dirección con hardware mínimo.

### DEC-02 — Mecanismo de reconfiguración: diodo PIN SMP1345

**Decisión:** un diodo PIN Skyworks SMP1345-079LF por parásito, conmutado a tierra.

**Alternativas descartadas:**

| Alternativa | Por qué no |
| --- | --- |
| Varactor | permite control continuo y nulos profundos, pero requiere DAC y 6 tensiones analógicas; además la restricción del mentor fija PIN |
| RF-MEMS | drivers de 30–80 V, fragilidad y costo; incompatible con `R8` |
| Relé de RF | milisegundos de conmutación, tamaño y consumo; incumple `A4` |
| PIN BAR63 / BAP64 | capacitancia mayor en corte o menor corriente de conducción; sin ventaja frente a SMP1345, que ya está elegido y presupuestado |

**Motivo:** `R_s ≈ 1.5 Ω` a 10 mA y `C ≈ 0.18 pF` en corte dan una razón de impedancia suficiente
para conmutar un monopolo λ/4 a 2.44 GHz. Es el componente de referencia de DOC-02 y su costo
unitario (US$0.31–0.56) lo mantiene irrelevante en el presupuesto.

**Consecuencia:** 64 estados posibles, nulos discretos, y una inductancia de lazo que corre la
resonancia (documentada en `DOC-05`). La profundidad de nulo prometida baja de lo que reporta la
literatura con varactores.

### DEC-03 — Elemento radiante: monopolo de varilla λ/4

**Decisión:** monopolos verticales de varilla (latón o cobre) de ≈ λ/4 sobre plano horizontal.

**Alternativas descartadas:** dipolo impreso (necesita balun y plano de tierra separado),
parche (sin acceso a la base para el interruptor y ancho de banda menor), PIFA (difícil de
sintonizar sin simulación).

**Motivo:** el interruptor tiene que estar en la **base** del parásito, donde la corriente inducida
es máxima, y eso exige un elemento vertical con acceso mecánico a ese punto. Además permite
**ajustar la longitud a mano**, que es la variable de sintonía más útil en el banco de trabajo y la
que hace viable llegar al prototipo v1 en el cronograma.

**Consecuencia:** polarización lineal vertical fija (declarado en DOC-02 §5.1 y aceptado); plano de
tierra obligatorio; el haz se inclina en elevación (§`DOC-04`).

### DEC-04 — Número de elementos: 7 (1 + 6)

**Decisión:** un activo y seis parásitos.

**Alternativas descartadas:** 5 elementos (1+4) → sectores de 90° sin solapamiento y huecos entre
haces; 8 elementos (1+7) → anillo no regular, rompe la simetría C6, suma dos diodos y dos líneas sin
mejorar la cobertura; 9 elementos (1+8) → igual problema y más que el doble de estados.

**Motivo:** seis es el menor número que produce **sectores regulares de 60° con solapamiento** y
simetría rotacional exacta. Es también el tamaño que la literatura reporta con resultados medidos en
2.4 GHz [3] y con método de diseño explícito [8].

**Consecuencia:** 14 patrones distintos y un libro de códigos pequeño (DOC-06), que es una ventaja
para `A1` (menos estados que verificar) y para `R8` (menos soldaduras).

### DEC-05 — Geometría del anillo: regular, pasos de 60°

**Decisión:** los seis parásitos sobre una circunferencia, equiespaciados, con el activo en el centro.

**Alternativa descartada:** anillo elíptico o hexagonal irregular para maximizar el lóbulo principal
en una dirección preferida. Se descarta porque el requisito es cobertura de 360° (`DR-03`) y porque
rompe la simetría que hace reproducible el libro de códigos.

**Consecuencia:** el patrón de un estado rotado 60° es el patrón girado. Se aprovecha para reducir
estados y para **detectar errores de montaje**: si el sector 3 no se parece al sector 1 girado, hay
una asimetría física que la simulación no explica.

### DEC-06 — Carga del parásito: cortocircuito a tierra con el PIN en la base

**Decisión:** el PIN conecta la base del parásito a tierra; la polarización entra por una línea de
alta impedancia de RF en el mismo nodo.

**Alternativas descartadas:**

| Alternativa | Por qué no |
| --- | --- |
| PIN en serie dentro del elemento (a media altura) | alarga eléctricamente el elemento y mete el interruptor en una zona de alta corriente con más pérdida; usado en [10] con resultado aceptable, pero es más difícil de fabricar a mano |
| Carga capacitiva fija + PIN que la conmuta | dos componentes por parásito, y la capacidad agregada reduce el contraste entre estados |
| PIN en paralelo con una inductancia fija | permite un tercer estado (carga inductiva) pero necesita 6 inductores más y multiplica los estados a analizar |

**Motivo:** cortocircuito en la base maximiza la corriente inducida, es la operación clásica de
parásito conmutado [4], [5] y requiere **una sola línea de polarización por elemento**.

**Consecuencia:** dos estados por elemento. El "abierto" no es perfectamente transparente
(la capacidad de 0.18 pF a 2.44 GHz equivale a ≈ 360 Ω), lo que aporta una interacción residual
que se mide, no se modela.

### DEC-07 — Red de adaptación del elemento activo

**Decisión:** red L fija, calculada para el **estado promedio ponderado** del libro de códigos, en
el plano del conector SMA.

**Alternativa descartada:** sin red de adaptación. El monopolo activo ve la impedancia mutua de los
seis parásitos, que cambia con el estado. Sin red, `|S11|` en 2.4 GHz queda fuera de la máscara en
varios estados y `A1` es inalcanzable. Esta es la corrección más importante respecto de DOC-02.

**Alternativa considerada y no adoptada de entrada:** red conmutada por estado. Duplicaría las
líneas de control y agregaría 6 componentes; queda como plan B si `T-02` muestra que una red fija no
alcanza para los estados del subconjunto útil.

**Motivo:** con una red fija, el peor estado del subconjunto definido en DOC-06 puede quedar dentro
de la máscara si el libro de códigos se elige con ese criterio. La red se dimensiona **después** de
medir los estados, sobre el estado que minimiza la peor desadaptación.

**Consecuencia:** `A1` se evalúa sobre el subconjunto cargado, no sobre los 64 estados (ver DOC-09).

### DEC-08 — Control: GPIO directo del ESP32

**Decisión:** seis GPIO directos, uno por línea de polarización.

**Alternativas descartadas:** registro de desplazamiento 74HC595 (agrega un componente de montaje
superficial y un protocolo serie, y el ESP32 ya tiene pines de sobra); ULN2003 (solo necesario si se
busca más corriente que la que admite el GPIO); expansor I²C (latencia innecesaria para `A4`).

**Motivo:** 11 mA por línea cae dentro de lo que un GPIO entrega de forma segura, y seis líneas
directas son las menos piezas posibles (`R8`). El pin de monitoreo de conmutación también sale
directo, lo que hace medible `A4` sin instrumentación adicional.

**Consecuencia y plan B:** si una medición muestra caída de tensión o ruido acoplado al dominio de
RF, se intercala un ULN2003 sin cambiar el resto del diseño.

### DEC-09 — Red de polarización: resistencia de limitación + choke de RF

**Decisión:** por cada parásito, `GPIO → R_limit → choke → nodo base/PIN → tierra`, con el choke
dimensionado para `|Z| ≥ 300 Ω` a 2.44 GHz y la línea ruteada por la cara inferior del plano.

**Alternativas descartadas:** resistor de alto valor como choke (cae demasiada tensión: con 11 mA
haría falta disipar watts); línea de λ/4 como choke impreso (funciona en banda angosta y ocupa
mucho espacio en una PCB de 15 cm con 6 líneas); polarización inductiva sin resistencia (corriente
no controlada, riesgo de quemar el diodo).

**Motivo:** es la topología estándar de un interruptor PIN con alimentación por bobina de bloqueo,
y la que DOC-02 ya había identificado como necesaria.

**Consecuencia:** la línea de polarización sigue siendo un conductor cerca del plano, y por eso
`R-05` de `DOC-08` la trata como riesgo de acoplamiento. Se verifica midiendo el patrón con y sin
las líneas conectadas.

### DEC-10 — Plano de tierra: PCB circular de doble cara

**Decisión:** placa circular de FR4 con cobre en ambas caras, diámetro nominal 15 cm (`DV-03`),
perforaciones para los siete monopolos y para el conector SMA.

**Alternativas descartadas:** chapa de aluminio (excelente conductor pero no integra las líneas ni
la electrónica, obliga a cablear por arriba y suma altura); plano cuadrado (más fácil de cortar,
pero los bordes rectos producen difracción asimétrica que ensucia el patrón).

**Motivo:** el cobre de la cara inferior permite rutear las seis líneas de polarización **por
debajo** del plano, que es la mitigación que DOC-02 ya identificaba, y montar la placa de control
sin cables colgando.

**Consecuencia:** la placa es la pieza mecánica principal; hay que prever su rigidez y el refuerzo
del conector SMA.

### DEC-11 — Alimentación: USB de 5 V

**Decisión:** alimentación por USB, con el regulador del propio devkit ESP32 para 3.3 V.

**Alternativas descartadas:** batería LiPo (agrega cargador y protección; se acepta **solo** como
opción de demo, no como diseño base); fuente de banco (no es reproducible en aula, `R8`).

**Motivo:** `DR-13` exige alimentación ≤ 5 V y ausencia de tensiones peligrosas. USB cumple y es lo
que cualquier aula tiene.

**Consecuencia:** 66 mA de polarización más el consumo del ESP32 quedan holgados dentro de los
500 mA de un puerto USB estándar.

### DEC-12 — Receptor: ESP32 con RSSI por paquete y MAC

**Decisión:** ESP32 en modo promiscuo, con RSSI por paquete asociado a la MAC de origen.

**Alternativas descartadas:** SDR ADALM-PLUTO (cuesta más que el presupuesto del sistema de antena y
en 2025 ya compitió un equipo con SDR: no diferencia, y complica `R8`); módulo Wi-Fi dedicado con
API cerrada (no da RSSI por MAC); receptor Bluetooth (la banda es compartida pero el escenario de
interferencia es más pobre).

**Motivo:** el ESP32 da RSSI por paquete con MAC de origen, que es exactamente lo que `A3` necesita
para separar deseado de interferente. El firmware `ESP32-CSI-Tool` [20] permite además CSI si hace
falta más resolución para `A5`.

**Consecuencia:** RSSI entero de 1 dB. Obliga a que todas las métricas críticas sean diferenciales
(`N-03` §3). Si en la campaña de detección el RSSI resulta insuficiente, se pasa a CSI **sin
cambiar la antena**, que es la decisión que importa conservar.

### DEC-13 — Libro de códigos: subconjunto cerrado

**Decisión:** cargar en el firmware un subconjunto cerrado de estados (≤ 25), definido en
`DOC-06`, no los 64.

**Alternativas descartadas:** los 64 estados (50 son rotaciones o complementos que no agregan
información y multiplican el tiempo de barrido y los estados que deben cumplir `A1`);
subconjunto mínimo de 7 (pierde los estados de nulos, que son el aporte original del proyecto).

**Motivo:** con 14 patrones distintos, el subconjunto útil cubre omnidireccional, seis sectores,
estados de haz ancho, estados de un solo parásito activo y estados de nulos. Cada estado cargado se
mide en `T-02` y `T-03`.

**Consecuencia:** `DR-18` es verificable: la lista del firmware y la de DOC-06 tienen que coincidir
exactamente. Si se agrega un estado experimental, se agrega a DOC-06 primero.

### DEC-14 — Visualización: anillo de seis LEDs y panel web

**Decisión:** seis LEDs en el anillo que muestran qué parásitos están activos, más un panel web
servido por el ESP32 con SIR y actividad por sector.

**Alternativas descartadas:** solo panel web (el jurado no ve la antena "pensar"); matriz de LEDs
por celda como en RIS (60 LEDs y cableado, `R8`); display LCD (menos intuitivo para `C4.1`).

**Motivo:** la explicabilidad es criterio de evaluación (`C4.1`, `DR-16`) y el patrón de podios
recientes premia lo visual (`N-02` §10). Un anillo de seis LEDs muestra el estado de la antena sin
que nadie lea un manual.

**Consecuencia:** seis LEDs de bajo consumo en la cara superior, y hay que cuidar que no queden
sobre el plano de tierra en una zona de corriente alta: se montan en el borde y con cable fino.

## 5. Interfaces

### 5.1 Mapa de pines

| GPIO | Función | Nota |
| --- | --- | --- |
| 13 | P1 — parásito a 0° | |
| 14 | P2 — parásito a 60° | |
| 25 | P3 — parásito a 120° | |
| 26 | P4 — parásito a 180° | |
| 27 | P5 — parásito a 240° | |
| 32 | P6 — parásito a 300° | |
| 33 | Pin de monitoreo de conmutación | para `T-05`; replica la escritura del puerto |
| 34 | Entrada analógica libre | reservado para sensor futuro |
| GND / 3V3 | Alimentación de las líneas de polarización | |

Se evitan deliberadamente GPIO 0, 2, 12 y 15 (pines de arranque) y 6–11 (flash).

### 5.2 Interfaz de software

- Estado del libro de códigos = palabra de 6 bits, bit `n` = parásito `Pn` en conducción.
- Modos: `comunicacion`, `sensado`, `simultaneo`, `manual`.
- El panel web expone: modo, estado actual, SIR por par, actividad por sector, y el mapa de los 6
  LEDs.

## 6. Modos de operación

| Modo | Secuencia | Métrica que produce | Requisito |
| --- | --- | --- | --- |
| Comunicación | barrido de los 6 sectores; se fija el de mayor RSSI del TX deseado | `M-04` (SIR) | DR-04, DR-06 |
| Sensado | estado con nulo hacia el iluminador; barrido de los 6 sectores restantes | `M-07` (actividad) | DR-05, DR-09 |
| Simultáneo | alternancia estado a estado entre paquetes | ambas, con marca temporal | DR-07, DR-08 |
| Manual | el operador fija el estado desde el panel | ninguna | DR-17 |

## 7. Criterios de aceptación

Los `A1`–`A5` refinados están en [`N-04`](../teoria/04-requisitos-y-trazabilidad.md) §4, con su
alcance y su banda de guarda. Los protocolos están en `DOC-07`.

Estado actual: **ninguno verificado**. No hay prototipo. Cualquier afirmación en la propuesta debe
rotularse como expectativa hasta que exista la medición.

## 8. Fuera de alcance

- Extensión con varactores (condicionada a que falle `A3`, DOC-08 compuerta 2).
- Control en elevación y reconfiguración de polarización.
- Certificación del sistema para uso fuera del aula.
- Cualquier forma de transmisión (`R1`).

## 9. Trazabilidad de este documento

| Sección | Alimenta a |
| --- | --- |
| §2 arquitectura | figura de la propuesta, página 2 |
| §4 decisiones | tabla de decisiones de la propuesta y `DOC-09` |
| §5 interfaces | `DOC-05`, `firmware/espar-esp32/` |
| §6 modos | `DOC-06`, `DOC-07`, demostración |
| §7 criterios | `DOC-07` |
