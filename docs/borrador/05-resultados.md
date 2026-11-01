# 05 — Resultados

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, **sin datos: ninguna campaña ejecutada** |
| Fuente principal | `docs/diseno/DOC-07-plan-de-verificacion.md` §13 (tabla de estado de la verificación) |
| Apoyo | `DOC-07` §4–§8 (criterios y muestras), `N-03` §4 (incertidumbre), `mediciones/` |
| Ubicación y fecha | Página 4 (primera mitad); se redacta el 2026-12-22, después de la compuerta G4 |

## Objetivo del capítulo

Reportar lo medido con su tamaño de muestra y su incertidumbre, y declarar sin adornos lo que quedó sin
medir. Es el capítulo que un jurado lee primero para decidir si el resto es creíble.

## Qué va

- **Una tabla de cinco filas**, copiada de `DOC-07` §13 y no de memoria: criterio, meta, medido, banda
  de guarda y campaña, una fila por `A1`–`A5`. Hoy las cinco dicen **pendiente**: `A1`–`A3` se miden
  antes de G2 y `A4`–`A5` antes de G3.
- **Cada fila con su muestra.** Un número sin tamaño de muestra no es un resultado: 60 barridos para
  `A1`, 21 600 paquetes para `A2`, tres sesiones de días distintos para `A3`, 100 transiciones por
  sentido y por método para `A4`, 60 ensayos ciegos para `A5` (`DOC-07` §4–§8).
- **La incertidumbre, declarada una vez.** El presupuesto es de 3–4 dB con término dominante
  identificado; por eso los criterios de 10 dB se declaran cumplidos recién a 13 dB (`N-03` §4).
- **La dispersión, no solo la media.** Para `A2`, entre los seis sectores del mismo bloque: si supera
  3 dB hay una asimetría física que se investiga. Para `A3`, entre sesiones (`DOC-07` §5–§6).
- **La matriz de confusión de `A5` completa**, 6×6, y no un porcentaje global (`DOC-07` §8).
- **Figura.** Meta contra medido, o el patrón medido: una sola figura en esta página, regenerable por
  comando desde `crudo/` (`DOC-07` §13).

## Qué no va

- Datos que no estén en `mediciones/`. Si un valor no está, la fila dice «pendiente» y el capítulo
  sigue: no se completa con la simulación NEC2, ni con el dato de otro trabajo, ni con un «se espera».
- La justificación del diseño: está en el capítulo 03. Acá solo se reporta.
- Las curvas completas de `S11` de los 20 estados, los 72 puntos de cada patrón y las capturas de
  osciloscopio: van las figuras de síntesis y el crudo queda en el repositorio.
- La lista de lo que falló y por qué: eso es el capítulo 06. Acá se reporta el número, incluso el que no
  alcanza.

## Extensión prevista

Página 4, **≈ 24 de las 42 líneas** disponibles (las otras 18 son del capítulo 06). Distribución: tabla
14, muestras e incertidumbre 6, epígrafe de figura 4. Si no entra, se recortan las columnas «banda de
guarda» y «campaña», nunca la columna «medido».

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada fila se copió de `DOC-07` §13 y su campaña existe en `mediciones/`.
- [ ] Cada valor medido tiene tamaño de muestra declarado al lado.
- [ ] La banda de guarda de 3 dB aparece en la misma tabla, no en una nota.
- [ ] Ninguna fila mezcla valor medido con expectativa de diseño.
- [ ] Las figuras se regeneran por comando desde `crudo/` y no se editaron a mano.
- [ ] Toda afirmación tiene un ID detrás (`A#`, `T-##`, `M-##`) y una campaña asociada.
