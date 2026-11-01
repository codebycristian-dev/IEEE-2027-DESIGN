# DOC-05 — Circuito de control y polarización de los diodos PIN

| Código | DOC-05 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-03 v1.0 (2026-10-14), §5 y DEC-06, DEC-08, DEC-09 |
| Tipo | Documento de diseño — electrónica |
| Estado | Vigente. Valores de partida calculados; a confirmar en banco con `T-05` y la medición del choque |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Primera versión: punto de operación, topología de polarización, criterios de RF, tiempo de conmutación estimado y reglas de layout. |

## 1. Objeto

Diseñar la célula que conmuta cada parásito. Es la parte del proyecto donde los errores **no se ven
en la simulación**: una línea de polarización mal ruteada cambia el patrón, y un punto de operación
mal elegido quema el diodo o degrada la conmutación. DOC-02 mencionaba «6 redes de polarización
(resistencia + bobina de bloqueo)» sin un solo número; acá están los números.

## 2. Topología de la célula

Una célula por parásito, seis idénticas:

```
   GPIO ──[ R_limit ]──┬──[ L_choke ]──┬── base del parásito
                       │               │
                    [ C_bypass ]     [ PIN ]
                       │               │
                      GND             GND

   Además, en el lado del GPIO:  [ R_pd 10 kΩ ] a GND  (estado definido durante el arranque)
```

Tres elementos cumplen tres funciones distintas y no son intercambiables:

| Elemento | Función | Si se omite |
| --- | --- | --- |
| `R_limit` | fija la corriente de conducción | corriente no controlada: el GPIO y el diodo quedan expuestos |
| `L_choke` | impide que la RF baje por la línea de continua | la línea se vuelve parte de la antena y el patrón deja de coincidir con el diseño |
| `C_bypass` | devuelve a tierra la RF residual del lado del GPIO | la RF llega al microcontrolador y aparece ruido en la conmutación |
| `R_pd` | garantiza el estado «abierto» mientras el ESP32 arranca | la antena tiene un estado indefinido durante el arranque, y `T-05` no es repetible |

## 3. Punto de operación

Datos de partida del SMP1345 [9]: `V_f ≈ 0.9 V` a 10 mA, `R_s ≈ 1.5 Ω`, `C_j ≈ 0.18 pF` en corte.
**`V_f` y el tiempo de conmutación se miden en banco y se corrigen acá** — la hoja de datos da curvas,
no un valor único.

Con alimentación de 3.3 V del devkit:

```
I = (3.3 V − 0.9 V) / R_limit
```

| `R_limit` | `I_diodo` | Potencia en R | Potencia en el diodo | Comentario |
| --- | --- | --- | --- | --- |
| 470 Ω | 5.1 mA | 12 mW | 4.6 mW | menos consumo, pero `R_s` sube y aumenta la pérdida de inserción |
| **220 Ω** | **10.9 mA** | **26 mW** | **9.8 mW** | **elegido**: es el punto donde la hoja de datos especifica `R_s = 1.5 Ω` |
| 150 Ω | 16.0 mA | 38 mW | 14.4 mW | innecesario; acerca el GPIO a su límite recomendado |

Presupuesto agregado, con los seis diodos encendidos a la vez (el peor caso, y el que conviene
soportar sin degradación):

| Magnitud | Valor | Límite |
| --- | --- | --- |
| Corriente total de polarización | 6 × 10.9 mA = **65 mA** | puerto USB 500 mA |
| Corriente por GPIO | 10.9 mA | 40 mA absoluto, 20 mA recomendado |
| Disipación total en resistencias | 6 × 26 mW = 0.16 W | — |
| Encapsulado de `R_limit` | 0603 (0.1 W) admite 26 mW con margen 4× | — |

**Decisión:** 220 Ω, 0603, 1 %. La tolerancia importa poco para la corriente (±1 %) pero se especifica
igual para que el BOM sea inequívoco.

## 4. Choque de RF

Requisito: `|Z_choke| ≥ 300 Ω` a 2441.75 MHz, con la impedancia **medida en el montaje real**, no la
del catálogo.

| Candidato | `|X_L|` a 2.44 GHz | Frecuencia de autorresonancia típica | Veredicto |
| --- | --- | --- | --- |
| 18 nH 0402 | 276 Ω | ≈ 5 GHz | insuficiente solo; aceptable en serie con otro |
| 27 nH 0603 | 414 Ω | ≈ 3.5 GHz | aceptable, con margen sobre la SRF |
| **33 nH 0603** | **506 Ω** | **≈ 2.8 GHz** | **elegido**: cumple y mantiene la SRF por encima de la banda |
| 39 nH 0603 | 598 Ω | ≈ 2.4–2.6 GHz | descartado: la SRF cae **dentro** de la banda y la impedancia se derrumba |

El detalle del 39 nH es el tipo de error que arruina un ESPAR sin que nadie lo note: a la frecuencia
de autorresonancia el inductor deja de ser inductivo y pasa a comportarse como un cortocircuito
capacitivo, con lo cual la línea de polarización se convierte en una antena parásita más. Por eso el
criterio no es «cuanto más grande, mejor» sino «grande y con la SRF fuera de banda».

**Verificación obligatoria:** medir `|Z|` del choque montado con el VNA (una puerta, con el diodo
desmontado) y registrar la curva en `mediciones/`. Si a 2.44 GHz la impedancia medida baja de
300 Ω, se reemplaza por dos inductores en serie (15 nH + 18 nH) que reparten la autorresonancia.

## 5. Capacitor de bypass

Criterio: impedancia despreciable a la frecuencia de trabajo, sin robar corriente continua.

| `C_bypass` | `|X_C|` a 2.44 GHz | Constante de tiempo con `R_limit` = 220 Ω |
| --- | --- | --- |
| 100 pF | 0.65 Ω | 22 ns |
| **470 pF** | **0.14 Ω** | **103 ns** |
| 1 nF | 0.065 Ω | 220 ns |

Se elige **470 pF, 0603, C0G** (no X7R: la clase 2 tiene pérdidas y deriva con la tensión). Con
`L_choke = 33 nH` el filtro pasa-bajos resultante corta en ≈ 40 MHz, suficiente para que nada de RF
llegue al GPIO y suficientemente alto para no afectar `A4`.

## 6. Tiempo de conmutación

`A4` pide < 1 ms extremo a extremo. Contribuciones:

| Contribución | Estimación | Origen |
| --- | --- | --- |
| Transición del GPIO | ~10 ns | ESP32 [21] |
| Establecimiento de la red de polarización | 3·τ ≈ 0.3 µs | `R_limit · C_bypass` y el filtro LC |
| Conmutación del diodo (carga/descarga de portadores) | **1–3 µs** típico | [9], [10]; a medir |
| Establecimiento de la corriente de RF en el elemento | < 1 µs | constante de tiempo eléctrica del parásito |

Margen estimado: **dos a tres órdenes de magnitud** por debajo del límite. La conclusión práctica es
que `A4` no es un riesgo de diseño; el riesgo es **medirlo mal**. Por eso `T-05` usa un pin de
monitoreo físico y la traza del receptor, no el reloj del firmware.

Nota de asimetría: el pasaje a «encendido» es rápido; el pasaje a «apagado» depende de la remoción
de carga almacenada y es más lento. `T-05` mide las dos transiciones por separado y reporta la peor.

## 7. Reglas de layout

Estas reglas no son estética: cada una responde a un mecanismo concreto de degradación.

1. **La línea de polarización va por la cara inferior del plano de tierra**, nunca por la superior.
   Motivo: la cara superior es la zona de campo intenso; un conductor ahí acopla y deforma el patrón.
2. **El choque se ubica a ≤ 5 mm de la base del parásito.** Motivo: todo el tramo entre la base y el
   choque es conductor de RF a la frecuencia de trabajo.
3. **La línea corre perpendicular al elemento** y se aleja del centro antes de girar. Motivo: minimizar
   el tramo paralelo, que es el que acopla.
4. **Malla de vías de tierra alrededor del punto de alimentación del activo**, separadas ≤ λ/20
   (≈ 6 mm). Motivo: evitar que la corriente de retorno se distribuya por caminos largos y radie.
5. **Sin cobre del plano de tierra entre la base del parásito y su choque** (zona de exclusión de
   3 mm). Motivo: la capacidad parásita a tierra en ese nodo desintoniza el parásito.
6. **El anillo de LEDs y sus cables van en el borde y por la cara inferior.** Motivo: DOC-03 DEC-14;
   un LED sobre el plano en zona de corriente alta es un dispersor.
7. **Conector SMA reforzado mecánicamente**, con el pin central corto. Motivo: `DR-14` (transporte) y
   mínima inductancia serie.

## 8. Estado definido durante el arranque

Problema real: entre el encendido y la configuración de los GPIO, los pines del ESP32 flotan y la
antena queda en un estado arbitrario. Consecuencias: la primera medición de una sesión no es
repetible y `T-05` no puede confiar en el estado inicial.

Solución adoptada: `R_pd = 10 kΩ` de cada GPIO a GND, externa. Con eso, durante el arranque los seis
parásitos quedan en «abierto» (estado `K0`, omnidireccional), que es el estado de referencia del
libro de códigos. No afecta la RF porque está detrás del choque.

## 9. Verificación de esta etapa

| Qué | Cómo | Dónde se registra |
| --- | --- | --- |
| `V_f` real del diodo a 10 mA | fuente de banco, amperímetro, 3 unidades | `mediciones/AAAA-MM-caracterizacion-pin/` |
| Impedancia del choque montado | VNA, una puerta, sin el diodo | igual campaña |
| Corriente real por línea | medir la caída en `R_limit` | igual campaña |
| Estado en el arranque | osciloscopio en el pin de monitoreo al energizar | igual campaña |
| Tiempo de conmutación (las dos transiciones) | `T-05` | `mediciones/AAAA-MM-conmutacion/` |

## 10. Pendientes que bloquean el cierre

| Pendiente | Bloquea |
| --- | --- |
| Confirmar `V_f` y tiempo de conmutación en banco | valores finales de `R_limit` y la afirmación de `A4` |
| Verificar la SRF real del choque elegido | `RSK-04` de `DOC-08` |
| Confirmar disponibilidad del SMP1345 en el proveedor y su precio | `gestion/BOM.md` |
| Decidir si el diodo va soldado o en zócalo | prototipo v0 (zócalo permite reemplazo, pero agrega inductancia) |

Mientras no se midan, los números de este documento son **de diseño**, no **verificados**.
