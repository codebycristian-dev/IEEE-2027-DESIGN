# Reconfigurable Receiving Antenna for ISAC — 2027 IEEE AP-S Student Design Contest

Repositorio de soporte del equipo para el concurso **Reconfigurable Receiving Antennas for
Integrated Sensing and Communications (ISAC)**, IEEE AP-S Student Design Contest 2027.

**Diseño adoptado:** ESPAR de 7 elementos a 2400–2483.5 MHz (f₀ = 2.44 GHz), con un monopolo
activo central y seis monopolos parásitos conmutados a tierra mediante diodos PIN (Skyworks
SMP1345), controlados por un ESP32.

| | |
| --- | --- |
| Equipo | Cristian Dorado · Jerónimo Chivatá · Sergio Gonzalez |
| Mentor (IEEE AP-S) | Julio Cesar García |
| Entregable de la fase actual | Propuesta de 4 páginas + BOM + carta del mentor |
| Plazo | **31 de diciembre de 2026, 23:59 GMT−10** |
| Hito siguiente | Prototipo v0 sin diodos (14-nov-2026) |

## Qué es este repositorio

Es el **respaldo técnico y la trazabilidad** de la propuesta de 4 páginas, no la propuesta. Acá
vive todo lo que no entra en cuatro páginas: la teoría de diseño, el estado del arte con
referencias, las decisiones de ingeniería con sus alternativas descartadas, el plan de
verificación y los datos de medición.

La regla que ordena el repositorio: **cada afirmación de la propuesta tiene que poder rastrearse
hasta un documento, y cada documento hasta una medición o una referencia.** La cadena completa
está en [`docs/teoria/04-requisitos-y-trazabilidad.md`](docs/teoria/04-requisitos-y-trazabilidad.md).

## Por dónde empezar

Si es tu primera vez en el repo, este orden tiene sentido:

1. [`docs/INDEX.md`](docs/INDEX.md) — registro de documentos del proyecto y qué está vigente.
2. [`docs/teoria/01-fundamentos-espar.md`](docs/teoria/01-fundamentos-espar.md) — cómo funciona un ESPAR.
3. [`docs/teoria/02-estado-del-arte.md`](docs/teoria/02-estado-del-arte.md) — qué se hizo antes y qué hueco ocupa este diseño.
4. [`docs/diseno/DOC-03-especificacion-de-diseno.md`](docs/diseno/DOC-03-especificacion-de-diseno.md) — la especificación vigente y sus decisiones.
5. [`docs/diseno/DOC-07-plan-de-verificacion.md`](docs/diseno/DOC-07-plan-de-verificacion.md) — cómo se demuestra que funciona.

## Estructura

```
docs/
  INDEX.md            Registro de documentos DOC-NN y estado de vigencia
  doc-01, doc-02      Documentos históricos del equipo (PDF)
  teoria/             Teoría de diseño: lo que no cabe en 4 páginas
  diseno/             Especificación, geometría, control, libro de códigos, verificación, riesgos
  borrador/           Mapa de las 4 páginas y esqueletos de capítulo
hardware/
  antena/             Geometría del arreglo, planos, cotas
  pcb/                Diseño de la PCB de control y polarización
  mecanica/           Plano de tierra, soporte, plataforma giratoria
firmware/espar-esp32/ Control de los seis diodos PIN y secuencias de conmutación
software/
  codebook/           Generación y validación del libro de códigos
  instrumentos/       Adquisición desde NanoVNA/LiteVNA
  analisis/           SIR por MAC, patrones, detección de movimiento
mediciones/           Una carpeta por campaña; datos crudos y procesados juntos
propuesta/            El entregable del 31-dic: 4 páginas, BOM, carta del mentor
gestion/              BOM y costo acumulado, cronograma, preguntas a los organizadores
odd/tasks/            Registro de trabajo y decisiones de proceso
```

## Qué contiene el repositorio hoy

Estado al 2026-10-14. Las carpetas marcadas *pendiente* existen con un `README.md` que dice qué va
dentro; todavía no tienen artefactos.

| Ruta | Contenido | Estado |
| --- | --- | --- |
| `README.md` | Este archivo: qué es el repo, qué contiene, cómo se usa | Vigente |
| `docs/INDEX.md` | Registro `DOC-NN`, convención de identificadores, cómo se agrega un documento | Vigente |
| `docs/doc-01-evaluacion-tecnologias.pdf` | Evaluación de las seis tecnologías candidatas | Vigente (fuente) |
| `docs/doc-02-propuesta-inicial.pdf` | Propuesta inicial ESPAR-PIN, sin trazabilidad de diseño | **Superado** por DOC-03 |
| `docs/teoria/01-fundamentos-espar.md` | Teoría: acoplamiento mutuo, carga reactiva, simetría C6 | Vigente |
| `docs/teoria/02-estado-del-arte.md` | Estado del arte con referencias verificadas y análisis de vacío | Vigente |
| `docs/teoria/03-metricas-y-modelo.md` | Definición de métricas y presupuesto de incertidumbre | Vigente |
| `docs/teoria/04-requisitos-y-trazabilidad.md` | Matriz `R → DR → A → T` | Vigente |
| `docs/diseno/DOC-03` | Especificación de diseño y decisiones `DEC` | Vigente |
| `docs/diseno/DOC-04` | Geometría, variables `DV` y plan de barrido | Vigente |
| `docs/diseno/DOC-05` | Circuito de control y polarización de los diodos PIN | Vigente |
| `docs/diseno/DOC-06` | Libro de códigos de configuraciones | Vigente |
| `docs/diseno/DOC-07` | Plan de verificación `A1-A5` con protocolos `T` | Vigente |
| `docs/diseno/DOC-08` | Riesgos `RSK` y compuertas de decisión | Vigente |
| `docs/diseno/DOC-09` | Mejora de la propuesta: delta explícito contra DOC-02 | Vigente |
| `docs/borrador/` | Mapa de las 4 páginas y esqueletos de capítulo | Vigente como índice |
| `gestion/BOM.md` | Lista de materiales con costo acumulado contra el tope de US$1500 | Vigente |
| `gestion/cronograma.md` | Plan de acción fechado hasta el envío | Vigente |
| `gestion/preguntas-organizadores.md` | Preguntas `P1-P4` y respuestas recibidas | Vigente |
| `hardware/antena/` | Cotas del arreglo, planos de fabricación | Pendiente |
| `hardware/pcb/` | Esquemático y layout de la PCB de control | Pendiente |
| `hardware/mecanica/` | Plano de tierra, soporte, plataforma giratoria | Pendiente |
| `firmware/espar-esp32/` | Firmware de conmutación y adquisición | Pendiente |
| `software/codebook/` | Generación y validación del libro de códigos | Pendiente |
| `software/instrumentos/` | Adquisición desde NanoVNA/LiteVNA | Pendiente |
| `software/analisis/` | Procesamiento de patrones, SIR y detección | Pendiente |
| `mediciones/` | Campañas de medición, una carpeta por campaña | Vacío: la primera se crea con el prototipo v0 |
| `propuesta/` | El PDF de 4 páginas, BOM y carta del mentor | Vacío a propósito |
| `odd/tasks/espar-isac-2027.md` | Registro de trabajo: specs, tareas y decisiones de proceso | Vigente |

**Lo que el repositorio no contiene todavía, y es deliberado:** la propuesta de 4 páginas, los
planos de fabricación, el firmware, los datos de medición y la carta del mentor. Todo eso depende
de hardware que aún no se compró.

## Cómo se usa

### Para leer

Empezá por `docs/INDEX.md`. Define qué está vigente. Después `docs/teoria/01` y `02` para el
fundamento, `docs/diseno/DOC-03` para la especificación y `DOC-07` para cómo se demuestra.
No leas DOC-02 como si fuera la especificación: está superado.

### Para escribir en la propuesta de 4 páginas

Cada afirmación que vaya al PDF tiene que tener un identificador detrás:

1. Si afirmás un requisito, citá el `DR-##` y su `R#` de origen (`docs/teoria/04`).
2. Si afirmás un número de diseño, citá la `DV-##` y el `DEC-##` que lo fijó (`DOC-03`, `DOC-04`).
3. Si afirmás un resultado, citá el `T-##` y la campaña en `mediciones/` que lo produjo.
4. Si afirmás una ventaja frente al estado del arte, citá la referencia de `docs/teoria/02`.

Si una frase del PDF no se puede rastrear así, o el documento falta o la frase no se sostiene.
El recorte de qué entra en cada página está en `docs/borrador/00-mapa-propuesta-4-paginas.md`.

### Para registrar una decisión de diseño nueva

1. Agregá la fila `DEC-##` en `docs/diseno/DOC-03-especificacion-de-diseno.md`, con la
alternativa descartada y el motivo. Una decisión sin alternativa descartada no es una decisión.
2. Si cambia un requisito de diseño, actualizá la fila `DR-##` en `docs/teoria/04`.
3. Si cambia el estado de vigencia de un documento, actualizá `docs/INDEX.md` en el mismo commit.

### Para registrar una campaña de medición

1. Creá `mediciones/AAAA-MM-asunto/` con tres subcarpetas: `crudo/`, `procesado/`, `figuras/`.
2. Escribí el `README.md` de la campaña **antes** de medir: qué `T-##` ejecutás, qué instrumento,
quién, fecha, condiciones (distancia, altura, orientación), y qué esperás encontrar.
3. Nunca separes el crudo del procesado: sin el crudo no se puede rehacer una figura para la
propuesta a último momento.
4. Si una campaña supera los 20 MB, avisá antes de commitear: se decide si va con LFS o como resumen.

### Antes de enviar la propuesta

- [ ] Todo `DR-##` tiene un `A#` que lo verifica.
- [ ] Todo `A#` tiene un `T-##` y una campaña en `mediciones/`.
- [ ] `gestion/BOM.md` cierra por debajo de US$1500 con precios fechados.
- [ ] Las preguntas `P1-P3` de `gestion/preguntas-organizadores.md` tienen respuesta o se documenta el silencio.
- [ ] Ningún documento vigente contradice a otro: `docs/INDEX.md` está al día.

## Convenciones

- **Idioma**: documentos internos en español; identificadores, código y comentarios de código en inglés.
- **Rutas**: sin espacios, sin acentos y sin puntos en los nombres de archivo, para no romper LaTeX, Python ni shell.
- **Trazabilidad**: los identificadores son estables y no se renumeran. `R` requisito de las bases · `DR` requisito de diseño · `DV` variable de diseño · `DEC` decisión de diseño · `A` criterio de aceptación · `T` protocolo de ensayo · `RSK` riesgo. La convención completa está en `docs/INDEX.md`.
- **Vigencia**: un documento no se borra, se marca como superado en `docs/INDEX.md` con el que lo reemplaza.

## Estado de los documentos

| Documento | Estado |
| --- | --- |
| DOC-01 Evaluación de seis tecnologías | Vigente — base de la decisión tecnológica |
| DOC-02 Propuesta inicial (ESPAR-PIN) | **Superado** por DOC-03; se conserva sin trazabilidad de diseño |
| DOC-03 a DOC-09 | Vigentes — ver `docs/INDEX.md` |

## Alcance de la fase actual

La propuesta de 4 páginas **no está escrita todavía** y este repositorio no la contiene
deliberadamente: primero se construye el respaldo técnico, después se recorta a cuatro páginas.
El mapa de ese recorte está en [`docs/borrador/00-mapa-propuesta-4-paginas.md`](docs/borrador/00-mapa-propuesta-4-paginas.md).
