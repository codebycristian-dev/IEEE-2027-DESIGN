# Registro de documentos del proyecto

Este archivo es la **autoridad sobre qué documento está vigente**. Si un documento no figura acá,
no existe para efectos de la propuesta. Si hay dos versiones, vale la que esta tabla marca como
vigente.

Última actualización: 2026-10-14.

## Registro

| Código | Título | Versión | Fecha | Estado | Archivo | Relación |
| --- | --- | --- | --- | --- | --- | --- |
| DOC-01 | Antenas receptoras reconfigurables para ISAC: evaluación de seis tecnologías candidatas | 1.0 | 2026-10-06 | **Vigente** | `docs/doc-01-evaluacion-tecnologias.pdf` | Origen de la decisión tecnológica y de los requisitos R1–R9 |
| DOC-02 | Registro del proyecto y decisión final de tecnología (ESPAR vs. RIS vs. píxeles) | 2.0 | 2026-10-13 | **Superado** por DOC-03 | `docs/doc-02-propuesta-inicial.pdf` | Punto de partida sin trazabilidad de diseño; se conserva como histórico |
| DOC-03 | Especificación de diseño del ESPAR de 7 elementos | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-03-especificacion-de-diseno.md` | Deriva de DOC-01; reemplaza la propuesta técnica de DOC-02 |
| DOC-04 | Geometría y dimensionamiento | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-04-geometria-y-dimensionamiento.md` | Detalla DOC-03 §5 |
| DOC-05 | Circuito de control y polarización de diodos PIN | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-05-control-y-polarizacion.md` | Detalla DOC-03 §6 |
| DOC-06 | Libro de códigos de configuraciones | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-06-libro-de-codigos.md` | Detalla DOC-03 §7 |
| DOC-07 | Plan de verificación de los criterios de aceptación | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-07-plan-de-verificacion.md` | Operacionaliza los criterios A1–A5 de DOC-02 §7.1 |
| DOC-08 | Riesgos y compuertas de decisión | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-08-riesgos-y-compuertas.md` | Actualiza los riesgos de DOC-02 §6.4 y §7.2 |
| DOC-09 | Mejora de la propuesta de diseño: delta contra DOC-02 | 1.0 | 2026-10-14 | Vigente | `docs/diseno/DOC-09-mejora-de-la-propuesta.md` | Explica qué cambia y por qué respecto de DOC-02 |

## Notas técnicas (no son DOC-NN)

Las notas de `docs/teoria/` son material de respaldo: teoría, estado del arte, métricas y
trazabilidad. No llevan número de documento porque no se presentan al concurso; se citan desde
los DOC-NN.

| Nota | Título | Archivo |
| --- | --- | --- |
| N-01 | Fundamentos del ESPAR con elementos parásitos conmutados | `docs/teoria/01-fundamentos-espar.md` |
| N-02 | Estado del arte y análisis de vacío | `docs/teoria/02-estado-del-arte.md` |
| N-03 | Métricas, modelo y presupuesto de incertidumbre | `docs/teoria/03-metricas-y-modelo.md` |
| N-04 | Requisitos y matriz de trazabilidad | `docs/teoria/04-requisitos-y-trazabilidad.md` |

## Artefactos de gestión y borrador (no son DOC-NN)

| Artefacto | Contenido | Archivo |
| --- | --- | --- |
| BOM | Lista de materiales y costo acumulado contra el tope de `R7` | `gestion/BOM.md` |
| Cronograma | Plan fechado único: pasos, etapas de diseño, compuertas y ensayos | `gestion/cronograma.md` |
| Preguntas `P#` | Registro de preguntas a los organizadores y correo de envío | `gestion/preguntas-organizadores.md` |
| Mapa de la propuesta | Qué entra en cada una de las 4 páginas y de qué documento sale | `docs/borrador/00-mapa-propuesta-4-paginas.md` |
| Esqueletos de capítulo | `01-introduccion` … `06-discusion`, en estado de esqueleto | `docs/borrador/` |

Advertencia de vigencia: los esqueletos de `docs/borrador/` **no son la propuesta**. La propuesta se
redacta después de la compuerta `G4` de `DOC-08`, con datos medidos.

## Convención de identificadores

Los identificadores son estables: **no se renumeran ni se reutilizan** aunque el elemento se
descarte. Un identificador descartado queda marcado como descartado.

| Prefijo | Significado | Vive en |
| --- | --- | --- |
| `R#` | Requisito impuesto por las bases del concurso | N-04 (derivados de DOC-01 tabla 2) |
| `DR-##` | Requisito de diseño, verificable y con fuente | N-04 |
| `DV-##` | Variable de diseño con rango y criterio de barrido | DOC-04 |
| `DEC-##` | Decisión de diseño con alternativas descartadas | DOC-03 |
| `A#` | Criterio de aceptación del prototipo | DOC-03, verificado por DOC-07 |
| `T-##` | Protocolo de ensayo que verifica un `A#` | DOC-07 |
| `RSK-##` | Riesgo con mitigación y disparador | DOC-08 |
| `P#` | Pregunta abierta a los organizadores | `gestion/preguntas-organizadores.md` |

## Cómo se agrega un documento

1. Elegí el próximo código `DOC-NN` libre de esta tabla. No reutilices códigos.
2. Abrí el documento con la **ficha de control** que ya usan DOC-01 y DOC-02:

   ```
   | Código | DOC-NN |
   | Versión / fecha | x.y — AAAA-MM-DD |
   | Documento previo | DOC-MM vX.Y, <título> (fecha) |
   | Tipo | ... |
   | Estado | Borrador | Para decisión | Vigente | Superado |
   ```

3. Agregá la fila en la tabla de este registro **en el mismo commit** que el documento.
4. Si reemplaza a otro, marcá el anterior como *Superado por DOC-NN*. No borres el archivo.
5. Si el documento cambia una decisión, actualizá `doc-XX` correspondiente y dejá la entrada
   nueva en el historial de versiones de ese documento, no acá.
