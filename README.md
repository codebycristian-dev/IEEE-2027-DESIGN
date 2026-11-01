# Reconfigurable Receiving Antenna for ISAC — 2027 IEEE AP-S Student Design Contest

Repositorio del equipo para el concurso **Reconfigurable Receiving Antennas for Integrated Sensing
and Communications (ISAC)**, IEEE AP-S Student Design Contest 2027.

**Diseño adoptado:** ESPAR de 7 elementos a 2400–2483.5 MHz (f₀ = 2.44 GHz), con un monopolo activo
central y seis monopolos parásitos conmutados a tierra mediante diodos PIN, controlados por un ESP32.

| | |
| --- | --- |
| Equipo | Cristian Dorado · Jerónimo Chivatá · Sergio Gonzalez |
| Mentor (IEEE AP-S) | Julio Cesar García |
| Entregable de la fase actual | Propuesta de 4 páginas + BOM + carta del mentor |
| Plazo | **31 de diciembre de 2026, 23:59 GMT−10** |

## Qué contiene el repositorio hoy

**La estructura, y sólo la estructura.** Al 2026-10-14 el repositorio tiene el esqueleto de carpetas,
los dos documentos históricos del equipo y las reglas de uso. No hay todavía documentos de diseño,
código, planos ni mediciones: las carpetas existen con un `README.md` que dice qué va adentro.

| Ruta | Contenido | Estado |
| --- | --- | --- |
| `README.md` | Este archivo | Vigente |
| `docs/INDEX.md` | Registro de documentos `DOC-NN` y convención de identificadores | Vigente |
| `docs/doc-01-evaluacion-tecnologias.pdf` | Evaluación de las seis tecnologías candidatas | Vigente (fuente de la decisión) |
| `docs/doc-02-propuesta-inicial.pdf` | Propuesta inicial ESPAR-PIN, sin trazabilidad de diseño | **Superado**: es punto de partida, no especificación |
| `docs/teoria/` | Notas de teoría de diseño | Vacío |
| `docs/diseno/` | Especificación, geometría, control, verificación, riesgos | Vacío |
| `docs/borrador/` | Capítulos del documento | Vacío |
| `hardware/antena/` | Cotas del arreglo y planos de fabricación | Vacío |
| `hardware/pcb/` | Esquemático y layout de la PCB de control | Vacío |
| `hardware/mecanica/` | Plano de tierra, soporte, plataforma giratoria | Vacío |
| `firmware/espar-esp32/` | Firmware de conmutación y adquisición | Vacío |
| `software/codebook/` | Generación y validación del libro de códigos | Vacío |
| `software/instrumentos/` | Adquisición desde NanoVNA/LiteVNA | Vacío |
| `software/analisis/` | Patrones, SIR por MAC, detección de movimiento | Vacío |
| `mediciones/` | Campañas de medición, una carpeta por campaña | Vacío |
| `propuesta/` | El PDF de 4 páginas, BOM y carta del mentor | Vacío a propósito |
| `gestion/` | BOM, cronograma y preguntas a los organizadores | Vacío |
| `odd/tasks/` | Registro de las decisiones de estructura del repositorio | Vigente |

## Cómo se usa

### Para leer

Empezá por `docs/INDEX.md`: dice qué documento está vigente. Hoy hay dos documentos y un esqueleto.
**No leas `doc-02-propuesta-inicial.pdf` como especificación**: está superado y no tiene trazabilidad
de diseño.

### Para agregar un documento

1. Elegí el próximo código `DOC-NN` libre en `docs/INDEX.md` y no reutilices códigos.
2. Abrí el documento con una ficha de control (código, versión y fecha, documento previo, tipo,
   estado), como ya hacen DOC-01 y DOC-02.
3. Registralo en `docs/INDEX.md` **en el mismo commit** que el documento.
4. Si reemplaza a otro, marcá el anterior como *Superado por DOC-NN*. No borres el archivo.

### Para registrar una campaña de medición

1. Creá `mediciones/AAAA-MM-asunto/` con tres subcarpetas: `crudo/`, `procesado/`, `figuras/`.
2. Escribí el `README.md` de la campaña **antes** de medir: qué se mide, con qué instrumento, quién,
   fecha, condiciones (distancia, altura, orientación) y qué se espera encontrar.
3. El crudo no se edita a mano. Si una campaña supera los 20 MB, se decide antes de commitear si va
   con LFS o como resumen.

## Convenciones

- **Idioma**: documentos internos en español; identificadores, código y comentarios de código en inglés.
- **Rutas**: sin espacios, sin acentos y sin puntos en los nombres de archivo, para no romper LaTeX,
  Python ni shell.
- **Identificadores**: se reservan los prefijos `R` (requisito de las bases), `DR` (requisito de
  diseño), `DV` (variable de diseño), `DEC` (decisión), `A` (criterio de aceptación), `T` (protocolo
  de ensayo), `RSK` (riesgo) y `P` (pregunta a los organizadores). No se renumeran ni se reutilizan.
  La convención completa está en `docs/INDEX.md`.
- **Vigencia**: un documento no se borra, se marca como superado con el que lo reemplaza.
