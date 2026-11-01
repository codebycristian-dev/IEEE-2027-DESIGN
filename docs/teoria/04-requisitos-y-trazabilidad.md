# N-04 — Requisitos y matriz de trazabilidad

Nota técnica de respaldo. Estado: vigente. Es la columna vertebral del repositorio: conecta las
bases del concurso con lo que se construye y con lo que se mide.

**Regla de oro:** ningún `DR` sin fuente, ningún `A` sin `DR`, ningún `T` sin `A`. Si un número de
la propuesta no se puede recorrer por esta cadena hasta una base o una medición, se cae.

## 1. Cadena de trazabilidad

```
R#   requisito de las bases           (DOC-01 tabla 2, tabla 7)
 └─ DR-##  requisito de diseño, verificable
     └─ A#  criterio de aceptación    (DOC-02 §7.1, refinados en DOC-03)
         └─ T-##  protocolo de ensayo (DOC-07)
             └─ mediciones/AAAA-MM-asunto/  datos
```

## 2. Requisitos de las bases

Reproducidos de DOC-01 para que esta nota se lea sola. La columna derecha es la implicación de
diseño y a qué `DR` da origen.

| `R#` | Requisito de las bases | Implicación | Da origen a |
| --- | --- | --- | --- |
| R1 | El hardware opera estrictamente como receptor | el sistema no transmite; verificable con SDR | DR-02 |
| R2 | Iluminadores: transmisores comerciales sin modificar (Wi-Fi, Bluetooth, hotspot) | no se controla modulación, canal ni potencia; el diseño se valida con RSSI real | DR-01 |
| R3 | Modo sensado: detectar movimiento o posición | barrido de estados y métrica de actividad por dirección | DR-05, DR-09 |
| R4 | Modo comunicación: haz hacia el TX deseado y supresión del interferente | relación delante/detrás y nulos utilizables | DR-03, DR-04, DR-05, DR-06 |
| R5 | Cambio dinámico entre modos, controlado por software | conmutación rápida y secuencias definidas | DR-07, DR-08, DR-17 |
| R6 | Métricas en tiempo real, fáciles de visualizar | interfaz gráfica y/o indicadores en la antena | DR-10, DR-17 |
| R7 | Costo total del sistema < US$1500 | incluye software comercial sin licencia universitaria | DR-11 |
| R8 | Reproducible en aula; teoría simple; instrucciones paso a paso | pocos componentes, fabricación accesible | DR-12, DR-13 |
| R9 | Propuesta de 4 páginas, Times New Roman 12 pt, BOM, carta del mentor; 31-dic-2026 | requiere resultados preliminares medidos | DR-15 |

## 3. Requisitos de diseño

| `DR` | Requisito verificable | Fuente | Criterio | Protocolo |
| --- | --- | --- | --- | --- |
| DR-01 | Opera en 2400–2483.5 MHz con `\|S11\| ≤ −10 dB` en todos los estados del subconjunto útil | R2, D-02 | **A1** | T-02 |
| DR-02 | El sistema no emite RF detectable: ninguna señal atribuible al sistema por encima de −80 dBm en 2.4 GHz | R1 | — | T-01 |
| DR-03 | Cobertura de 360° en azimut con 6 sectores conmutables | R4 | — | T-03 |
| DR-04 | Relación delante/detrás ≥ 10 dB en cada uno de los 6 sectores | R4 | **A2** | T-03 |
| DR-05 | Profundidad de nulo ≥ 10 dB en la dirección del iluminador mientras el haz apunta al TX deseado, con separación ≥ 90° entre ambos | R3, R4 | — | T-04 |
| DR-06 | Mejora de SIR ≥ 10 dB respecto del estado omnidireccional, con TX e interferente separados ≥ 90° | R4 | **A3** | T-04 |
| DR-07 | Tiempo de conmutación extremo a extremo < 1 ms | R5 | **A4** | T-05 |
| DR-08 | Cambio de modo comunicación↔sensado dentro de un intervalo entre paquetes (≤ 10 ms) | R5 | — | T-05 |
| DR-09 | Detección de movimiento: sector correcto en ≥ 8 de 10 ensayos con una persona caminando a 1–3 m | R3 | **A5** | T-06 |
| DR-10 | Métricas de SIR y de actividad visibles con refresco ≤ 1 s | R6 | — | T-07 |
| DR-11 | Costo total del sistema < US$1500 con precios fechados; instrumentos de desarrollo declarados aparte | R7 | — | T-08 |
| DR-12 | Replicable: ≤ 25 tipos de componente distintos, sin PCB multicapa, sin ajuste crítico por unidad; montaje desde cero ≤ 30 min | R8 | — | T-09 |
| DR-13 | Seguro: alimentación ≤ 5 V CC, sin tensiones peligrosas, sin partes cortantes expuestas | R8 | — | T-09 |
| DR-14 | Rearmable para transporte en ≤ 10 min, sin piezas sueltas que se puedan perder | C3.3 | — | T-09 |
| DR-15 | Todo `DR` tiene su `A`, su `T` y sus datos; la propuesta se sostiene sobre este repositorio | R9 | — | revisión documental |
| DR-16 | Explicabilidad: tras la demo, un no especialista describe qué hace y por qué en ≤ 60 s | C4.1 | — | T-10 |
| DR-17 | Control por software con interfaz gráfica: el operador elige modo y el sistema elige estado | R5, R6 | — | T-07 |
| DR-18 | Libro de códigos cerrado y reproducible: los estados cargados en el firmware son exactamente los documentados, ≤ 25 | C2.4 | — | T-03 |

`C#` refiere a los criterios de evaluación del concurso (DOC-01 §3.2), no a las bases. Se incluyen
porque los criterios también imponen requisitos verificables.

## 4. Criterios de aceptación y su alcance

Los cinco criterios de DOC-02 §7.1 se conservan con la misma numeración **y se precisa su alcance**.
El refinamiento se justifica en `DOC-09`.

| `A#` | Enunciado vigente | Cambio respecto de DOC-02 |
| --- | --- | --- |
| A1 | `\|S11\| ≤ −10 dB` en 2400–2483.5 MHz en **todos los estados del subconjunto útil** (≤ 25) | DOC-02 decía «todas las configuraciones del libro de códigos»; se acota al subconjunto cargado y se agrega la exigencia de red de adaptación |
| A2 | Relación delante/detrás ≥ 10 dB **en cada sector** | se mantiene, se define la métrica (M-03) |
| A3 | Mejora de SIR ≥ 10 dB con TX deseado e interferente separados ≥ 90° **respecto del estado omnidireccional** | se agrega la referencia explícita; antes no decía contra qué se compara |
| A4 | Tiempo de conmutación extremo a extremo < 1 ms, **medido en el pin de monitoreo** | se agrega el método; el firmware no se autovalida |
| A5 | Detección de movimiento con sector correcto en 1–3 m, **≥ 8 de 10 ensayos** | se agrega el criterio numérico |

Además, todo criterio se evalúa con la banda de guarda de `N-03` §4: `valor − 3 dB ≥ meta`.

## 5. Matriz de cobertura

### Bases → requisitos de diseño

| `R#` | Cubierto por | Estado |
| --- | --- | --- |
| R1 | DR-02 | diseñado, ensayo T-01 definido |
| R2 | DR-01 | diseñado, ensayo T-02 definido |
| R3 | DR-05, DR-09 | diseñado, ensayos T-04 y T-06 definidos |
| R4 | DR-03, DR-04, DR-05, DR-06 | diseñado, ensayos T-03 y T-04 definidos |
| R5 | DR-07, DR-08, DR-17 | diseñado, ensayo T-05 definido |
| R6 | DR-10, DR-17 | diseñado, ensayo T-07 definido |
| R7 | DR-11 | estimado; se cierra al comprar (`gestion/BOM.md`) |
| R8 | DR-12, DR-13 | diseñado, ensayo T-09 definido |
| R9 | DR-15 | en curso: este repositorio |

Ningún `R#` queda sin cubrir. Eso es lo que la propuesta puede afirmar hoy; **ningún `DR` tiene
todavía datos**, porque no hay prototipo. La columna honesta hoy es «diseñado», no «verificado».

### Requisitos de diseño → criterio → protocolo

| `DR` | `A#` | `T##` | Datos |
| --- | --- | --- | --- |
| DR-01 | A1 | T-02 | pendiente (prototipo v1) |
| DR-04 | A2 | T-03 | pendiente (prototipo v0) |
| DR-06 | A3 | T-04 | pendiente (prototipo v1) |
| DR-07 | A4 | T-05 | pendiente (prototipo v1) |
| DR-09 | A5 | T-06 | pendiente (prototipo v1) |

## 6. Requisitos deliberadamente no adoptados

Queda registrado para que la decisión no se reabra por olvido:

| No adoptado | Motivo |
| --- | --- |
| Reconfiguración de polarización | requiere un segundo conjunto de parásitos ortogonales; duplica diodos y líneas de polarización. Queda como extensión posterior (DOC-02 §7.2) |
| Control de haz en elevación | no lo piden las bases; el montaje con falda lo mejoraría pero agrega piezas a la demo |
| Operación simultánea estricta | `R5` la marca como opcional; se implementa alternancia por paquete, que es medible con `T-05` |
| Transmisión de cualquier tipo | prohibida por `R1` |
| Varactores en el prototipo base | la restricción del mentor fija PIN; los varactores son extensión condicionada a que falle `A3` |

## 7. Requisitos que dependen de respuesta de los organizadores

| `P#` | Requisito afectado | Qué cambia si la respuesta es negativa |
| --- | --- | --- |
| P1 | DR-02 | si hay que documentar de otra forma la operación como receptor, cambia el protocolo `T-01`, no el diseño |
| P2 | DR-11 | si los instrumentos de desarrollo cuentan en el tope, el ESP32 y el VNA entran en la BOM y hay que recortar el resto |
| P3 | DR-06 | si cada equipo lleva sus propios TX a Kioto, hay que verificar certificación japonesa y sumarla a la BOM |
| P4 | ninguno vigente | **no bloqueante**: solo era relevante si se elegía RIS, descartada en DOC-02 §7. Se envía igual para dejar constancia escrita de cómo los organizadores leen «antena receptora», que es el criterio que respalda DR-03 |

Están registradas en `gestion/preguntas-organizadores.md` con su fecha de envío.

## 8. Cómo se cambia un requisito

1. No se edita un `DR` vigente en silencio. Se agrega una fila nueva con el siguiente número y se
   marca la anterior como «reemplazado por `DR-##`».
2. Si el cambio nace de una respuesta de los organizadores o del mentor, se registra la fecha y la
   fuente en la fila.
3. Si el cambio afecta un `A#`, se actualiza la tabla §4 y el protocolo en `DOC-07` en el mismo
   commit.
4. Si el cambio invalida una compuerta de `DOC-08`, se revisa la compuerta antes de seguir.
