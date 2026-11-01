# Preguntas a los organizadores (`P1`–`P4`)

| | |
| --- | --- |
| Artefacto | Registro de preguntas abiertas al comité del concurso |
| Versión / fecha | 1.0 — 2026-10-14 |
| Estado | **Ninguna pregunta enviada.** Fecha de envío prevista: 2026-10-17 |
| Origen | DOC-02 §8.1 (texto de las preguntas), `N-04` §7 (requisito afectado) |
| Compuerta que depende de esto | **G0 — 2026-10-24** (`DOC-08` §4) |

## Canal y formato

| | |
| --- | --- |
| Dirección | `designcontest@2027.apsursi.org` |
| Asunto obligatorio | `2027 IEEE AP-S Design Contest [NombreDelEquipo]` |
| Idioma | inglés (los organizadores son internacionales; el registro interno queda en español) |
| Remitente | el miembro del equipo que figure como contacto en el formulario de inscripción |

El asunto se transcribe literalmente, con corchetes y sin traducir: es el formato que fija DOC-02
§8.1 y cambiarlo es la forma más fácil de que el correo se pierda en una bandeja compartida. En
`[NombreDelEquipo]` va el nombre con el que el equipo se inscribió, sin espacios si el nombre los
tiene.

## Estado de las cuatro preguntas

| ID | Pregunta (español) | Requisito afectado | Estado | Fecha de envío | Respuesta |
| --- | --- | --- | --- | --- | --- |
| P1 | ¿Un receptor comercial (ESP32 o SDR) configurado para no transmitir cumple el requisito de operar estrictamente como receptor? ¿Cómo debe documentarse? | `DR-02` (protocolo `T-01`) | pendiente de envío | prevista 2026-10-17 | — |
| P2 | ¿Los instrumentos usados solo en desarrollo (por ejemplo, un analizador vectorial) cuentan dentro de los US$1500? | `DR-11` (`gestion/BOM.md`, bloques A y B) | pendiente de envío | prevista 2026-10-17 | — |
| P3 | ¿Los organizadores proveen transmisores en Kioto o cada equipo lleva los suyos con certificación japonesa? | `DR-06` (protocolo `T-04`) | pendiente de envío | prevista 2026-10-17 | — |
| P4 | ¿Una superficie reflectiva pasiva cuenta como parte del sistema de antena receptora? | ninguno en el diseño vigente (aplicaría a la decisión tecnológica solo si se eligiera RIS) | **no bloqueante** — pendiente de envío | prevista 2026-10-17 | — |

Ninguna respuesta está registrada a la fecha de este documento. La columna «respuesta» se completa el
mismo día en que llega, con la cita textual y la fecha; no se parafrasea.

## Por qué P4 se envía aunque sea no bloqueante

`P4` pregunta si una superficie reflectiva pasiva cuenta como parte del sistema de antena receptora.
Esa pregunta **solo tiene consecuencias si el equipo hubiera elegido RIS**, y el diseño vigente es un
ESPAR de parásitos conmutados: no hay superficie reflectiva en el sistema (`DEC-01` de `DOC-03` §4).
Hoy `P4` no afecta ningún `DR`, por eso está marcada como no bloqueante y no entra en el criterio de
paso de G0, que exige `P1`–`P3`.

Se envía igual por tres razones concretas:

1. **Costo cero.** Va en el mismo correo que `P1`–`P3`; no agrega envío ni espera.
2. **Es la constancia de la decisión.** Si en la semifinal un jurado pregunta por qué no se usó RIS,
   la respuesta documentada es que la pregunta se hizo y qué contestó el comité. Una decisión
   tecnológica con consulta registrada se defiende distinto de una decisión por preferencia.
3. **Protege contra un cambio de alcance.** La compuerta 4 de `DOC-08` §4 todavía permite reabrir la
   tecnología. Si eso pasara, `P4` ya estaría respondida y no habría que esperar semanas.

Lo que **no** se hace con `P4`: no se usa para reabrir la evaluación de tecnologías, que está cerrada
en `DOC-01` y `DOC-02` §7.

## Correo listo para enviar

Se deja en bloque de código para que el cliente de correo no lo reformatee: las cuatro preguntas van
numeradas y sin viñetas decorativas, porque el comité responde citando el número.

```text
To: designcontest@2027.apsursi.org
Subject: 2027 IEEE AP-S Design Contest [NombreDelEquipo]

Dear 2027 IEEE AP-S Student Design Contest Committee,

We are a student team from Universidad Nacional de Colombia preparing an entry for
the 2027 IEEE AP-S Student Design Contest on Reconfigurable Receiving Antennas for
Integrated Sensing and Communications (ISAC).

Our design is a seven-element electronically steerable passive array radiator
(ESPAR) operating as a receive-only antenna in the 2400-2483.5 MHz band, with six
parasitic monopoles switched to ground by PIN diodes and controlled by an ESP32.

Before we commit to the final bill of materials and verification plan, we would
appreciate clarification on the following four points. We have numbered them so
that they can be answered individually.

P1. A commercial receiver (for example an ESP32 module or an SDR) configured so that
    it never transmits: does it satisfy the requirement that the hardware operate
    strictly as a receiver? If so, how would you like this to be documented in the
    four-page proposal? We currently plan to show a spectrum capture with the
    system on and off, plus the receiver configuration, but we will follow whatever
    evidence you prefer.

P2. Do instruments used only during development (for example a portable vector
    network analyzer, a turntable, or a bench power supply) count toward the
    US$1500 total cost limit? We have separated the delivered system from the
    development instruments in our bill of materials, and we would like to know
    which column is the one that is evaluated.

P3. Do the organizers provide the transmitters used during the demonstration in
    Kyoto, or is each team expected to bring its own (for example a Wi-Fi router or
    a mobile hotspot)? If teams must bring their own, are there any Japanese
    certification or radio-regulation requirements we should account for, and would
    that equipment count toward the cost limit?

P4. Does a passive reflective surface count as part of the receiving antenna system
    for the purposes of this contest? This question is not blocking for our current
    design, which contains no reflective surface, but we would like to record the
    answer for completeness.

Thank you for your time. We would be glad to provide any additional detail about
our design or our verification plan.

Best regards,
[Nombre del contacto]
[NombreDelEquipo] - 2027 IEEE AP-S Student Design Contest
Universidad Nacional de Colombia
[correo de contacto]
```

## Seguimiento

| Paso | Cuándo | Qué se registra |
| --- | --- | --- |
| Envío | 2026-10-17 | fecha, hora y copia del correo enviado en este archivo |
| Acuse | 48 h después del envío | si no hay acuse, reenvío con el mismo asunto |
| Reintento | 2026-10-22 | segundo envío, con la misma dirección y asunto |
| Cierre | 2026-10-24 (G0) | si no hay respuesta, se documenta el silencio y se diseña para el caso conservador |

El caso conservador está definido de antemano para no tener que decidirlo con el reloj corriendo:

- `P1` sin respuesta: se ejecuta `T-01` tal como está escrito en `DOC-07` §3.
- `P2` sin respuesta: se asume que **los instrumentos cuentan** dentro del tope. El margen alcanza
  igual (`gestion/BOM.md`: US$1097.96 en ese escenario).
- `P3` sin respuesta: se asume que **cada equipo lleva sus transmisores** y se verifica la
  certificación japonesa antes de viajar.

`RSK-12` de `DOC-08` §3 cubre exactamente este escenario: sin respuesta al 2026-10-31, se documenta el
envío y se diseña para el caso conservador.

## Nota de coherencia

El paso 2 de DOC-02 §8.2, el criterio de paso de G0 y `RSK-12` hablan de «`P1`–`P3`», mientras que
este documento registra y envía también `P4`. No es una contradicción de fondo: `P4` viaja en el mismo
correo y no condiciona ninguna compuerta. Queda anotado porque un lector que compare los tres
documentos va a encontrar la diferencia.
