# 06 — Discusión

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, sin redacción |
| Fuente principal | `DOC-08` §3 (riesgos aceptados) y §4 (compuertas) |
| Apoyo | `gestion/BOM.md` (costo), `DOC-03` §8 (fuera de alcance), `DOC-09` §4 (qué se sostiene) |
| Ubicación y fecha | Página 4 (cierre del documento); se redacta el 2026-12-22, después de G4 |

## Objetivo del capítulo

Cerrar el documento diciendo qué se logró, qué no y por qué, y qué necesita otro grupo para repetirlo.
Un límite reconocido suma credibilidad; un límite escondido la resta entera.

## Qué va

- **Qué se logró, en tres bullets con respaldo medido.** Cobertura de 360° con seis sectores (`DR-03`),
  mejora de `SIR` contra el estado omnidireccional (`A3`) y un sistema replicable con BOM, tolerancias
  y protocolos (`R8`, `DR-12`) (`DOC-09` §4).
- **Qué no se logró y por qué.** Sin justificaciones defensivas: si `A3` quedó en 8 dB se dice 8 dB y
  se explica que el nulo discreto del control binario es la causa (`DEC-02`, `DOC-07` §6).
- **Tres límites aceptados explícitamente.** Resolución de nulos limitada por la geometría (múltiplos
  de 30–60°), polarización fija vertical y ancho de haz de 60–100° (`DOC-08` §3, riesgos aceptados).
- **Replicabilidad en cuatro números.** ≤ 25 tipos de componente, sin PCB multicapa, montaje desde cero
  ≤ 30 min y rearmado ≤ 10 min (`DR-12`, `DR-14`, `DOC-07` §11).
- **Costo en dos bloques.** Sistema entregado e instrumentos de desarrollo separados, con el margen
  contra el tope de US$1500 y la aclaración de que la separación depende de `P2` (`gestion/BOM.md`).
- **Explicabilidad.** El anillo de seis LEDs muestra el estado de la antena sin manual: es criterio de
  evaluación (`C4.1`, `DR-16`) y se verifica con `T-10` (`DOC-03` DEC-14, `DOC-07` §12).
- **Trabajo futuro, tres bullets con condición.** Varactores solo si `A3` no alcanza (compuerta 2); CSI
  con `ESP32-CSI-Tool` [20] si el RSSI no alcanza para `A5`, sin cambiar la antena; falda de plano de
  tierra como mitigación de elevación (`DOC-08` §4, `DOC-03` §8).
- **Referencias.** 6 a 10, solo las efectivamente leídas, numeradas como en `N-02` §11.

## Qué no va

- El registro completo de 12 riesgos con disparador y compuerta: es gestión interna. Se mencionan dos
  como mucho, y solo si explican un resultado.
- El cronograma y las compuertas G0–G5.
- La comparación con RIS y antenas de píxeles más allá de una frase de cierre.
- Promesas de trabajo futuro sin condición: cada bullet lleva su disparador.
- Agradecimientos extensos: una línea para el mentor y el capítulo IEEE AP-S Colombia.

## Extensión prevista

Página 4, **≈ 18 de las 42 líneas** disponibles. Distribución: qué se logró 4, qué no 4, límites
aceptados 4, replicabilidad y costo 3, trabajo futuro 3. Las referencias van al pie y no cuentan.

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada límite aceptado está en `DOC-08` §3 y se declara como aceptado, no como disculpa.
- [ ] Los números de replicabilidad coinciden con `DR-12` y `DR-14`.
- [ ] El costo citado coincide con `gestion/BOM.md` y su fecha de referencia está declarada.
- [ ] Cada bullet de trabajo futuro tiene su condición de activación.
- [ ] No se promete nada que dependa de una compuerta que ya pasó sin cumplirse.
- [ ] Toda afirmación tiene un ID detrás (`DR-##`, `A#`, `T-##`) o una referencia de `N-02` §11.
