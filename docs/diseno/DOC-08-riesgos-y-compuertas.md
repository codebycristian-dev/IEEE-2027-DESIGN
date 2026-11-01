# DOC-08 — Riesgos y compuertas de decisión

| Código | DOC-08 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-02 v2.0 §6.4 y §7.2 |
| Tipo | Registro de riesgos |
| Estado | Vigente |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Convierte los riesgos cualitativos de DOC-02 §6.4 en un registro con disparador, mitigación y compuerta. Agrega los riesgos de verificación, cronograma y logística. |

## 1. Objeto

Un riesgo sin **disparador** y sin **acción** es una lista de miedos. Este registro fija, para cada
riesgo: cómo se detecta (disparador), qué se hace (mitigación) y en qué fecha se decide (compuerta).

## 2. Escalas

| Probabilidad | Valor | Impacto | Valor |
| --- | --- | --- | --- |
| muy baja | 1 | cosmético | 1 |
| baja | 2 | retraso de días | 2 |
| media | 3 | incumple un `A#` | 3 |
| alta | 4 | incumple el plazo del 31-dic | 4 |
| muy alta | 5 | pérdida del proyecto | 5 |

Nivel = P × I. **Tolerable ≤ 4 · requiere plan 5–9 · crítico ≥ 10.**

## 3. Registro

| `RSK` | Riesgo | P | I | Nivel | Disparador | Mitigación | Compuerta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RSK-01 | El plano de tierra finito inclina el haz y la relación delante/detrás no llega a 10 dB | 3 | 3 | 9 | `T-03` en v0 da `F/B` < 10 dB en el mejor sector | ajustar `DV-02` y `DV-04` (dos iteraciones); después, falda de 20 mm en el borde | G1 |
| RSK-02 | Las líneas de polarización acoplan y deforman el patrón | 3 | 3 | 9 | el patrón cambia al conectar/desconectar las líneas | reglas de layout de DOC-05 §7; medir con y sin líneas | G1 |
| RSK-03 | Un estado del libro no cumple la máscara de `A1` | 3 | 3 | 9 | `T-02` muestra algún estado por encima de −10 dB | recalcular `DV-07`; si persiste, excluir el estado del libro y documentar | G2 |
| RSK-04 | El choque de RF autorresuena dentro de banda y la línea se vuelve antena | 2 | 4 | 8 | `|Z|` medido del choque < 300 Ω a 2.44 GHz | dos inductores en serie; cambiar encapsulado; medir siempre | G2 |
| RSK-05 | Asimetría de fabricación: los seis sectores no son equivalentes | 3 | 2 | 6 | dispersión entre sectores > 3 dB en `T-03` | tolerancias de DOC-04 §6; recalcular el promedio de la red de adaptación | G1 |
| RSK-06 | El PIN corre la resonancia del parásito y pierde contraste entre estados | 3 | 3 | 9 | la diferencia entre «puente de alambre» y «PIN» en v0→v1 supera 2 dB | acortar el elemento para compensar; cambiar de PIN a uno de menor inductancia de lazo | G2 |
| RSK-07 | La mejora de SIR no alcanza 10 dB (nulos poco profundos) | 3 | 3 | 9 | `A3` < 10 dB | si < 6 dB: extensión con varactores (compuerta 2 de DOC-02 §7.2); si 6–10 dB: reportar el valor medido | G2 |
| RSK-08 | El cronograma no llega: compra tardía de componentes | 3 | 4 | 12 | el kit mínimo no está pedido al 24-oct-2026 | comprar de dos proveedores; aceptar sustitutos documentados para pasivos | G0 |
| RSK-09 | El montaje no sobrevive el transporte a Kioto | 2 | 3 | 6 | `T-09` da rearmado > 10 min o hay piezas sueltas | diseño de varillas desmontables con topes; caja rígida; repuesto de cada varilla | G3 |
| RSK-10 | El multitrayecto del aula domina y enmascara el efecto de la antena | 4 | 2 | 8 | dispersión entre sesiones > 3 dB en `T-04` | medir en tres posiciones y tres días; reportar mediana y dispersión | G2 |
| RSK-11 | El RSSI del ESP32 no alcanza para detectar movimiento | 3 | 3 | 9 | `A5` < 8/10 con `M-07` | pasar a CSI con `ESP32-CSI-Tool` [20] sin cambiar la antena | G3 |
| RSK-12 | Las preguntas `P1`–`P3` quedan sin respuesta y afectan el cumplimiento | 3 | 3 | 9 | sin respuesta al 31-oct-2026 | documentar el envío y la fecha; diseñar para el caso conservador (instrumentos incluidos en el costo) | G0 |

### Riesgos aceptados sin mitigación

Se aceptan explícitamente, y así se declara en la propuesta:

| Riesgo aceptado | Motivo |
| --- | --- |
| Resolución de nulos limitada por la geometría (múltiplos de 30–60°) | es consecuencia del control binario elegido (DEC-02); la alternativa son varactores, que la restricción del mentor excluye de la base |
| Polarización fija vertical | un segundo anillo ortogonal duplica la electrónica; no lo piden las bases |
| Ancho de haz de 60–100° | con seis elementos no hay más resolución; se compensa con seis sectores solapados |

Declarar esto **suma** credibilidad: un jurado que ve límites reconocidos confía más en los números
que sí se reportan.

## 4. Compuertas de decisión

Cada compuerta es una fecha con un criterio de paso y una acción si no se cumple. Sin compuertas, un
proyecto estudiantil descubre en diciembre que no llega.

| Compuerta | Fecha | Criterio de paso | Si no se cumple |
| --- | --- | --- | --- |
| **G0** | 2026-10-24 | kit mínimo pedido; `P1`–`P3` enviadas; `A1`–`A5` ratificados con el mentor | se compra de proveedor alternativo y se sigue con los criterios vigentes documentando el silencio |
| **G1** | 2026-11-14 | v0 construido con puentes manuales; `F/B` ≥ 8 dB en el mejor sector | retroalimentar la etapa B de DOC-04 con el dato medido; no se suelda ningún PIN |
| **G2** | 2026-12-05 | v1 con PIN; `A1` y `A2` cumplidos; `A3` medido | si `A3` < 6 dB, evaluar varactores; si `A1` no cierra, red conmutada (DEC-07 plan B) |
| **G3** | 2026-12-14 | demo de ambos modos; `A4` y `A5` medidos; figuras listas | si `A5` falla, cambiar a CSI y repetir; si `A4` falla, revisar la red de polarización |
| **G4** | 2026-12-22 | propuesta redactada con resultados medidos y BOM cerrado | rotular como expectativa lo que no se midió, declarando el plan; nunca inventar un número |
| **G5** | 2026-12-24 | PDF enviado, con acuse | margen de 7 días sobre el plazo del 31-dic |

Regla de las compuertas: **una compuerta no se saltea, se documenta.** Si G2 pasa sin `A3` medido, el
riesgo deja de ser riesgo y pasa a ser deuda, y la propuesta lo dice.

## 5. Escalamiento

| Situación | Acción |
| --- | --- |
| Un riesgo crítico se materializa | se detiene la construcción, se convoca al mentor con el dato medido, se decide entre las opciones de la compuerta |
| Dos compuertas consecutivas fallan | se recorta el alcance de la demo (menos estados, menos modos) antes que enviar una propuesta con resultados que no existen |
| Cambio de requisito del mentor u organizadores | se actualiza `N-04`, se revisan las compuertas afectadas, no se reinterpreta en silencio |
| Falla el cumplimiento de `R1` | se detiene todo lo demás: es descalificación, no pérdida de puntos |

## 6. Riesgo residual aceptado al cierre de este documento

El riesgo dominante del proyecto a la fecha es **RSK-08 (cronograma de compras)**, con nivel 12. Nada
del diseño depende de una decisión técnica pendiente: depende de que los componentes estén sobre la
mesa antes de noviembre. Es el único riesgo que hoy tiene plazo vencido en el corto plazo, y el
trabajo de esta semana es la compra, no más documentación.
