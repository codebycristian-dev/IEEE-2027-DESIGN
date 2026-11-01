# Registro de decisiones de estructura del repositorio

Feature: esqueleto del repositorio del proyecto ESPAR para el 2027 IEEE AP-S Student Design Contest.
Rama: `feat/esqueleto-repo`. Estado: cerrada.

## Specs

S1. El repositorio es el del diseño del concurso: «este va a ser el repositorio del diseño del concurso para participar en el concuros de antenas Reconfigurable Receiving Antennas for Integrated Sensing and Communications (ISAC) 2027 de la AP-S».
S2. DOC-01 es la evaluación de tecnologías válida: «el archivo 1 es ded evaluacioń de tecnologías».
S3. DOC-02 no es especificación ni diseño final y no tiene trazabilidad: «el segundo solo es una propuesta que no se ha refinado, que no es la final y que no tiene trazabilidad de diseño, solo es un punto de partida».
S4. El alcance pedido es el esqueleto: «solo queria el esqueleto del repositorio».

## Tasks

| ID | Specs | Entrega | Ruta |
| --- | --- | --- | --- |
| T1 | S1, S2, S3 | Árbol de directorios por tipo de artefacto y reubicación de DOC-01/DOC-02 | `docs/`, `hardware/`, `firmware/`, `software/`, `mediciones/`, `propuesta/`, `gestion/` |
| T2 | S1 | README raíz con qué contiene el repositorio y cómo se usa | `README.md` |
| T3 | S2, S3 | Registro `DOC-NN` y convención de identificadores | `docs/INDEX.md` |
| T4 | S4 | README en cada carpeta diciendo qué va adentro | una por directorio |
| T5 | S2, S3, S4 | Ajuste de README e INDEX para que no citen documentos que no existen | este commit |

## Log

L1 (usuario, original): «me gustaria darle una estructura al repo, este va a ser el repositorio del diseño del concurso para participar en el concuros de antenas Reconfigurable Receiving Antennas for Integrated Sensing and Communications (ISAC) 2027 de la AP-S.»

L2 (usuario): «el archivo 1 es ded evaluacioń de tecnologías el segundo solo es una propuesta que no se ha refinado, que no es la final y que no tiene trazabilidad de diseño, solo es un punto de partida por que lo que se quiere es diseñar una ESPAR, Genera el esqueleto, del proyecto teniendo en cuenta eso, usa la opción recomendada para construir el repositorio.»

L3 (decisión): estructura por tipo de artefacto, con los capítulos del documento como archivos dentro de `docs/borrador/`, en lugar de seis carpetas numeradas por capítulo. Motivo: los mismos datos alimentan varios capítulos, y firmware, PCB y mediciones no tienen capítulo natural.

L4 (decisión): los documentos históricos se reubican con `git mv` conservando historia y se renombran como `doc-01-…` y `doc-02-…`; DOC-02 se marca como superado en el registro.

L5 (usuario): «che solo queria el esqueleto del repositorio.» La documentación de diseño que se había escrito en paralelo queda en la rama `feat/repo-espar-isac`, fuera de esta rama. Este repositorio queda sólo con la estructura.

L6 (decisión): una rama no puede citar documentos que no tiene. El commit de estructura citaba `DOC-03` a `DOC-09` en el README y en el INDEX; este commit los recorta a lo que existe y deja constancia en el INDEX de que DOC-02 sigue superado y sin reemplazo escrito.
