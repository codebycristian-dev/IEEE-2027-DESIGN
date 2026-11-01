# 02 — Estado del arte

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, sin redacción |
| Fuente principal | `docs/teoria/02-estado-del-arte.md` §2–§9 y §11 (lista maestra de referencias) |
| Apoyo | `DOC-01` (evaluación de tecnologías, PDF), `DOC-09` §2 |
| Ubicación y fecha | Página 1 (cierre); se redacta el 2026-12-22, después de la compuerta G4 |

## Objetivo del capítulo

Ubicar el diseño en la literatura en pocas líneas: qué se hizo antes, qué se toma de cada trabajo y
qué queda sin resolver. No es una revisión bibliográfica: es el argumento de que hay algo propio.

## Qué va

- **Origen.** Harrington [1] demuestra que un patrón directivo se sintetiza con un solo puerto de RF
  variando la reactancia de los elementos no alimentados (`N-02` §2).
- **Techo de la arquitectura.** Gyoda y Ohira [2] reportan 9 dBi ± 1 dB y nulos más profundos que
  −50 dB, pero con **varactores**: se cita para declarar de entrada qué se pierde al bajar a un PIN
  binario (`N-02` §2, `DOC-09` §2).
- **Control discreto.** Vaughan [4] y Thiel et al. [5]: conmutar un parásito entre cortocircuito y
  abierto en el punto de máxima corriente alcanza para dirigir el haz. Es la operación del PIN del
  proyecto (`N-02` §3).
- **Antecedente más cercano.** Caluyo y Ballado [3], ESPAR de 7 elementos en banda ISM medido; fija la
  expectativa realista de ganancia, 6–9 dBi (`N-01` §6, `N-02` §4).
- **Método.** Schlub, Lu y Ohira [8] aplican optimización genética y elementos finitos a un ESPAR de 7
  elementos: no se copia la geometría, se copia la disciplina de variables declaradas (`N-02` §3).
- **Plano de tierra.** Ojiro et al. [7] cuantifican que el plano finito baja el ángulo de máxima
  radiación: por eso `DV-03` es variable de diseño y la falda es plan B (`N-02` §6, `DOC-04` §5).
- **Vacío y tabla comparada.** Los cuatro puntos de `N-02` §9 con la cita al lado de cada uno, más una
  tabla de 4 filas con trabajo, elementos, mecanismo, banda y resultado reportado.

## Qué no va

- Las 27 referencias de `N-02` §11: a la propuesta van **6 a 10**, solo las leídas o con metadatos
  verificados. Una referencia sin leer no sostiene una cifra.
- RIS y antenas de píxeles [16]–[18]: una frase de descarte; la evaluación completa está en `DOC-01`.
- RF-MEMS [19] y varactores como alternativa real: la restricción del mentor fija PIN, y eso es una
  restricción, no una comparación.
- El historial de ganadores (`N-02` §10): a lo sumo una frase, y solo si sostiene `DEC-14`.
- Novedad absoluta: la formulación admitida es «no se localizó un trabajo revisado por pares que use
  conmutación de parásitos junto con CSI de ESP32» (`N-02` §11).

## Extensión prevista

Página 1, **≈ 12 de las 44 líneas**: origen y techo 4, control discreto y antecedente 3, vacío 5. La
tabla compite con la figura de arquitectura: si no hay espacio, se convierte en tres frases.

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada `[n]` existe en `N-02` §11 y su estado de lectura está declarado.
- [ ] Ninguna cifra de otro trabajo se presenta como expectativa propia del diseño.
- [ ] El techo de −50 dB se atribuye a varactores y se aclara que no es trasladable.
- [ ] El vacío se apoya en `N-02` §9 y no afirma novedad absoluta.
- [ ] Toda afirmación tiene un ID detrás (`DR-##`, `DEC-##`) o una referencia de `N-02` §11.
