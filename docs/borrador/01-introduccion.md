# 01 — Introducción

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, sin redacción |
| Fuente principal | `docs/teoria/02-estado-del-arte.md` §9 (vacío) y `DOC-03` §1 (objeto y alcance) |
| Apoyo | `DOC-09` §2 (delta), `N-04` §2 (`R1`–`R9`) |
| Ubicación y fecha | Página 1; se redacta el 2026-12-22, después de la compuerta G4 |

## Objetivo del capítulo

Presentar el problema del concurso y la respuesta del equipo en menos de una página. Dejar explícito,
antes de cualquier detalle, qué se propone construir y qué no.

## Qué va

- **Encabezado.** Título, equipo, integrantes, mentor IEEE AP-S e institución, en cuatro líneas como
  máximo.
- **Resumen de 8 líneas.** Qué es el sistema (ESPAR de 7 elementos, 2400–2483.5 MHz, 6 diodos PIN,
  ESP32), qué modos tiene y qué se mide para demostrarlo (`DOC-03` §1–§2 y §6).
- **El problema.** Las bases piden una antena receptora reconfigurable para ISAC: recepción estricta
  (`R1`) e iluminadores comerciales sin modificar (`R2`). El receptor es un ESP32 que no controla al
  transmisor, así que la única variable disponible es la antena (`N-04` §2).
- **La propuesta en una frase.** Controlar el patrón sin controlar la RF: seis parásitos conmutados a
  tierra mueven el haz en azimut con seis líneas digitales (`DOC-03` DEC-01).
- **El vacío que se ocupa.** Los cuatro puntos de `N-02` §9, uno por línea: el ESPAR usado como
  receptor y no como radiador; el nulo hacia el iluminador como mecanismo de sensado; la alternancia
  de estados entre paquetes de Wi-Fi sobre un receptor comercial; la trazabilidad completa.
- **Objetivo y alcance.** Cobertura de 360° con 6 sectores (`DR-03`), explicabilidad en 60 s (`DR-16`)
  y reproducibilidad en aula (`R8`). Fuera de alcance: transmisión (`R1`), control en elevación,
  reconfiguración de polarización (`DOC-03` §8).

## Qué no va

- La teoría del acoplamiento mutuo y de la carga reactiva: vive en `docs/teoria/01-fundamentos-espar.md`
  y se cita, no se desarrolla.
- La comparación ESPAR / RIS / píxeles: la decisión está cerrada en `DOC-01` y va una frase con la
  referencia, no la justificación completa.
- Resultados, mediciones o cifras de desempeño: eso es el capítulo 05, y solo si hay campaña.
- Cronograma, compuertas y riesgos: son gestión interna (`gestion/cronograma.md`).

## Extensión prevista

Página 1, **≈ 32 de las 44 líneas**: encabezado 4, resumen 8, problema 6, propuesta 4, vacío 6,
alcance 4. La figura de arquitectura ocupa el resto y pertenece al capítulo 03.

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada `R#` citado existe en `N-04` §2 y no se parafrasea.
- [ ] El vacío se apoya en `N-02` §9, no en una impresión del equipo.
- [ ] No aparece ninguna cifra de desempeño: ni ganancia, ni `SIR`, ni relación delante/detrás.
- [ ] El alcance declarado coincide con `DOC-03` §8.
- [ ] Toda afirmación tiene un ID detrás (`R#`, `DR-##`, `DEC-##`) o una referencia de `N-02` §11.
