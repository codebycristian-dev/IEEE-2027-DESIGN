# 03 — Metodología

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, sin redacción |
| Fuente principal | `docs/diseno/DOC-03-especificacion-de-diseno.md` §2 y §4 (arquitectura y decisiones) |
| Apoyo | `DOC-04` §3–§4, `DOC-05` §3–§6, `N-03` §4 (banda de guarda) |
| Ubicación y fecha | Página 2 y cierre de la página 3; se redacta el 2026-12-22, después de G4 |

## Objetivo del capítulo

Explicar cómo está construido el sistema y por qué cada elección se tomó frente a una alternativa
concreta. Es el capítulo que responde a «¿esto está diseñado o salió de una corazonada?».

## Qué va

- **Arquitectura en una figura y tres frases.** Monopolo activo central, seis parásitos en anillo, un
  PIN por parásito, seis GPIO del ESP32, un puerto SMA (`DOC-03` §2).
- **Por qué siete elementos.** Seis es el menor número que da sectores regulares de 60° con
  solapamiento y simetría rotacional exacta; cinco deja huecos y ocho rompe la simetría sin mejorar la
  cobertura (`DOC-03` DEC-04).
- **Cuatro decisiones con su alternativa descartada**, una por línea y con el motivo al lado:
  - Topología: parásitos conmutados con un puerto. Se descarta el arreglo de fase alimentado, la RIS de
    1 bit y la antena de píxeles; es la única que da control de patrón sin control de RF (DEC-01).
  - Interruptor: PIN SMP1345. Se descartan varactor, RF-MEMS y relé por restricción del mentor, tensión
    y tiempo de conmutación (DEC-02).
  - Adaptación: red L fija sobre el estado promedio. Se descarta no tener red, porque `A1` se vuelve
    inalcanzable (DEC-07).
  - Control: GPIO directo. Se descartan registro de desplazamiento y ULN2003 por piezas y latencia
    (DEC-08).
- **Geometría como variables, no como cotas.** Radio del anillo 22–34 mm (`DV-02`), plano de
  120/150/180 mm (`DV-03`), parásitos de 0.85–1.05 × `L_a` (`DV-04`), cada una con su criterio de
  cierre (`DOC-04` §3).
- **La electrónica en cinco números.** `R_limit` = 220 Ω, `I_diodo` = 10.9 mA, 65 mA con los seis
  encendidos, choque de 33 nH con autorresonancia fuera de banda, bypass de 470 pF C0G (`DOC-05`
  §3–§5).
- **Método de verificación y estatus del dato.** Todo criterio se evalúa con banda de guarda: se declara
  cumplido solo si `valor − 3 dB ≥ meta`, porque la incertidumbre es de 3–4 dB. Y todo número de
  `DOC-03`–`DOC-05` es hoy **de diseño**: pasa a verificado solo con campaña (`N-03` §4, `DOC-07` §13).

## Qué no va

- La teoría del ESPAR: acoplamiento mutuo, carga reactiva y las 14 órbitas (`docs/teoria/01-fundamentos-espar.md`).
- El plan de barrido con sus 27 corridas NEC2 (etapas A–C) y las siete reglas de layout de `DOC-05` §7:
  va una frase de cada uno. De las reglas, a la propuesta va una: la polarización por la cara inferior.
- Mediciones propias: no hay ninguna todavía. Si al 22-dic existe v1, el dato va al capítulo 05.

## Extensión prevista

Página 2 completa (**≈ 44 líneas**) más **≈ 6 líneas** de la página 3: arquitectura y figura 10, siete
elementos 5, decisiones 14, geometría 8, electrónica 7.

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada decisión cita su `DEC-##` y tiene alternativa descartada con motivo.
- [ ] Ninguna cota se presenta como final: todas son `DV-##` con rango y criterio de cierre.
- [ ] Los cinco números de electrónica coinciden con `DOC-05` §3–§5 al dígito.
- [ ] La banda de guarda de 3 dB aparece junto al criterio, no en una nota al pie.
- [ ] Todo valor no medido está rotulado como expectativa, con el protocolo que lo va a medir.
- [ ] Toda afirmación tiene un ID detrás (`DEC-##`, `DV-##`, `DR-##`) o una referencia de `N-02` §11.
