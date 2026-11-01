# N-03 — Métricas, modelo y presupuesto de incertidumbre

Nota técnica de respaldo. Estado: vigente. Define **cómo se calcula cada número** que aparece en
`DOC-07` y en la propuesta, y cuánto puede equivocarse. Sin esta nota, un resultado medido no es
un resultado: es una observación.

## 1. Catálogo de métricas

Cada métrica tiene un identificador, una definición cerrada y un criterio de aceptación asociado.

### M-01 — Adaptación de entrada (alimenta `A1`)

El coeficiente de reflexión en el plano del conector:

```
Γ = (Z_in − Z0) / (Z_in + Z0)        |S11| [dB] = 20 · log10(|Γ|)
VSWR = (1 + |Γ|) / (1 − |Γ|)
```

La máscara de −10 dB equivale a VSWR ≤ 1.92:1. Se evalúa **estado por estado** y sobre la banda
completa 2400–2483.5 MHz, no en un punto. El criterio es de máscara: el peor punto de la banda, en
el peor estado del subconjunto útil, tiene que cumplir.

**Por qué estado por estado:** el monopolo activo ve una impedancia mutua distinta según qué
parásitos estén cortocircuitados. Un diseño que solo se mide en el estado omnidireccional está
midiendo el caso más fácil.

### M-02 — Patrón de azimut normalizado (alimenta `A2`)

Potencia recibida en función del ángulo de la plataforma giratoria, normalizada al máximo de la
vuelta, para un estado fijo:

```
P_norm(φ_k) = P(φ_k) − max_k P(φ_k)      [dB]
```

Se reporta con pasos de 5° (72 puntos) y con el número de paquetes promediados por punto.

### M-03 — Relación delante/detrás por sector (alimenta `A2`)

```
F/B_s = max{ P(φ) : φ ∈ sector_s } − max{ P(φ) : φ ∈ sector_opuesto(s) }
```

**Decisión de definición:** se define por el máximo de cada mitad, no por el valor en el eje. Un
sector de 60° tiene ancho; usar un solo punto hace que la métrica dependa de la alineación
mecánica. Esta definición es la que se declara en la propuesta.

### M-04 — SIR y su mejora (alimenta `A3`)

Con dos transmisores comerciales identificados por MAC:

```
SIR_estado = RSSI_deseado − RSSI_interferente        [dB]
ΔSIR = SIR_estado_optimo − SIR_omni
```

La mejora se mide contra el estado omnidireccional (`K0`), no contra una antena externa. Razón: lo
que la propuesta promete es que **la reconfiguración** aporta la mejora, no que un monopolo sea
mejor o peor que otra antena.

### M-05 — Profundidad de nulo

```
N_d = max_φ P(φ) − P(φ_d)
```

Se reporta en la dirección objetivo `φ_d` con la resolución angular de la vuelta (5°). La
profundidad que importa para ISAC no es la máxima alcanzable, sino la que se logra **con el haz
apuntando al TX deseado**: esa es la que se publica.

### M-06 — Tiempo de conmutación (alimenta `A4`)

```
t_sw = t( señal estable en ±1 dB ) − t( flanco de comando )
```

Se mide con un pin de monitoreo que replica la señal de control y la traza temporal del receptor,
no con el reloj del firmware: el firmware mide su propia intención, no el efecto físico.

### M-07 — Detección de movimiento (alimenta `A5`)

```
actividad_s = varianza temporal de RSSI en el sector s, ventana W
detección    = sector con máxima actividad_s
acierto      = ( sector detectado == sector real )
```

La tasa de acierto se reporta por sector y en total. Detalle del umbral en `DOC-07` §6.

## 2. Modelo de enlace para interpretar RSSI

Para verificar que las cifras medidas son físicamente razonables:

```
P_rx[dBm] = P_tx + G_tx + G_rx − FSPL − L_misc
FSPL[dB] = 20·log10(d_km) + 20·log10(f_MHz) + 32.44
```

A 1 m y 2440 MHz: `FSPL = 20·log10(0.001) + 20·log10(2440) + 32.44 ≈ −60 + 67.7 + 32.4 = 40.1 dB`.

Sirve para una sola cosa: **detectar un error de medición por orden de magnitud**. Si el ΔSIR
medido es negativo en el estado que debería apuntar al TX deseado, hay un error de montaje o de
etiquetado, no un hallazgo.

## 3. Resolución y ruido del receptor ESP32

| Efecto | Magnitud | Consecuencia |
| --- | --- | --- |
| Cuantización de RSSI | 1 dB (entero) | piso de resolución por paquete |
| Variación por multitrayecto | 3–8 dB entre paquetes | promedio obligatorio |
| Ruido de estimación | ~1–2 dB | promedio de N paquetes |

Con `N = 30` paquetes por punto, el error estándar de la media baja a ≈ 0.2–0.4 dB si las muestras
son independientes. **No siempre lo son**: con el receptor quieto y un TX fijo, las muestras están
correlacionadas y el promedio subestima la incertidumbre. Mitigación adoptada: promediar sobre
`N = 30` y **reportar también la desviación estándar** de la ventana. Si `σ > 2 dB`, el punto se
repite.

Lo que **no** se puede hacer con RSSI entero es resolver diferencias menores a 1 dB. Por eso todas
las métricas críticas (`M-03`, `M-04`) son **diferencias de dos medidas del mismo receptor**: el
sesgo de cuantización se cancela y la incertidumbre diferencial queda del orden de 0.3 dB.

## 4. Presupuesto de incertidumbre

Contribuciones estimadas para una medición de patrón con ESP32 (presupuesto tipo B, `k = 1`):

| Fuente | Contribución | Cómo se controla |
| --- | --- | --- |
| Cuantización de RSSI promediada | 0.3 dB | N = 30, reporte de σ |
| Repetibilidad del conector / calibración del VNA | 0.1–0.2 dB en `|S11|` | calibración SOL antes de cada sesión |
| Repetibilidad angular de la plataforma | ±2° | marcado de cero y tope mecánico por vuelta |
| Inclinación del patrón con el ángulo de elevación | 1–2 dB en el borde del haz | altura fija del TX y RX documentada |
| Multitrayecto del entorno | **2–3 dB** | medir en dos posiciones del aula y reportar la dispersión |
| Deriva de potencia del TX comercial | 1 dB | TX fijo, no se toca entre medidas comparadas |
| Proximidad del operador | hasta 3 dB | operador a > 1.5 m y siempre del mismo lado |

**Término dominante: el entorno, no el instrumento.** La incertidumbre combinada es del orden de
**3–4 dB (k = 1)**. Este número tiene una consecuencia directa sobre los criterios:

> Regla de banda de guarda: una medida se declara «cumple» solo si `valor − U ≥ meta` con
> `U = 3 dB`. Un `A3` medido en 10.0 dB **no cumple**; uno medido en 13 dB o más sí.

Se prefiere declarar esto ahora antes que defender un 10.0 dB justo en el borde en la revisión de
la propuesta.

## 5. Reglas de registro

Toda medición guarda, junto con los datos:

- identificador de campaña, fecha y hora de inicio y fin;
- instrumento y versión de firmware, más el archivo de calibración usado;
- distancia, altura y orientación de TX y RX, y posición dentro del aula;
- temperatura y humedad si están disponibles;
- qué `T-##` se ejecutó y qué se esperaba encontrar;
- operador.

Esto no es burocracia: sin el archivo de calibración, un barrido de `S11` no es reproducible, y sin
la posición, un patrón no es comparable con el de la campaña anterior.

## 6. Lo que este proyecto no mide

Declararlo ahora evita prometer de más:

| Magnitud | Por qué no |
| --- | --- |
| Ganancia absoluta en dBi | requiere cámara anecoica o método de comparación con antena patrón calibrada |
| Eficiencia de radiación | requiere calorimetría o cámara de reverberación |
| Polarización cruzada | requiere enlace con polarización controlada en ambos extremos |
| Patrón en elevación | la plataforma gira en azimut; el corte de elevación se obtiene con un soporte manual y se reporta como indicativo |

Todas las cifras de ganancia que aparezcan en la propuesta son **relativas** (respecto del monopolo
solo o respecto del estado omnidireccional), y así se rotulan. `N-01` §6 fija esas expectativas.

## 7. Relación con los criterios de aceptación

| Métrica | Criterio | Protocolo |
| --- | --- | --- |
| M-01 | `A1` | `T-02` |
| M-02, M-03 | `A2` | `T-03` |
| M-04 | `A3` | `T-04` |
| M-06 | `A4` | `T-05` |
| M-07 | `A5` | `T-06` |

La matriz completa, con requisitos de origen, está en
[`04-requisitos-y-trazabilidad.md`](04-requisitos-y-trazabilidad.md).
