# 00 — Mapa de la propuesta de 4 páginas

| | |
| --- | --- |
| Artefacto | Planificación del entregable de 4 páginas. **No es la propuesta.** |
| Versión / fecha | 1.0 — 2026-10-14 |
| Estado | Esqueleto de planificación |
| Restricciones de las bases (`R9`) | 4 páginas, Times New Roman 12 pt, incluye BOM y carta del mentor; plazo 31-dic-2026, 23:59 GMT−10 |
| Se escribe en | 2026-12-22 (paso 9 de DOC-02 §8.2), después de la compuerta **G4** |

## Para qué sirve este archivo

El entregable son **4 páginas**. Todo lo que el repositorio produce no entra ahí y no tiene por qué
entrar: este archivo decide **qué ocupa cada página, de dónde sale y con qué figura**, para que la
redacción del 22-dic sea transcribir y recortar, no decidir.

Regla de lectura: cada fila de la tabla apunta a un documento del repositorio. Si una idea no tiene
documento de origen, no va a la propuesta.

## Presupuesto de líneas

Estimación de capacidad: A4, Times New Roman 12 pt, márgenes de 2.5 cm, interlineado simple →
**≈ 44 líneas de texto por página**, ≈ 176 líneas en total, descontando títulos y pies de figura.
El presupuesto se lleva por página y no por sección: cuando una sección se pasa, se recorta ahí
mismo.

| Página | Contenido | Documento de origen | Figura | IDs que se citan | Líneas |
| --- | --- | --- | --- | --- | --- |
| **1** | Título, equipo, mentor, institución. Resumen de 8 líneas. Problema ISAC: recepción reconfigurable con hardware mínimo. Vacío en la literatura: el ESPAR usado como receptor y el nulo hacia el iluminador como mecanismo de sensado. Objetivo y alcance declarado. | `N-02` §9 (vacío); `DOC-03` §1 (objeto y alcance); `DOC-09` §2 | Diagrama de arquitectura del sistema (bloque antena → ESP32 → interfaz), de `DOC-03` §2 | `R1`–`R9`, `DR-03`, `DR-16` | 44 |
| **2** | Arquitectura y decisiones. Los siete elementos y por qué siete (menor número con sectores regulares de 60° y simetría C6). Tabla de 4–5 decisiones con la alternativa descartada al lado. Geometría con las variables que se barren, no con cotas cerradas. | `DOC-03` §4 (DEC-01, DEC-02, DEC-04, DEC-07); `DOC-04` §3–§4 | Plano del arreglo con cotas (`DV-02`, `DV-03`, `DV-05`) y, si existe, foto de v1 | `DEC-01`, `DEC-02`, `DEC-04`, `DEC-07`, `DV-02`, `DV-03`, `DR-12` | 44 |
| **3** | Aplicación ISAC y verificación. Los tres modos y qué métrica produce cada uno. Libro de códigos: 20 estados en 5 bloques, no 64. Cómo se demuestra: los protocolos `T-02`–`T-06` con su tamaño de muestra y la banda de guarda de 3 dB. | `DOC-03` §6; `DOC-06` §4; `DOC-07` §2 y §4–§8; `N-03` §4 | Patrón de azimut medido de dos estados contrastados, o mapa estado → dirección si la medición no llegó | `A1`–`A5`, `T-02`–`T-06`, `DR-05`, `DR-06`, `DR-09`, `M-03`, `M-04` | 46 |
| **4** | Resultados medidos (o su rótulo de pendiente). Discusión: qué se logró, qué no y por qué. Límites aceptados explícitamente. Replicabilidad: BOM resumido en dos bloques y qué necesita otro grupo para repetirlo. Trabajo futuro. Referencias (6–10, las efectivamente leídas). | `DOC-07` §13 (tabla de estado); `DOC-08` §3 (riesgos aceptados); `gestion/BOM.md`; `N-02` §11 | Tabla de resultados `A1`–`A5` con valor medido, meta e incertidumbre; o el BOM resumido | `DR-11`, `DR-14`, `DR-16`, `T-08`, `T-10`, `RSK` aceptados | 42 |

Total: ≈ 176 líneas. No hay página 5 ni anexos: el BOM y la carta del mentor se adjuntan como
documentos separados, según `R9`.

## Criterios de recorte por página

| Página | Si hay que recortar | Nunca se recorta |
| --- | --- | --- |
| 1 | el resumen baja a 6 líneas; el contexto ISAC se reduce a dos frases | el vacío declarado: es el argumento de originalidad (`C1`) |
| 2 | la tabla de decisiones baja de 5 a 4 filas; la geometría pasa a texto | la columna «alternativa descartada»: una decisión sin alternativa es una preferencia |
| 3 | se sacan `T-07` y `T-09`; queda `T-02`–`T-06` | los tamaños de muestra y la banda de guarda |
| 4 | el trabajo futuro baja a tres bullets | el rótulo de «pendiente» de todo dato no medido |

## Qué no entra en 4 páginas y queda respaldado en el repositorio

| Queda afuera | Dónde vive | Por qué no entra |
| --- | --- | --- |
| Teoría del acoplamiento mutuo, carga reactiva y simetría C6 | `docs/teoria/01-fundamentos-espar.md` | 3–4 páginas de desarrollo; en la propuesta alcanza con una frase y la cita |
| Estado del arte completo y las 27 referencias | `docs/teoria/02-estado-del-arte.md` | la propuesta cita 6–10; el resto sostiene la evaluación de tecnologías |
| Presupuesto de incertidumbre de 3–4 dB y la regla `valor − 3 dB ≥ meta` | `docs/teoria/03-metricas-y-modelo.md` §4 | se usa para decidir los umbrales, no se explica en el texto |
| Matriz de trazabilidad completa `R → DR → A → T` | `docs/teoria/04-requisitos-y-trazabilidad.md` | es el respaldo de cada afirmación, no una figura |
| Las 14 órbitas y la demostración por Burnside de los 64 estados | `DOC-06` §3 | en la propuesta va solo «20 estados cargados en 5 bloques» |
| Procedimiento de ajuste con lima, tolerancias y registro de longitud real | `DOC-04` §6 | es lo que hace replicable el diseño, pero se demuestra con el repositorio |
| Cálculo completo de polarización: `R_limit`, choke, SRF, bypass, layout | `DOC-05` §2–§8 | en la propuesta va una frase y el valor de corriente |
| Los 10 protocolos de ensayo con procedimiento paso a paso | `DOC-07` | la propuesta reporta resultados; el protocolo es lo que los hace creíbles |
| Registro de 12 riesgos con disparador y compuerta | `DOC-08` §3 | se mencionan 2–3 límites aceptados, no el registro |
| Cronograma y compuertas G0–G5 | `gestion/cronograma.md` | es gestión interna |
| Delta completo contra DOC-02 (16 cambios) | `DOC-09` §2 | es historia del proyecto, no del diseño |
| Código del firmware, scripts de análisis y campañas crudas | `firmware/`, `software/`, `mediciones/` | se declara su existencia y su ubicación |

## Advertencia: la propuesta no se escribe antes de G4

**Este archivo planifica; no autoriza a redactar.** La propuesta se escribe el **2026-12-22**, después
de la compuerta **G4** de `DOC-08` §4, cuyo criterio de paso es «propuesta redactada con resultados
medidos y BOM cerrado».

Consecuencias que no se negocian al momento de escribir:

1. **Ningún dato sin medición.** Hoy la tabla de estado de `DOC-07` §13 marca los diez protocolos como
   «no ejecutado». Un valor que no esté en `mediciones/` se escribe como expectativa, con el protocolo
   que lo va a medir y la fecha. Nunca se presenta como resultado.
2. **Si G4 llega sin `A3` medido**, la propuesta lo dice y declara el plan; no se ajusta la meta al
   resultado. La regla de `DOC-07` §6 es explícita: un resultado honesto por debajo de la meta es mejor
   que una meta ajustada al resultado.
3. **La tabla de la página 4 se arma con la tabla de estado de `DOC-07` §13**, no con lo que el equipo
   recuerde de la campaña.
4. **Cada afirmación tiene que poder recorrerse** `R# → DR-## → A# → T-## → campaña`. Si no se recorre,
   se cae del texto, no se suaviza.

## Verificación de este mapa

| Qué | Cómo |
| --- | --- |
| El presupuesto de líneas cierra en 176 | al armar el borrador, contar líneas por página antes de compilar |
| Toda figura tiene documento de origen | cada figura de la tabla apunta a un documento; las que dependen de medición se marcan como pendientes de G2/G3 |
| Todo `DR` citado existe | comparar la columna de IDs contra `N-04` §3 |
| Nada de la columna «qué no entra» aparece en el texto | revisión final antes de G5 |
