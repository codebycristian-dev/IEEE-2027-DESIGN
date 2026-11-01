# Repositorio de soporte y trazabilidad de diseño — ESPAR ISAC 2027

Feature: estructura del repositorio + documentación de diseño que respalda la propuesta de 4 páginas del 2027 IEEE AP-S Student Design Contest (ISAC). Technología: ESPAR de 7 elementos a 2.44 GHz con diodos PIN.
Rama: `feat/repo-espar-isac`. Estado: en curso.

## Specs

S1. DOC-01 es la evaluación de tecnologías válida y fuente de requisitos: «el archivo 1 es ded evaluacioń de tecnologías».
S2. DOC-02 no es especificación ni diseño final y no tiene trazabilidad: «el segundo solo es una propuesta que no se ha refinado, que no es la final y que no tiene trazabilidad de diseño, solo es un punto de partida». Se conserva como documento histórico, marcado como superado.
S3. Objeto del proyecto: «lo que se quiere es diseñar una ESPAR».
S4. Se genera el esqueleto del repositorio con la opción estructural recomendada (D: raíz por artefacto, capítulos del documento como archivos): «Genera el esqueleto, del proyecto teniendo en cuenta eso, usa la opción recomendada para construir el repositorio».
S5. Se genera la documentación que justifica una propuesta de diseño defendible ante los jueces: «genera la Documentación necesaria para justificar una buena propuesta de Diseño para el concurso».
S6. Se mejora la propuesta de diseño con soporte en estado del arte y buenas prácticas de ingeniería de diseño: «mejora la propuesta de Diseño, con soporte en la documentación en el estado del arte y usando buenas pauta de ingenieria de Diseño».
S7. No se redacta la propuesta de 4 páginas en este trabajo: «Lo que se quiere no es construir el documento de 4 páginas de momento».
S8. El repositorio debe respaldar esas 4 páginas, con trazabilidad explícita y con la teoría de diseño que no cabe en ellas: «se quiere es tener un repositorio que respalde esas 4 paginas y en donde este plasmado la trazabilidad y lo que no quepa en esas 4 paginas con respecto a la Teoria de Diseño».

## Tasks

| ID | Specs | Entrega | Ruta | Commit |
| --- | --- | --- | --- | --- |
| T1 | S4 | Rama, árbol de directorios, documento de feature | `odd/tasks/espar-isac-2027.md` | (este commit) |
| T2 | S2 | Reubicación de `DOC-01`/`DOC-02` con `git mv`, DOC-02 marcado como superado | `docs/doc-01-*.pdf`, `docs/doc-02-*.pdf` | U1 |
| T3 | S4, S8 | README raíz + registro documental `DOC-NN` | `README.md`, `docs/INDEX.md` | U1 |
| T4 | S5, S8 | Teoría del ESPAR: acoplamiento mutuo, carga reactiva, simetría C6 | `docs/teoria/01-fundamentos-espar.md` | U2 |
| T5 | S6, S8 | Estado del arte con referencias verificadas y análisis de vacío | `docs/teoria/02-estado-del-arte.md` | U2 |
| T6 | S5 | Métricas, modelo y presupuesto de incertidumbre de medición | `docs/teoria/03-metricas-y-modelo.md` | U3 |
| T7 | S5, S8 | Trazabilidad `R1-R9` → `DR-##` → `A#` → `T-##` | `docs/teoria/04-requisitos-y-trazabilidad.md` | U3 |
| T8 | S6 | Especificación de diseño y decisiones `DEC-##` con alternativas descartadas | `docs/diseno/DOC-03-especificacion-de-diseno.md` | U4 |
| T9 | S6 | Geometría, variables `DV-##` y plan de barrido paramétrico | `docs/diseno/DOC-04-geometria-y-dimensionamiento.md` | U4 |
| T10 | S6 | Circuito de control y polarización de diodos PIN | `docs/diseno/DOC-05-control-y-polarizacion.md` | U5 |
| T11 | S6 | Libro de códigos: órbita C6 = 14 patrones, subconjunto útil | `docs/diseno/DOC-06-libro-de-codigos.md` | U5 |
| T12 | S5 | Plan de verificación `A1-A5` con protocolos, muestras e incertidumbre | `docs/diseno/DOC-07-plan-de-verificacion.md` | U6 |
| T13 | S6 | Registro de riesgos y compuertas de decisión | `docs/diseno/DOC-08-riesgos-y-compuertas.md` | U6 |
| T14 | S6 | Mejora de la propuesta: delta explícito contra DOC-02 | `docs/diseno/DOC-09-mejora-de-la-propuesta.md` | U6 |
| T15 | S4, S5 | BOM contra tope US$1500, cronograma, preguntas P1-P4 | `gestion/` | U7 |
| T16 | S7, S8 | Mapa de las 4 páginas y esqueletos de capítulo | `docs/borrador/` | U7 |

## Log

L1 (usuario, original): «me gustaria darle una estructura al repo, este va a ser el repositorio del diseño del concurso para participar en el concuros de antenas Reconfigurable Receiving Antennas for Integrated Sensing and Communications (ISAC) 2027 de la AP-S.»

L2 (usuario): «el archivo 1 es ded evaluacioń de tecnologías el segundo solo es una propuesta que no se ha refinado, que no es la final y que no tiene trazabilidad de diseño, solo es un punto de partida por que lo que se quiere es diseñar una ESPAR, Genera el esqueleto, del proyecto teniendo en cuenta eso, usa la opción recomendada para construir el repositorio y genera la Documentación necesaria para justificar una buena propuesta de Diseño para el concurso, y mejora la propuesta de Diseño, con soporte en la documentación en el estado del arte y usando buenas pauta de ingenieria de Diseño. Lo que se quiere no es construir el documento de 4 páginas de momento sino que se quiere es tener un repositorio que respalde esas 4 paginas y en donde este plasmado la trazabilidad y lo que no quepa en esas 4 paginas con respecto a la Teoria de Diseño. Entiendes cual es la tarea?»

L3 (decisión de orquestación): estructura por tipo de artefacto con capítulos como archivos de documento (opción D), elegida sobre la propuesta de seis carpetas numeradas por capítulo, porque los mismos datos alimentan varios capítulos y porque firmware, PCB y mediciones no tienen capítulo natural.

L4 (decisión): git local `codebycristian-dev <cdoradog@unal.edu.co>` y remote `origin` migrado a SSH, porque HTTPS no tenía credenciales en esta máquina.

L5 (decisión): id de trazabilidad con prefijos fijos — `R` (bases del concurso), `DR` (requisito de diseño), `DV` (variable de diseño), `DEC` (decisión), `A` (criterio de aceptación), `T` (protocolo de ensayo), `RSK` (riesgo). Todo documento nuevo usa estos prefijos y no crea otros.
