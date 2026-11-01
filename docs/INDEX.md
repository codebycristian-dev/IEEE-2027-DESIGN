# Registro de documentos del proyecto

Este archivo es la **autoridad sobre qué documento está vigente**. Si un documento no figura acá, no
existe para efectos de la propuesta. Si hay dos versiones, vale la que esta tabla marca como vigente.

Última actualización: 2026-10-14.

## Registro

| Código | Título | Versión | Fecha | Estado | Archivo | Relación |
| --- | --- | --- | --- | --- | --- | --- |
| DOC-01 | Antenas receptoras reconfigurables para ISAC: evaluación de seis tecnologías candidatas | 1.0 | 2026-10-06 | **Vigente** | `docs/doc-01-evaluacion-tecnologias.pdf` | Origen de la decisión tecnológica y de los requisitos R1–R9 |
| DOC-02 | Registro del proyecto y decisión final de tecnología (ESPAR vs. RIS vs. píxeles) | 2.0 | 2026-10-13 | **Superado** | `docs/doc-02-propuesta-inicial.pdf` | Punto de partida sin trazabilidad de diseño; se conserva como histórico |

Los códigos siguientes (`DOC-03` en adelante) están libres. Se asignan con el criterio de la sección
«Cómo se agrega un documento».

> `DOC-02` está marcado **Superado** y todavía no tiene reemplazo escrito. Mientras eso siga así, la
> especificación de diseño del proyecto es la de DOC-02 §5.1, con la salvedad de que sus cotas son de
> orden de magnitud y no están verificadas.

## Convención de identificadores

Los identificadores son estables: **no se renumeran ni se reutilizan**, aunque el elemento se
descarte. Un identificador descartado queda marcado como descartado.

| Prefijo | Significado | Dónde vive |
| --- | --- | --- |
| `R#` | Requisito impuesto por las bases del concurso | DOC-01, tabla 2 y tabla 7 |
| `DR-##` | Requisito de diseño, verificable y con fuente | documento de especificación de diseño |
| `DV-##` | Variable de diseño con rango y criterio de barrido | documento de geometría |
| `DEC-##` | Decisión de diseño con alternativas descartadas | documento de especificación de diseño |
| `A#` | Criterio de aceptación del prototipo | DOC-02 §7.1 y documento de verificación |
| `T-##` | Protocolo de ensayo que verifica un `A#` | documento de verificación |
| `RSK-##` | Riesgo con mitigación y disparador | registro de riesgos |
| `P#` | Pregunta abierta a los organizadores | DOC-02 §8.1 y registro de preguntas |

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
5. Si el documento cambia una decisión, dejá la entrada nueva en el historial de versiones de ese
   documento, no acá.
