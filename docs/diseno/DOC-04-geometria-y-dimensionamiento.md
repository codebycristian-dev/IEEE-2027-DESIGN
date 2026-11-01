# DOC-04 — Geometría y dimensionamiento

| Código | DOC-04 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-03 v1.0 (2026-10-14), §5 |
| Tipo | Documento de diseño — geometría |
| Estado | Vigente. **Ninguna cota es final**: los valores finales se cierran con el plan del §7 |

## Historial de versiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Define las variables `DV-##`, el cálculo de partida, el plan de barrido y el procedimiento de ajuste. Corrige la práctica de DOC-02 de fijar cotas sin rango ni criterio de cierre. |

## 1. Objeto

Fijar **qué se puede mover, cuánto y con qué criterio se cierra**. DOC-02 daba cotas («anillo de
radio ≈ λ/4», «plano de 12–18 cm») sin decir cómo se eligen dentro de ese rango ni cómo se sabe que
están bien. Este documento reemplaza esos números por variables con rango, métrica y procedimiento.

## 2. Constantes de partida

| Magnitud | Valor | Cálculo |
| --- | --- | --- |
| Banda de operación | 2400–2483.5 MHz | `DR-01` |
| Frecuencia central | f₀ = 2441.75 MHz | centro de la banda |
| Longitud de onda | λ₀ = c/f₀ = **122.78 mm** | c = 299.792458 mm·ns⁻¹ |
| Cuarto de onda | λ₀/4 = **30.69 mm** | |
| Longitud eléctrica típica de un monopolo real | 0.23λ–0.25λ ≈ **28–31 mm** | la capacidad de extremo y el plano finito acortan respecto de λ/4 ideal |

**Decisión de método:** las cotas de partida son de orden de magnitud y su función es acotar el
espacio de búsqueda, no especificar la pieza. El valor final sale del §7.

## 3. Variables de diseño

| `DV` | Variable | Símbolo | Nominal de partida | Rango a barrer | Criterio de cierre |
| --- | --- | --- | --- | --- | --- |
| DV-01 | Longitud del monopolo activo | `L_a` | 29 mm (0.236λ) | 26–32 mm, 4 niveles | resonancia del activo solo (`Im Z_in ≈ 0`) y mínimo `\|S11\|` en f₀ |
| DV-02 | Radio del anillo de parásitos | `r` | 27 mm (0.22λ) | 22–34 mm, 5 niveles | máximo `F/B` del sector con HPBW aceptable |
| DV-03 | Diámetro del plano de tierra | `D_g` | 150 mm (1.22λ) | 120 / 150 / 180 mm | compromiso inclinación de elevación ↔ tamaño de transporte |
| DV-04 | Longitud de los parásitos | `L_p` | = `L_a` | 0.85–1.05 × `L_a`, 4 niveles | profundidad del nulo (`M-05`) y `F/B` |
| DV-05 | Diámetro del conductor | `d` | 3 mm (varilla) | 2 / 3 / 4 mm | rigidez mecánica y ancho de banda; no se optimiza |
| DV-06 | Altura del plano sobre el suelo de la sala | `h` | 1.2 m | 1.0–1.5 m | reproducibilidad entre campañas, no desempeño |
| DV-07 | Red de adaptación (L, C) | `L_m`, `C_m` | por calcular | 2–15 nH / 0.5–5 pF | `A1` en todos los estados del subconjunto útil |
| DV-08 | Separación del nodo de polarización respecto del plano | `z_b` | 0 mm (en la base) | 0–3 mm | espurios de la línea de polarización en el patrón |

Notas de justificación:

- **DV-02 y la separación entre elementos.** Con 6 parásitos en un anillo regular, la cuerda entre
  elementos adyacentes vale exactamente `r` (`2r·sen 30° = r`). O sea que el radio del anillo **es**
  la separación entre elementos, y por eso su rango se elige en el entorno de 0.2λ–0.25λ, que es el
  espaciamiento clásico reflector–radiador.
- **DV-04 y el papel del parásito.** Con el PIN en conducción el parásito está cortocircuitado a
  tierra y se comporta como reflector si su longitud lo hace resonante cerca de f₀. Alargarlo o
  acortarlo corre esa resonancia y cambia cuánto refleja. Es la variable de sintonía más sensible
  del arreglo: un desplazamiento de 1 mm sobre 29 mm es 3.4 % de la longitud, del orden de 80 MHz de
  corrimiento en frecuencia.
- **DV-03 no se optimiza por ganancia.** Se elige por el compromiso entre inclinación del haz en
  elevación (`N-01` §5) y el tamaño que se transporta a Kioto (`DR-14`). Se documenta la curva
  medida, no se busca un óptimo.
- **DV-05, DV-06 y DV-08 no son objetivos de optimización**: se fijan por mecánica, reproducibilidad
  y control de espurios respectivamente, y solo se revisan si la medición muestra un problema.

## 4. Configuración nominal de partida

```
        Plano de tierra: disco Ø 150 mm (DV-03), PCB doble cara
        Elementos: varilla Ø 3 mm (DV-05)
        Activo: L_a = 29 mm, centro, alimentado por SMA
        Parásitos: L_p = 29 mm, 6 unidades, anillo r = 27 mm (DV-02)
        Altura de trabajo: h = 1.2 m (DV-06)
```

Cotas mecánicas que se derivan y **sí** quedan fijas desde ya, porque son de fabricación:

| Cota | Valor | Motivo |
| --- | --- | --- |
| Separación del borde del plano al anillo | 75 − 27 = **48 mm** (0.39λ) | mantiene los parásitos lejos del borde, donde la corriente de borde es máxima |
| Altura del nodo de polarización | **≤ 3 mm** sobre el cobre | `DV-08`; más alto mete la línea en zona de alta corriente |
| Diámetro del orificio del elemento | **3.2 mm** (varilla de 3 mm con holgura) | permite ajuste y soldadura |
| Posición del SMA | centro, cara inferior | no interrumpe el cobre de la cara superior |

## 5. Efecto esperado del plano finito

Con `D_g = 150 mm` el máximo de radiación no está en el horizonte: sube unos grados por difracción
en el borde (`N-01` §5, referencias [7], [8]). Consecuencias operativas, que se aceptan:

1. El TX de prueba y el arreglo se montan **a la misma altura** (`h ≈ 1.2 m`), para que el máximo
   inclinado del arreglo siga iluminando al TX.
2. El corte de elevación se mide una vez (soporte manual) y se reporta como indicativo, no como
   especificación (`N-03` §6).
3. La falda (*ground skirt*) queda como mitigación del plan B: si `A2` no se alcanza por
   inclinación del haz y no por relación delante/detrás, se agrega una pared vertical de 20 mm en el
   borde antes de tocar el diámetro.

## 6. Tolerancias y procedimiento de ajuste

La sensibilidad es alta (§3, nota DV-04), así que el ajuste es un procedimiento, no un corte a ojo:

1. Cada elemento se corta **3 mm más largo** que el nominal y se ajusta con lima o con el tornillo
   de longitud, midiendo `S11` después de cada paso de 0.5 mm.
2. Se ajusta primero el **activo solo**, con los seis parásitos en circuito abierto (sin diodos, o
   con los PIN al aire), hasta mínimo `S11` en f₀.
3. Después se cortocircuitan los parásitos uno por uno (con un puente de alambre, sin electrónica) y
   se registra el corrimiento de `S11` que produce cada uno. Si el corrimiento es asimétrico entre
   sectores, hay un problema mecánico: se corrige antes de seguir.
4. Solo entonces se instalan los PIN y se repite: la diferencia entre puente de alambre y PIN es la
   pérdida y la inductancia del interruptor, y es un dato que va a `DOC-05`.

Tolerancias aceptadas en la pieza terminada: longitud ±0.5 mm, radio del anillo ±0.5 mm,
perpendicularidad de cada elemento ±2°. Se verifica con calibre y escuadra, y se registra la longitud
real de cada parásito en `hardware/antena/`.

## 7. Plan de barrido

La geometría no se cierra por intuición ni por barrido exhaustivo: son 240 combinaciones si se hace
factorial completo. Se hace en tres etapas encadenadas.

### Etapa A — resonancia del elemento activo

| | |
| --- | --- |
| Herramienta | NEC2 (`nec2c` + `xnec2c`, software libre para estructuras de hilo) |
| Variables | `L_a` en 26, 28, 30, 32 mm |
| Condición | 6 parásitos en circuito abierto; plano como malla de 12 radiales de 150 mm |
| Métrica | frecuencia de resonancia y `\|S11\|` mínimo |
| Corridas | 4 |
| Cierre | `L_a` que resuena en 2441.75 MHz ± 20 MHz |

**Elección de herramienta y su motivo:** el arreglo es de hilos verticales sobre un plano, que es
exactamente el dominio de NEC2. Un simulador de onda completa (openEMS, HFSS) da más fidelidad en el
plano de tierra, pero exige mallado y tiempo de cómputo que el equipo no tiene esta semana. NEC2 da
la tendencia con error conocido y, sobre todo, es reproducible y gratuito (`R8`). La validación final
es la medición, no el simulador.

### Etapa B — anillo y parásitos

| | |
| --- | --- |
| Herramienta | NEC2 |
| Variables | `r` ∈ {22, 25, 27, 30, 34} mm × `L_p` ∈ {0.85, 0.95, 1.00, 1.05}·`L_a` |
| Condición | `L_a` fijo de la etapa A; estado con 3 parásitos contiguos cortocircuitados |
| Métricas | `F/B` del sector (`M-03`), HPBW en azimut, dirección de máximo |
| Corridas | 20 |
| Cierre | celda que maximiza `F/B` manteniendo HPBW ≤ 100° |

### Etapa C — plano de tierra

| | |
| --- | --- |
| Herramienta | NEC2, y después medición |
| Variable | `D_g` ∈ {120, 150, 180} mm |
| Condición | mejor celda de la etapa B |
| Métricas | ángulo de elevación del máximo, `F/B`, `\|S11\|` |
| Corridas | 3 |
| Cierre | `D_g` que mantiene el máximo dentro de ±15° del horizonte con el menor diámetro |

Total: **27 corridas de simulación**. Dos días de trabajo, no dos semanas.

### Etapa D — verificación en banco (prototipo v0)

Antes de soldar un solo PIN, el prototipo v0 reemplaza los interruptores por **puentes de alambre
atornillados** (cortocircuito) y por **ausencia de puente** (abierto). Eso permite medir `A1` y `A2`
con la geometría ya elegida y decidir si el barrido de simulación predijo bien.

| | |
| --- | --- |
| Instrumento | LiteVNA/NanoVNA calibrado en el plano del SMA; plataforma giratoria |
| Protocolos | `T-02` (parcial), `T-03` |
| Criterio de cierre | si `F/B` medido ≥ 8 dB en el mejor sector, se pasa a v1 con PIN; si no, se vuelve a la etapa B con el dato medido |
| Fecha objetivo | 2026-11-14 (plan de acción de DOC-02, paso 6) |

## 8. Qué falta para cerrar este documento

| Falta | Depende de | Bloquea a |
| --- | --- | --- |
| Elección del diámetro nominal definitivo | etapa C | `hardware/antena/` y `hardware/mecanica/` |
| Valores de la red de adaptación (`DV-07`) | `T-02` sobre v0 | `DOC-05`, `A1` |
| Verificación de que el corrimiento por PIN es aceptable | etapa D con PIN | `DOC-05`, compuerta 1 de `DOC-08` |
| Lectura de [3] y [8] para contrastar rangos | deuda de lectura de `N-02` §12 | confianza en los rangos de `DV-02` y `DV-04` |

Mientras el plan no se ejecute, todos los valores de este documento son **de partida** y así se
rotulan en cualquier figura que llegue a la propuesta.
