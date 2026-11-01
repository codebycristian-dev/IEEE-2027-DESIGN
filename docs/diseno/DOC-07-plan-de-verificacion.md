# DOC-07 — Plan de verificación de los criterios de aceptación

| Código | DOC-07 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-03 v1.0 §7; DOC-02 v2.0 §7.1 |
| Tipo | Plan de verificación |
| Estado | Vigente. **Ningún protocolo ejecutado**: no hay prototipo |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Diez protocolos `T-01`…`T-10` con montaje, procedimiento, tamaño de muestra, criterio y destino de los datos. Agrega los protocolos que DOC-02 no tenía para R1, R6, R7 y R8. |

## 1. Objeto

Convertir los criterios `A1`–`A5` y los requisitos `DR-##` en **procedimientos que otra persona pueda
ejecutar sin preguntar nada**. Un criterio sin protocolo no es un criterio: es una intención.

Regla de lectura: si un resultado se obtiene sin seguir el protocolo escrito acá, no entra a la
propuesta. No porque esté mal, sino porque no es reproducible ni comparable.

## 2. Resumen

| Protocolo | Verifica | `DR` | Duración estimada | Cuándo |
| --- | --- | --- | --- | --- |
| T-01 | recepción pasiva estricta | DR-02 | 1 h | con v0 |
| T-02 | adaptación por estado | DR-01 (A1) | 3 h | con v0 y con v1 |
| T-03 | patrones y relación delante/detrás | DR-03, DR-04 (A2) | 5 h | con v0 y con v1 |
| T-04 | SIR y nulos | DR-05, DR-06 (A3) | 4 h | con v1 |
| T-05 | tiempo de conmutación | DR-07, DR-08 (A4) | 2 h | con v1 |
| T-06 | detección de movimiento | DR-09 (A5) | 4 h | con v1 y demo |
| T-07 | interfaz y visualización | DR-10, DR-17 | 1 h | con v1 |
| T-08 | auditoría de costo | DR-11 | 1 h | antes de enviar |
| T-09 | montaje, seguridad y rearmado | DR-12, DR-13, DR-14 | 2 h | con v1 |
| T-10 | explicabilidad | DR-16 | 1 h | antes de enviar |

Cada ejecución se guarda en `mediciones/AAAA-MM-<asunto>/` con su `README.md` escrito **antes** de
medir.

---

## 3. T-01 — Recepción pasiva estricta

**Motivo.** `R1` es el requisito más fácil de incumplir sin darse cuenta: un módulo ESP32 mal
configurado puede asociarse o emitir balizas. Es también el que un jurado puede objetar.

**Equipo.** SDR de recepción (RTL-SDR, HackRF en modo RX) o analizador de espectro con antena de
referencia; el sistema completo montado y alimentado.

**Montaje.** Antena de referencia a 1 m del arreglo, sin obstáculos, banda 2350–2550 MHz.

**Procedimiento.**
1. Con el sistema **apagado**, capturar el piso de ruido durante 60 s; guardar el registro.
2. Encender el sistema y ponerlo en cada uno de los cuatro modos (comunicación, sensado, simultáneo,
   manual) durante 60 s cada uno.
3. Durante cada modo, conmutar todos los estados del libro de códigos a 1 Hz.
4. Registrar el máximo detectado en la banda en cada caso.
5. Confirmar en el firmware que la interfaz Wi-Fi está en modo estación o monitor, sin asociación y
   sin balizas propias; guardar la captura de configuración.

**Criterio.** Ninguna componente atribuible al sistema por encima de **−80 dBm**, y variación menor a
1 dB entre el registro con el sistema apagado y encendido.

**Datos.** `mediciones/AAAA-MM-recepcion-pasiva/` con los registros del SDR y la captura de la
configuración del firmware.

**Si falla.** No se atenúa nada: se corrige la configuración del receptor. Si el organizador pide
otra forma de documentarlo (`P1`), se rehace el protocolo con su indicación.

---

## 4. T-02 — Adaptación de entrada por estado (A1)

**Equipo.** LiteVNA o NanoVNA; kit de calibración SOL; cables cortos; soporte que no altere la
posición del arreglo.

**Montaje.** El arreglo en su soporte definitivo, a 1.2 m del piso y lejos de objetos metálicos a
menos de 0.5 m. Conector SMA accesible.

**Procedimiento.**
1. Calibrar SOL **en el plano del conector del arreglo** (no en el otro extremo del cable).
2. Barrido de 2200 a 2700 MHz, 401 puntos, formato Touchstone `.s1p`.
3. Para cada uno de los **20 estados** de DOC-06: fijar el estado, esperar 100 ms, capturar.
4. Repetir la serie completa **3 veces**, desconectando y reconectando en cada repetición, para
   estimar la repetibilidad del conector.
5. Calcular, por estado y por repetición, el peor valor de `|S11|` dentro de 2400–2483.5 MHz.

**Tamaño de muestra.** 20 estados × 3 repeticiones = **60 barridos**.

**Criterio.** `|S11| ≤ −10 dB` en toda la banda, en los 20 estados. Se declara cumplido solo si el
peor valor es **≤ −13 dB**, aplicando la banda de guarda de `N-03` §4.

**Datos.** `mediciones/AAAA-MM-s11/` con los `.s1p` crudos, el archivo de calibración usado y una
tabla resumen por estado.

**Si falla.** Orden de intervención: (1) ajustar `L_a`; (2) recalcular la red de adaptación
`DV-07`; (3) si un estado puntual es el único que falla, evaluar excluirlo del libro; (4) solo
entonces red conmutada (plan B de DEC-07).

---

## 5. T-03 — Patrones en azimut y relación delante/detrás (A2)

**Equipo.** Plataforma giratoria con marca de cero y paso de 5°; TX comercial fijo (router o
hotspot) a 1 m del eje; ESP32 registrando RSSI por paquete y MAC; cinta métrica y nivel.

**Montaje.** TX y arreglo a la misma altura (`h = 1.2 m`, `DV-06`); eje de giro alineado con el
centro del arreglo; distancia 1 m; nada metálico en el círculo de giro.

**Procedimiento.**
1. Fijar un estado del libro de códigos.
2. Girar de 0° a 355° en pasos de 5°: en cada punto, dejar estabilizar 2 s y capturar **30
   paquetes** del TX de referencia.
3. Registrar media y desviación estándar por punto.
4. Repetir para `K0`, `KS1`–`KS6`, `KW1`, `KN1` y `KX1` (**10 estados**).
5. Repetir la vuelta de `K0` al final, para detectar deriva del enlace.

**Tamaño de muestra.** 10 estados × 72 puntos × 30 paquetes = **21 600 paquetes**, más la vuelta de
control.

**Métricas.** `M-02` (patrón normalizado) y `M-03` (relación delante/detrás por sector).

**Criterio.**
- `A2`: relación delante/detrás ≥ 10 dB **en cada uno de los seis sectores**; se declara cumplido
  con ≥ 13 dB.
- Coherencia direccional: el máximo de cada `KS*` cae dentro de **±15°** de la dirección esperada
  de DOC-06 §5.
- Simetría: la dispersión entre los seis sectores del mismo bloque no supera 3 dB; si la supera, hay
  una asimetría física que se investiga antes de seguir.

**Datos.** `mediciones/AAAA-MM-patrones/`, un CSV por estado y por vuelta, más las figuras.

**Si falla.** Compuerta 1 de `DOC-08`: primero longitud de parásitos y diámetro de plano (dos
iteraciones de ajuste, sin cambiar de topología). Recién después, la falda.

---

## 6. T-04 — SIR y nulos (A3, DR-05)

**Equipo.** Dos TX comerciales distintos identificados por MAC (por ejemplo el router de la sala y
un hotspot de teléfono), separados angularmente; ESP32.

**Montaje.** TX deseado en 0°, interferente en 90°, 120° y 180° (tres configuraciones). Ambos a 1 m.

**Procedimiento.**
1. Con el estado `K0`, medir RSSI de cada MAC durante 60 s (referencia omnidireccional).
2. Barrer los seis estados `KS*`: en cada uno, medir RSSI de cada MAC durante 30 s.
3. Calcular `SIR = RSSI_deseado − RSSI_interferente` por estado y la mejora contra `K0` (`M-04`).
4. Repetir el barrido para el bloque `KN*` y calcular la profundidad de nulo hacia el interferente
   (`M-05`).
5. Repetir toda la serie en **3 sesiones de días distintos**, para separar el efecto del entorno.

**Tamaño de muestra.** 6 estados × 3 configuraciones × 3 sesiones × 30 paquetes = **1 620 paquetes**
por bloque.

**Criterio.**
- `A3`: mejora de SIR ≥ 10 dB respecto de `K0`, declarada cumplida con ≥ 13 dB.
- `DR-05`: profundidad de nulo ≥ 10 dB con el haz apuntando al deseado, declarada con ≥ 13 dB.
- Se reporta la dispersión entre sesiones; si la mediana se aparta de la media, se reportan ambas.

**Datos.** `mediciones/AAAA-MM-sir/` con un CSV por sesión, configuracion y estado.

**Si falla.** Compuerta 2 de `DOC-08`: si `A3` no supera 6 dB, se evalúa la extensión con varactores.
Si está entre 6 y 13 dB, se reporta el valor medido: **un resultado honesto por debajo de la meta es
mejor que una meta ajustada al resultado**.

---

## 7. T-05 — Tiempo de conmutación (A4)

Dos métodos, porque miden cosas distintas y hacen falta los dos.

### Método A — tiempo eléctrico de la orden (obligatorio)

**Equipo.** Osciloscopio de 2 canales, ≥ 100 MHz; pin de monitoreo GPIO33 (DOC-03 §5.1).

**Procedimiento.** Alternar `KS1` ↔ `KS4` a 1 kHz; capturar 100 transiciones de subida y 100 de
bajada; medir el tiempo entre flancos de la orden.

### Método B — tiempo de establecimiento de la RF (obligatorio si hay instrumental)

**Equipo.** Detector de diodo + osciloscopio, con una antena pequeña frente a un parásito; o el
propio receptor con marca temporal por paquete.

**Procedimiento.** Conmutar a 100 Hz y capturar la envolvente durante la transición; medir el tiempo
hasta que la envolvente se estabiliza en ±1 dB (`M-06`).

**Tamaño de muestra.** 100 transiciones de encendido y 100 de apagado por método.

**Criterio.** `t_sw < 1 ms` extremo a extremo, con **el peor de los dos métodos y la peor de las dos
transiciones**.

**Datos.** `mediciones/AAAA-MM-conmutacion/` con las capturas del osciloscopio y una tabla de
percentiles (p50, p95, máximo).

**Si falla.** Improbable según `DOC-05` §6. Si ocurre, el sospechoso es la red de polarización
(`C_bypass` demasiado grande o choque saturado), no el diodo.

---

## 8. T-06 — Detección de movimiento (A5)

**Equipo.** Sistema en modo sensado; una persona; cinta para marcar distancias; cronómetro; guion de
ensayos escrito de antemano.

**Procedimiento.**
1. Marcar seis zonas en el azimut, una por sector, a distancias de 1, 2 y 3 m.
2. Elegir el ensayo por sorteo (generado antes, no en el momento) y anotarlo **solo en la hoja que el
   operador no ve**: el operador no conoce el sector real.
3. La persona camina dentro de la zona elegida durante 15 s.
4. El sistema, con ventana `W = 10 s`, reporta el sector de máxima actividad (`M-07`).
5. Registrar acierto/error y distancia real.
6. Repetir hasta **10 ensayos por sector** (60 ensayos totales).

**Criterio.**
- `A5`: ≥ 8 de 10 aciertos por sector.
- Se publica la **matriz de confusión 6×6**, no solo la tasa global: con 10 ensayos por sector, la
  tasa global esconde los sectores que fallan siempre.

**Datos.** `mediciones/AAAA-MM-deteccion/` con la hoja de sorteo, la hoja de resultados y los
registros del sistema.

**Honestidad estadística.** Diez ensayos distinguen un sistema que funciona de uno que no, pero no
distinguen 70 % de 95 %. Por eso la métrica que va a la propuesta es la matriz completa y el rango de
distancias, no un porcentaje único.

**Si falla.** Antes de cambiar nada, verificar que el nulo hacia el iluminador esté en la dirección
correcta: la mayoría de los fallos de detección son fallos de supresión del trayecto directo.

---

## 9. T-07 — Interfaz y visualización

**Procedimiento.**
1. Cronometrar el tiempo entre actualizaciones del panel en modo operación (6 estados, 2 paquetes
   por estado): ¿≤ 1 s?
2. Verificar que el panel muestra modo, estado actual, SIR por par y actividad por sector.
3. Verificar la correspondencia LED ↔ estado para **los 20 estados** de DOC-06, uno por uno:
   los LEDs encendidos tienen que ser exactamente los `Pn` en conducción.

**Criterio.** Refresco ≤ 1 s (`DR-10`); 20/20 correspondencias correctas (`DR-17`).

**Datos.** `mediciones/AAAA-MM-interfaz/` con el video o capturas y la tabla de verificación.

---

## 10. T-08 — Auditoría de costo (DR-11)

**Procedimiento.** Sumar `gestion/BOM.md` con precios fechados y cotizaciones adjuntas. Separar en
dos columnas: **sistema entregado** (antena, control, receptor, alimentación, mecánica) y
**instrumentos de desarrollo** (VNA, plataforma giratoria si se compró).

**Criterio.** Columna «sistema entregado» < US$1500. Si la respuesta a `P2` indica que los
instrumentos de desarrollo cuentan, la suma total también tiene que quedar por debajo.

---

## 11. T-09 — Montaje, seguridad y rearmado

**Procedimiento.**
1. Desarmar el sistema por completo (sin instrucciones), cronometrar.
2. Rearmar siguiendo el instructivo, cronometrar. Repetir **3 veces** con personas distintas si es
   posible.
3. Contar los **tipos** de componente distintos (no las unidades).
4. Inspección de seguridad: tensión máxima presente, partes cortantes, estabilidad del soporte.

**Criterio.** Armado inicial ≤ 30 min; rearmado ≤ 10 min; ≤ 25 tipos de componente; ninguna tensión
> 5 V CC accesible.

**Datos.** `mediciones/AAAA-MM-montaje/` con los tiempos y la lista de tipos de componente.

---

## 12. T-10 — Explicabilidad

**Procedimiento.** Tres personas sin formación en RF. Demo de 60 s con los dos modos. Después, sin
ayuda, cada una explica qué hace el sistema y por qué funciona. Se registra en audio o por escrito.

**Criterio.** Las tres describen correctamente los dos modos y la idea de «elegir dirección con
interruptores». Si dos de tres mencionan el anillo de LEDs como lo que entendieron, el diseño de
visualización funcionó.

---

## 13. Registro y trazabilidad de los resultados

| Elemento | Regla |
| --- | --- |
| Nombre de campaña | `mediciones/AAAA-MM-asunto/` |
| Contenido mínimo | `crudo/`, `procesado/`, `figuras/`, `README.md` de campaña |
| `README.md` de campaña | escrito antes de medir: protocolo, equipo, condiciones, qué se espera |
| Datos crudos | no se editan a mano, nunca |
| Resultado | una fila por campaña en la tabla de estado de este documento |
| Figura para la propuesta | regenerable por comando desde `crudo/` |

### Tabla de estado de la verificación

| Protocolo | `A#` | Estado | Campaña | Resultado |
| --- | --- | --- | --- | --- |
| T-01 | — | no ejecutado | — | — |
| T-02 | A1 | no ejecutado | — | — |
| T-03 | A2 | no ejecutado | — | — |
| T-04 | A3 | no ejecutado | — | — |
| T-05 | A4 | no ejecutado | — | — |
| T-06 | A5 | no ejecutado | — | — |
| T-07 | — | no ejecutado | — | — |
| T-08 | — | no ejecutado | — | — |
| T-09 | — | no ejecutado | — | — |
| T-10 | — | no ejecutado | — | — |

## 14. Orden de ejecución

El orden no es el de la numeración: está elegido para que un fallo temprano cueste menos.

```
v0 (sin diodos, puentes manuales)     v1 (con PIN)                 antes de enviar
├── T-02 parcial  (A1, 7 estados)     ├── T-02 completo (20)       ├── T-08 costo
├── T-03 parcial  (A2, 3 estados)     ├── T-03 completo (10)       ├── T-10 explicabilidad
├── T-01          (R1)                ├── T-04 (A3, nulos)         └── revisión final de formato
└── seguridad de montaje (T-09)       ├── T-05 (A4)
                                      ├── T-06 (A5)
                                      ├── T-07 interfaz
                                      └── T-09 completo
```

Si `A2` falla en v0, no se suelda un solo PIN: se corrige geometría primero. Ese es el sentido de
medir con puentes de alambre.
