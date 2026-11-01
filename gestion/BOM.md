# BOM — lista de materiales y costo acumulado

| | |
| --- | --- |
| Artefacto | Lista de materiales (`R7` → `DR-11`) |
| Versión / fecha | 1.0 — 2026-10-14 |
| Estado | **Estimación. Ningún precio está cotizado.** |
| Auditoría de costo | `T-08` de `DOC-07` §10, antes de enviar |
| Documentos que fijan cantidades | `DOC-03` §4–§5, `DOC-05` §2–§8 |

## Aviso sobre los precios

**Ningún precio de este documento está cotizado.** Las dos tablas de abajo son estimaciones de orden
de magnitud del equipo, con **fecha de referencia 2026-10-14**, y su única función es detectar si el
diseño entra en el tope de `R7` antes de gastar. No hay cotizaciones adjuntas, no hay números de
orden, no hay proveedor confirmado y ninguna fila tiene precio verificado.

Todas las filas llevan estado `estimado` por esa razón. Una fila pasa a `cotizado` solo cuando existe
una cotización con fecha y proveedor, y a `comprado` cuando existe el comprobante. La regla de
`gestion/README.md` aplica: **el costo se controla al comprar, con el precio real, no con el
estimado**. Este documento no reemplaza esa constancia.

El único precio con fuente en el repositorio es el del diodo PIN: US$0.56 por unidad suelta y US$0.31
por 100 unidades, según la referencia [27] de `N-02` §11 (consultada el 2026-10-13). Se toma el valor
unitario alto, que es el conservador para una compra de seis piezas.

## Criterio de separación en dos bloques

`R7` fija el tope de **US$1500 al sistema** que se presenta. `DR-11` agrega la condición de que los
**instrumentos de desarrollo se declaren aparte**. La pregunta `P2` a los organizadores
(`gestion/preguntas-organizadores.md`) todavía no tiene respuesta, así que se presupuesta el caso
conservador: se separan los bloques y al final se muestra el margen con las dos lecturas.

| Bloque | Qué incluye | Cuenta contra `R7` |
| --- | --- | --- |
| A — Sistema entregado | antena, electrónica de control, receptor, mecánica, consumibles del montaje | Sí, sin discusión |
| B — Instrumentos de desarrollo | VNA, plataforma giratoria, fuente, osciloscopio | Pendiente de `P2` |

## Bloque A — Sistema entregado

| Ítem | Cantidad | Referencia | Proveedor | Precio unitario | Subtotal | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| Diodo PIN SMP1345-079LF (SC-79) | 6 | DEC-02; [27] | DigiKey (referencia [27]) | US$0.56 | US$3.36 | estimado |
| Resistencia 220 Ω, 0603, 1 % | 6 | `R_limit`, DOC-05 §3 | proveedor por confirmar | US$0.05 | US$0.30 | estimado |
| Inductor 33 nH, 0603 | 6 | `L_choke`, DOC-05 §4 | proveedor por confirmar | US$0.20 | US$1.20 | estimado |
| Capacitor 470 pF, 0603, C0G | 6 | `C_bypass`, DOC-05 §5 | proveedor por confirmar | US$0.10 | US$0.60 | estimado |
| Resistencia 10 kΩ, 0603 | 6 | `R_pd`, DOC-05 §8 | proveedor por confirmar | US$0.03 | US$0.18 | estimado |
| Devkit ESP32 (módulo con USB) | 1 | DEC-12 | proveedor por confirmar | US$12.00 | US$12.00 | estimado |
| LED de bajo consumo | 6 | DEC-14 | proveedor por confirmar | US$0.08 | US$0.48 | estimado |
| Resistencia 1 kΩ, 0603 (LED) | 6 | DEC-14 | proveedor por confirmar | US$0.03 | US$0.18 | estimado |
| Conector SMA hembra a PCB, refuerzo mecánico | 1 | DOC-05 §7 regla 7 | proveedor por confirmar | US$2.50 | US$2.50 | estimado |
| Kit de red de adaptación: L 2–15 nH y C 0.5–5 pF, varios valores | 1 juego | `DV-07`, DEC-07 | proveedor por confirmar | US$4.00 | US$4.00 | estimado |
| Placa FR4 doble cara cobreada, Ø 150 mm | 2 | `DV-03`, DEC-10 | proveedor por confirmar | US$8.00 | US$16.00 | estimado |
| Varilla de latón Ø 3 mm, 1 m | 2 | `DV-05`, DEC-03 | ferretería local | US$6.00 | US$12.00 | estimado |
| Diodo PIN de repuesto | 4 | RSK-06 (reemplazo tras caracterizar) | DigiKey (referencia [27]) | US$0.56 | US$2.24 | estimado |
| Estaño para soldar | 1 | — | ferretería local | US$5.00 | US$5.00 | estimado |
| Cable AWG 22, rollo de 10 m | 1 | — | ferretería local | US$4.00 | US$4.00 | estimado |
| Cable Dupont 20 cm, 40 unidades | 1 | — | proveedor por confirmar | US$3.00 | US$3.00 | estimado |
| Caja de transporte rígida | 1 | RSK-09, DR-14 | ferretería local | US$15.00 | US$15.00 | estimado |
| **Subtotal bloque A** | | | | | **US$82.04** | estimado |

Notas del bloque A:

- Dos placas FR4 y dos varillas de 1 m cubren el prototipo **v0** (puentes de alambre) y el **v1**
  (con PIN). `RSK-09` pide repuesto de cada varilla antes del transporte a Kioto.
- El kit de red de adaptación no estaba en la lista original de `DOC-02`: lo exige DEC-07, que sin
  red fija deja `A1` fuera de alcance. Los valores finales de `DV-07` se calculan recién con `T-02`
  sobre v0, por eso se compra un surtido y no un valor.
- No se presupuesta fabricación de PCB: se hace en el laboratorio de la universidad y no tiene costo
  para el equipo. Si hubiera que encargarla, es un ítem nuevo y no una reinterpretación de este.
- El precio del diodo es el de compra unitaria (US$0.56). Comprar por cantidad lo baja a US$0.31, una
diferencia del orden de US$1.50 en seis piezas: no cambia ninguna decisión y por eso no se estima.

## Bloque B — Instrumentos de desarrollo

| Ítem | Cantidad | Referencia | Proveedor | Precio unitario | Subtotal | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| Analizador vectorial LiteVNA 64 (o NanoVNA-H4) | 1 | T-02, T-03 | proveedor por confirmar | US$120.00 | US$120.00 | estimado |
| Kit de calibración SOL, SMA | 1 | T-02 paso 1 | proveedor por confirmar | US$15.00 | US$15.00 | estimado |
| Plataforma giratoria con escala angular y paso de 5° | 1 | T-03 | proveedor por confirmar | US$60.00 | US$60.00 | estimado |
| Fuente de alimentación de banco, 0–30 V / 3 A | 1 | DOC-05 §9 | proveedor por confirmar | US$70.00 | US$70.00 | estimado |
| Osciloscopio ≥ 100 MHz, 2 canales | 1 | T-05 método A | préstamo de la universidad | US$0.00 | US$0.00 | estimado |
| Cables y accesorios de RF: 2 × SMA-SMA 50 cm, carga de 50 Ω, atenuadores | 1 juego | T-02, T-03 | proveedor por confirmar | US$30.00 | US$30.00 | estimado |
| Multímetro de banco | 1 | DOC-05 §9 | proveedor por confirmar | US$25.00 | US$25.00 | estimado |
| **Subtotal bloque B** | | | | | **US$320.00** | estimado |

Notas del bloque B:

- El osciloscopio se presupuesta en US$0.00 porque se usa prestado. **Si hay que comprarlo, suma del
  orden de US$300** y el total del proyecto pasa de US$700; sigue por debajo de US$1500, así que no
  cambia la decisión, pero se declara.
- La plataforma giratoria es la que `T-03` exige con paso de 5° y marca de cero. Una base improvisada
  sin escala no sirve para el protocolo: el dato no sería comparable entre campañas.
- Los instrumentos no se compran si `P2` confirma que quedan fuera del tope y el laboratorio los
  presta. La prioridad de compra es: VNA y kit SOL primero (`T-02` bloquea `A1`), plataforma después
  (`T-03` bloquea `A2`).

## Cierre de costo

| Concepto | Monto |
| --- | --- |
| Subtotal bloque A — sistema entregado | **US$82.04** |
| Subtotal bloque B — instrumentos de desarrollo | US$320.00 |
| Total general (A + B) | US$402.04 |
| Tope de `R7` | US$1500.00 |
| **Margen contra US$1500 — solo sistema entregado (criterio vigente de `DR-11`)** | **US$1417.96** |
| Margen contra US$1500 — si `P2` incluye los instrumentos | US$1097.96 |

Lectura de los números:

1. El sistema entregado ocupa el **5.5 % del tope**. El costo no es una restricción activa de este
   diseño: la restricción activa es el tiempo (`RSK-08`).
2. La estimación del bloque A (US$82.04) cae dentro del rango de orden de magnitud que `DOC-02` tabla
   6 asignaba a «antena + control» para el ESPAR (US$80–150). Es una verificación de coherencia entre
   dos documentos, no una confirmación de precio.
3. Incluso en el caso conservador de `P2` —instrumentos dentro del tope— queda un margen de
   US$1097.96. Ninguna de las dos lecturas pone en riesgo `DR-11`.

## Riesgo asociado y compuerta

Este documento no cierra `DR-11`: lo deja estimado. El riesgo que lo domina no es el monto sino la
**fecha**. `RSK-08` (nivel 12, el más alto del registro de `DOC-08` §3) tiene como disparador que el
kit mínimo **no esté pedido al 2026-10-24**, y su mitigación es comprar en dos proveedores y aceptar
sustitutos documentados para los pasivos.

Esa fecha es la compuerta **G0** de `DOC-08` §4 (2026-10-24), que exige tres cosas el mismo día: kit
mínimo pedido, `P1`–`P3` enviadas y `A1`–`A5` ratificados con el mentor. Si G0 no se cumple, se compra
de proveedor alternativo y se sigue con los criterios vigentes documentando el silencio.

Consecuencia operativa: el BOM se cierra en **dos pasos**, no en uno. El 2026-10-24 se cierran las
filas del bloque A con precio cotizado; las filas del bloque B se cierran después de la respuesta a
`P2`. Mientras tanto, toda fila de este documento se lee como `estimado`.
