# Cronograma — plan fechado hasta el envío

| | |
| --- | --- |
| Artefacto | Cronograma único del proyecto |
| Versión / fecha | 1.0 — 2026-10-14 |
| Estado | Planificación. Todos los hitos en `pendiente` |
| Fuentes fusionadas | DOC-02 §8.2 (10 pasos), DOC-04 §7 (etapas A–D), DOC-07 §14 (orden de ensayos), DOC-08 §4 (compuertas G0–G5) |

## Convención de fechas

Este archivo **no inventa fechas**. La columna `fecha` usa tres formas, y cada una declara su origen:

| Forma | Significado |
| --- | --- |
| `2026-MM-DD` | fecha fijada por el documento fuente (paso de DOC-02 §8.2 o compuerta de DOC-08 §4) |
| `ventana AAAA-MM-DD → AAAA-MM-DD` | el documento fuente fija el orden pero no la fecha; la ventana se deriva de las compuertas que la encierran |
| `por fijar` | no hay base en el repositorio para asignar una fecha |

Las etapas A, B y C de `DOC-04` §7 no tienen fecha en su documento de origen; solo la etapa D tiene
fecha objetivo (2026-11-14, paso 6). Su ventana se deriva de ahí y de la compuerta G0.

## Tabla única

| Fecha | Hito | Entregable | Depende de | Compuerta | Estado |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Ratificar la decisión D-06 en reunión de equipo (paso 1) | Acta de reunión con la fecha registrada | — | — | pendiente |
| 2026-10-17 | Enviar `P1`–`P3` a los organizadores (paso 2) | Correo enviado y copia en `gestion/preguntas-organizadores.md` | — | G0 | pendiente |
| 2026-10-24 | Ratificar `A1`–`A5` con el mentor (paso 3) | Criterios ratificados y registrados en `N-04` §4 | paso 1 | G0 | pendiente |
| 2026-10-24 | Cotizar y comprar el kit mínimo (paso 4) | `gestion/BOM.md` con las filas del bloque A en estado `cotizado` | paso 3; `DOC-05` §10 | G0 | pendiente |
| 2026-10-31 | Contactar al capítulo IEEE AP-S Colombia (paso 5) | Registro del contacto y recomendaciones de logística | paso 2 | — | pendiente |
| ventana 2026-10-25 → 2026-11-13 | Etapa A — resonancia del elemento activo (`DOC-04` §7) | `L_a` que resuena en 2441.75 MHz ± 20 MHz; 4 corridas NEC2 | kit mínimo; paso 4 | G1 | pendiente |
| ventana 2026-10-25 → 2026-11-13 | Etapa B — anillo y parásitos (`DOC-04` §7) | Celda `r` × `L_p` que maximiza `F/B` con HPBW ≤ 100°; 20 corridas | etapa A | G1 | pendiente |
| ventana 2026-10-25 → 2026-11-13 | Etapa C — plano de tierra (`DOC-04` §7) | `D_g` nominal definitivo; 3 corridas | etapa B | G1 | pendiente |
| 2026-11-14 | Prototipo v0 con puentes manuales (paso 6; etapa D de `DOC-04` §7) | v0 construido, geometría validada, `F/B` ≥ 8 dB en el mejor sector | etapas A–C; paso 4 | G1 | pendiente |
| ventana 2026-11-15 → 2026-12-04 | `T-02` parcial — `A1` con 7 estados (`DOC-07` §14) | `.s1p` crudos y tabla de peor `\|S11\|` por estado | v0 | G2 | pendiente |
| ventana 2026-11-15 → 2026-12-04 | `T-03` parcial — `A2` con 3 estados (`DOC-07` §14) | Patrones normalizados y `F/B` por sector | v0 | G2 | pendiente |
| ventana 2026-11-15 → 2026-12-04 | `T-01` — recepción pasiva estricta (`DOC-07` §3) | Registros del SDR y captura de configuración del firmware | v0 | G2 | pendiente |
| ventana 2026-11-15 → 2026-12-04 | Seguridad y montaje de v0 (`DOC-07` §14; `T-09` parcial) | Inspección de tensión, partes cortantes y estabilidad | v0 | G2 | pendiente |
| 2026-12-05 | Prototipo v1 con diodos PIN y verificación de `A1`–`A4` (paso 7) | v1 soldado; `A1` y `A2` cumplidos; `A3` medido | `T-02` y `T-03` parciales | G2 | pendiente |
| ventana 2026-12-05 → 2026-12-13 | `T-02` completo — `A1` con los 20 estados (`DOC-07` §4) | 60 barridos (20 estados × 3 repeticiones) | v1 | G3 | pendiente |
| ventana 2026-12-05 → 2026-12-13 | `T-03` completo — `A2` con 10 estados (`DOC-07` §5) | 21 600 paquetes y figuras de patrón | v1 | G3 | pendiente |
| ventana 2026-12-05 → 2026-12-13 | `T-04` — `SIR` y nulos, `A3` (`DOC-07` §6) | Mejora de `SIR` contra `K0` y profundidad de nulo por sesión | v1; `T-03` completo | G3 | pendiente |
| ventana 2026-12-05 → 2026-12-13 | `T-05` — tiempo de conmutación, `A4` (`DOC-07` §7) | 100 transiciones por método y por sentido; tabla de percentiles | v1 | G3 | pendiente |
| 2026-12-14 | Demostración mínima de ambos modos (paso 8; `T-06`, `A5`) | Matriz de confusión 6×6 y rango de distancias | `T-04` | G3 | pendiente |
| ventana 2026-12-14 → 2026-12-21 | `T-07` — interfaz y visualización (`DOC-07` §9) | Refresco medido y 20/20 correspondencias LED ↔ estado | v1 | G4 | pendiente |
| ventana 2026-12-14 → 2026-12-21 | `T-09` completo — montaje, seguridad y rearmado (`DOC-07` §11) | Tiempos de armado y rearmado; conteo de tipos de componente | v1 | G4 | pendiente |
| ventana 2026-12-14 → 2026-12-21 | Figuras para la propuesta (paso 8) | Figuras regenerables por comando desde `mediciones/*/crudo/` | `T-03`, `T-04` | G4 | pendiente |
| 2026-12-22 | Redactar la propuesta de 4 páginas y obtener la carta del mentor (paso 9) | `propuesta/propuesta-4-paginas.pdf` y `carta-mentor.pdf` firmada | figuras; `docs/borrador/00-mapa-propuesta-4-paginas.md` | G4 | pendiente |
| ventana 2026-12-22 → 2026-12-23 | `T-08` — auditoría de costo (`DOC-07` §10) | `gestion/BOM.md` cerrado con precios fechados y cotizaciones | paso 4; `P2` | G4 | pendiente |
| ventana 2026-12-22 → 2026-12-23 | `T-10` — explicabilidad (`DOC-07` §12) | Registro de las tres personas y su descripción de los dos modos | demo de ambos modos | G4 | pendiente |
| 2026-12-24 | Enviar la propuesta, 23:59 GMT−10 (paso 10) | Acuse de recibo de los organizadores | paso 9; `T-08`; `T-10` | G5 | pendiente |

## Compuertas de decisión

Reproducidas de `DOC-08` §4 para que este archivo se lea solo. **Una compuerta no se saltea, se
documenta.**

| Compuerta | Fecha | Criterio de paso | Si no se cumple |
| --- | --- | --- | --- |
| **G0** | 2026-10-24 | kit mínimo pedido; `P1`–`P3` enviadas; `A1`–`A5` ratificados con el mentor | se compra de proveedor alternativo y se sigue con los criterios vigentes documentando el silencio |
| **G1** | 2026-11-14 | v0 construido con puentes manuales; `F/B` ≥ 8 dB en el mejor sector | retroalimentar la etapa B con el dato medido; no se suelda ningún PIN |
| **G2** | 2026-12-05 | v1 con PIN; `A1` y `A2` cumplidos; `A3` medido | si `A3` < 6 dB, evaluar varactores; si `A1` no cierra, red conmutada (DEC-07 plan B) |
| **G3** | 2026-12-14 | demo de ambos modos; `A4` y `A5` medidos; figuras listas | si `A5` falla, cambiar a CSI y repetir; si `A4` falla, revisar la red de polarización |
| **G4** | 2026-12-22 | propuesta redactada con resultados medidos y BOM cerrado | rotular como expectativa lo que no se midió, declarando el plan; nunca inventar un número |
| **G5** | 2026-12-24 | PDF enviado, con acuse | margen de 7 días sobre el plazo del 31-dic |

## Ruta crítica

Tres hitos, si se atrasan, ponen en riesgo el envío. No son los más costosos: son los únicos que no
tienen holgura porque todo lo demás cuelga de ellos.

1. **Compra del kit mínimo — 2026-10-24 (G0).** Es el único hito cuyo atraso **no se puede recuperar
   después**, porque el resto de la cadena tiene fecha fija: sin componentes no hay v0 el 14-nov, y
   sin v0 no hay `A1` ni `A2` medidos. Es exactamente `RSK-08`, el riesgo de nivel más alto del
   registro (12). La mitigación ya está decidida: dos proveedores y sustitutos documentados para los
   pasivos. La fecha del 24-oct es además la que deja margen para un reenvío.
2. **v0 con `F/B` ≥ 8 dB — 2026-11-14 (G1).** Es el hito que decide si la geometría sirve. Si falla,
   se vuelve a la etapa B con el dato medido, y esa iteración consume días que hoy no están
   presupuestados. La regla de `DOC-07` §14 es explícita: si `A2` falla en v0, **no se suelda un solo
   PIN** hasta corregir geometría. Soldar antes de tiempo ahorra una semana en el mejor caso y cuesta
   el prototipo en el peor.
3. **v1 con `A1` y `A2` cumplidos y `A3` medido — 2026-12-05 (G2).** Es la última compuerta donde
   todavía se puede cambiar algo de fondo: después de G2 solo quedan nueve días hasta la demo y la
   propuesta ya tiene que escribirse con lo que haya. Un `A3` sin medir al 5-dic no se convierte en
   dato el 20-dic.

Los tres comparten una propiedad: **cada uno es la entrada del siguiente**. Por eso un atraso de una
semana en G0 no cuesta una semana: cuesta las tres compuertas. Los hitos posteriores a G3 (redacción,
`T-08`, `T-10`, envío) tienen holgura real, porque la propuesta se escribe sobre datos que ya existen.

## Nota de coherencia

El paso 7 de `DOC-02` §8.2 pide «verificar `A1`–`A4`» al 2026-12-05, pero `DOC-08` G3 y `DOC-07` §14
ubican `T-05` (`A4`) y `T-06` (`A5`) entre el 5 y el 14 de diciembre. La lectura adoptada acá es la de
`DOC-08`/`DOC-07`, que son los documentos vigentes: al 5-dic se cierra `A1`–`A3` y `A4` se mide antes
del 14-dic. La diferencia queda registrada, no corregida.
