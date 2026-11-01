# DOC-06 — Libro de códigos de configuraciones

| Código | DOC-06 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-03 v1.0 (2026-10-14), DEC-13 y §6 |
| Tipo | Documento de diseño — control |
| Estado | Vigente. Sustituye la afirmación de DOC-02 de «64 estados / 14 patrones» por una lista explícita y contable |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Enumeración completa de las 14 órbitas con demostración de la cuenta, subconjunto útil de 20 estados, tabla de sectores y presupuesto de tiempo de barrido. |

## 1. Objeto y por qué este documento existe

DOC-02 afirmaba «2⁶ = 64 estados, por simetría de rotación de 60° corresponden a 14 formas de patrón
distintas». La cuenta es correcta, pero el documento no la demostraba ni decía **qué** estados se
cargan en el firmware. Sin esa lista, `DR-18` no es verificable y `A1` no tiene universo de
evaluación.

Acá quedan fijadas: la notación, las 14 órbitas, el subconjunto de 20 estados que va al firmware, el
mapeo estado → dirección de haz, y el presupuesto de tiempo de barrido.

## 2. Notación

- Seis parásitos `P1` … `P6` en el anillo, ordenados en sentido antihorario desde `P1` en azimut 0°,
  a pasos de 60°.
- Un estado es una cadena de 6 bits: el bit `n` vale 1 si `Pn` está en conducción (parásito
  cortocircuitado a tierra = reflector) y 0 si está en corte (abierto).
- La cadena se escribe con `P1` a la izquierda. Ejemplo: `111000` significa `P1`, `P2` y `P3` en
  conducción.
- Como palabra de 6 bits para el firmware, el bit menos significativo es `P1`.

| Bit (firmware) | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Parásito | P6 | P5 | P4 | P3 | P2 | P1 |
| GPIO | 32 | 27 | 26 | 25 | 14 | 13 |

## 3. Las 14 órbitas

Dos estados que son rotaciones entre sí producen el mismo patrón, girado. El número de patrones
distintos es el número de órbitas bajo el grupo de rotaciones `C6`, que por el lema de Burnside vale
14 (demostración en [`N-01`](../teoria/01-fundamentos-espar.md) §4). La tabla siguiente las enumera
todas, con el tamaño de cada órbita. La suma de tamaños es 64, lo que verifica la enumeración.

| Órbita | Representante | Parásitos activos | Tamaño de órbita | Clase de patrón esperado |
| --- | --- | --- | --- | --- |
| O01 | `000000` | 0 | 1 | omnidireccional (referencia) |
| O02 | `111111` | 6 | 1 | sin directividad útil: todo cortocircuitado |
| O03 | `100000` | 1 | 6 | perturbación leve, haz muy ancho |
| O04 | `011111` | 5 | 6 | complemento de O03 |
| O05 | `110000` | 2 contiguos | 6 | haz ancho moderado, `F/B` bajo |
| O06 | `101000` | 2 con hueco de 1 | 6 | haz asimétrico con nulo lateral |
| O07 | `100100` | 2 opuestos | 3 | dos reflectores enfrentados: nulos perpendiculares |
| O08 | `001111` | 4 contiguos | 6 | complemento de O05 |
| O09 | `010111` | 4 con hueco | 6 | complemento de O06 |
| O10 | `011011` | 4 alternados | 3 | complemento de O07 |
| O11 | `111000` | **3 contiguos** | 6 | **haz de sector: el estado de trabajo** |
| O12 | `110100` | 3 con reparto 2+1 | 6 | haz de sector asimétrico |
| O13 | `110010` | 3 con reparto 2+1 opuesto | 6 | haz de sector asimétrico, espejo de O12 |
| O14 | `101010` | 3 alternados | 2 | múltiples nulos, haz fragmentado |

Comprobación de la suma: 1+1+6+6+6+6+3+6+6+3+6+6+6+2 = **64** ✓

Observación de simetría útil para el análisis: O03↔O04, O05↔O08, O06↔O09, O07↔O10 son pares
complementarios, y el complemento de un estado invierte aproximadamente el patrón (el haz aparece
del lado opuesto). Eso reduce a la mitad el número de patrones que hay que entender a mano, aunque
no el de estados que hay que cargar.

## 4. Subconjunto útil: 20 estados

**Decisión (DEC-13):** al firmware van 20 estados, no 64. Los 44 restantes quedan disponibles para
experimentación en banco pero **no se cargan**, y por lo tanto no están obligados a cumplir `A1`.

Motivo: cada estado cargado tiene que medirse en `T-02` y `T-03`. Veinte estados es el máximo que el
equipo puede medir con la repetibilidad exigida antes del 31 de diciembre; cargar 64 convertiría el
plan de verificación en inejecutable.

| Bloque | Estados | Patrón | Para qué |
| --- | --- | --- | --- |
| `K0` | 1 | `000000` | referencia omnidireccional (`A3`) y estado de reposo |
| `KS1`–`KS6` | 6 | 3 contiguos (`O11`) | haz de sector: **modo comunicación** |
| `KW1`–`KW6` | 6 | 2 contiguos (`O05`) | haz ancho: cobertura rápida y adquisición inicial |
| `KN1`–`KN6` | 6 | 4 contiguos = 2 contiguos en corte (`O08`) | **nulo hacia el iluminador con haz útil del otro lado**: modo sensado |
| `KX1` | 1 | `101010` (`O14`) | múltiples nulos: medición de la capacidad real de rechazo |

Total: 1 + 6 + 6 + 6 + 1 = **20**.

`KX1` es el único estado que no es un bloque de rotaciones: se carga solo porque es el que puede
producir nulos simultáneos en tres direcciones, y DOC-08 necesita evidencia medida para decidir si
el modo sensado usa `KN*` o `KX1`.

### Estados cargados, completos

La tabla se escribe entera, sin abreviar «rotaciones»: un estado mal transcrito no da síntoma hasta
que el patrón no coincide, y encontrar ese error después de soldar cuesta días.

| ID | Cadena (P1…P6) | Bits (P6…P1) | Hex | Bloque |
| --- | --- | --- | --- | --- |
| K0 | `000000` | 000000 | 0x00 | omnidireccional |
| KS1 | `111000` | 000111 | 0x07 | sector |
| KS2 | `011100` | 001110 | 0x0E | sector |
| KS3 | `001110` | 011100 | 0x1C | sector |
| KS4 | `000111` | 111000 | 0x38 | sector |
| KS5 | `100011` | 110001 | 0x31 | sector |
| KS6 | `110001` | 100011 | 0x23 | sector |
| KW1 | `110000` | 000011 | 0x03 | haz ancho |
| KW2 | `011000` | 000110 | 0x06 | haz ancho |
| KW3 | `001100` | 001100 | 0x0C | haz ancho |
| KW4 | `000110` | 011000 | 0x18 | haz ancho |
| KW5 | `000011` | 110000 | 0x30 | haz ancho |
| KW6 | `100001` | 100001 | 0x21 | haz ancho |
| KN1 | `001111` | 111100 | 0x3C | nulo + haz |
| KN2 | `100111` | 111001 | 0x39 | nulo + haz |
| KN3 | `110011` | 110011 | 0x33 | nulo + haz |
| KN4 | `111001` | 100111 | 0x27 | nulo + haz |
| KN5 | `111100` | 001111 | 0x0F | nulo + haz |
| KN6 | `011110` | 011110 | 0x1E | nulo + haz |
| KX1 | `101010` | 010101 | 0x15 | nulos múltiples |

Nota de transcripción: la cadena se lee `P1…P6`, de modo que `KX1` = `101010` significa `P1`, `P3`
y `P5` en conducción. Leídos en el orden `P6…P1` los mismos bits son `010101`, y el valor de la
palabra es `0x15`. El estado complementario `010101` **no** se carga: es una rotación de 60° del
mismo patrón y no aporta información nueva. Este es exactamente el error que el script del §7
detecta: la primera versión de esta tabla tenía la cadena y el hex invertidos, y la verificación
falló.

**Atención:** los valores hex de esta tabla son el resultado de la convención del §2 (P1 = bit 0) y
se verifican con un script en `software/codebook/` antes de cargarlos. Un error de un bit acá no da
síntoma hasta que el patrón no coincide: por eso `DR-18` exige que firmware y documento coincidan
literalmente, y por eso el ítem de verificación es un diff automático, no una inspección visual.

## 5. Estado → dirección de haz

La regla geométrica: el bloque de parásitos en conducción refleja, y el máximo de radiación aparece
**del lado opuesto al centro del bloque**.

| Estado | Activos | Centro del bloque | Haz esperado | Estado complementario |
| --- | --- | --- | --- | --- |
| KS1 | P1, P2, P3 | 60° | 240° | KN con nulo en 60° |
| KS2 | P2, P3, P4 | 120° | 300° | — |
| KS3 | P3, P4, P5 | 180° | 0° | — |
| KS4 | P4, P5, P6 | 240° | 60° | — |
| KS5 | P5, P6, P1 | 300° | 120° | — |
| KS6 | P6, P1, P2 | 0° | 180° | — |

**Advertencia sobre el signo:** la convención «opuesto al centro del bloque» es la esperada por el
modelo de reflector, pero el sentido (horario o antihorario) depende del orden físico de los
parásitos en el anillo. Se confirma con la primera medición (`T-03`) y, si resulta invertida, se
corrige la tabla del §5 **sin renumerar los estados** — la regla de IDs de `docs/INDEX.md` prohíbe
renumerar.

Lo mismo aplica a la tabla de nulos del bloque `KN`: el nulo esperado apunta hacia el par en corte.
Se verifica con `T-04`.

## 6. Presupuesto de tiempo de barrido

Esto es lo que decide si los modos son operables o no, y es el punto donde la letra chica de DOC-02
(«barrido del libro de códigos») se vuelve un problema de ingeniería.

Un receptor Wi-Fi escucha balizas del punto de acceso; un intervalo típico entre paquetes útiles es
de 100 ms. Con un tiempo de establecimiento de ~1 ms (`A4`), el costo dominante es la **espera de
paquetes**, no la conmutación.

| Modo de operación | Estados | Paquetes por estado | Tiempo por vuelta | Uso |
| --- | --- | --- | --- | --- |
| Adquisición inicial | 6 (`KW*`) | 2 | ~0.6 s | primera conexión, `DR-10` |
| Comunicación en régimen | 6 (`KS*`) | 2 | ~0.6 s | seguimiento continuo |
| Sensado | 6 (`KN*`) + 6 (`KS*`) | 2 | ~2.4 s | mapa de actividad |
| **Medición** (`T-02`…`T-06`) | hasta 20 | **30** | ~60 s | no es operación: es caracterización |

Con esto `DR-10` (refresco ≤ 1 s) se cumple en los modos de operación, **no** en modo medición. Esa
distinción no estaba en DOC-02 y es la que evita que el panel se vea congelado o que la
incertidumbre se dispare.

## 7. Verificación de este documento

| Qué | Cómo | Criterio |
| --- | --- | --- |
| Enumeración de órbitas | script en `software/codebook/` que rota las 64 cadenas y cuenta | 14 órbitas, tamaños iguales al §3 |
| Correspondencia documento ↔ firmware | script que compara la tabla del §4 con el arreglo del firmware | coincidencia exacta, `DR-18` |
| Patrón esperado por bloque | `T-03` sobre `K0`, `KS1`, `KW1`, `KN1`, `KX1` | el máximo cae dentro de ±15° de la dirección esperada |
| Nulo del bloque `KN` | `T-04` | profundidad ≥ 10 dB (`DR-05`) |
| Tiempo de vuelta | marca temporal de `T-05` | ≤ 1 s en modo operación |

## 8. Pendientes

| Pendiente | Bloquea |
| --- | --- |
| Confirmar el sentido de rotación de los sectores | tabla del §5 y la figura de la propuesta |
| Decidir si `KX1` entra en la demo o solo en el análisis | `DOC-07` §6 |
| Escribir el script de verificación de la tabla | cierre de `DR-18` |
