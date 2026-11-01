# DOC-09 — Mejora de la propuesta de diseño: delta contra DOC-02

| Código | DOC-09 |
| --- | --- |
| Versión / fecha | 1.0 — 2026-10-14 |
| Documento previo | DOC-02 v2.0 (2026-10-13), §5.1 y §7.1 |
| Tipo | Registro de mejora y justificación |
| Estado | Vigente |

## 1. Objeto

DOC-02 fue un **punto de partida**: eligió bien la tecnología y describió una arquitectura, pero no
tenía trazabilidad de diseño, no fijaba variables con criterio y tenía al menos una meta
inalcanzable. Este documento lista, sin adornos, **qué cambió, por qué y a costa de qué**.

La regla que se aplicó: nada se cambió por preferencia estética. Cada cambio responde a un problema
verificable.

## 2. Delta de diseño

| # | Tema | DOC-02 | Vigente | Motivo del cambio | Documento |
| --- | --- | --- | --- | --- | --- |
| 1 | Red de adaptación del activo | **no existía** | red L fija dimensionada sobre el estado promedio del libro | sin red, `\|S11\|` cambia en cada estado y `A1` es inalcanzable: el monopolo ve la impedancia mutua de seis parásitos que conmutan | DEC-07, DOC-05 |
| 2 | Alcance de `A1` | «todas las configuraciones del libro de códigos» (64) | «los 20 estados cargados» | 64 estados no se pueden medir con la repetibilidad exigida antes del 31-dic; el criterio tiene que ser exigente **y** verificable | N-04 §4 |
| 3 | Radio del anillo | «≈ λ/4» como valor | `DV-02`, rango 22–34 mm (0.18λ–0.28λ) con barrido de 5 niveles | «≈λ/4» era una cota de orden de magnitud presentada como decisión. Además, con 6 elementos la cuerda entre adyacentes **es** el radio, así que es la variable de acoplamiento más importante y merece barrido | DOC-04 §3 |
| 4 | Plano de tierra | «12–18 cm de diámetro» sin criterio | `DV-03`, nominal 150 mm, tres niveles, con curva de inclinación en elevación | el diámetro cambia el ángulo del máximo, no solo el tamaño: es una variable electromagnética con compromiso mecánico | DOC-04 §3 y §5 |
| 5 | Estados cargados | 64 (implícito) | 20 explícitos en 5 bloques con rol asignado (`K0`, `KS*`, `KW*`, `KN*`, `KX1`) | 50 de los 64 son rotaciones o complementos sin información nueva; cargarlos multiplica estados a verificar sin agregar capacidad | DOC-06 §4 |
| 6 | Libro de códigos como artefacto | «barrido del libro de códigos» | tabla completa estado → bits → hex → dirección de haz, con verificador automático | sin lista cerrada, `DR-18` no es verificable y un error de un bit no se detecta hasta ver el patrón | DOC-06, `software/codebook/` |
| 7 | Control del ESP32 | «6 líneas digitales, sin registros» | mapa de pines completo, pin de monitoreo dedicado, pull-down de arranque, pines de strapping evitados | el pull-down resuelve el estado indefinido durante el arranque; el pin de monitoreo es lo que hace medible `A4` sin instrumentación extra | DOC-03 §5.1, DOC-05 §8 |
| 8 | Polarización | «resistencia + bobina de bloqueo» | `R = 220 Ω`, `I = 10.9 mA`, choque con criterio de autorresonancia, bypass C0G, reglas de layout | faltaban los números; el criterio de SRF evita el error de elegir un inductor más grande que resuena dentro de banda y convierte la línea en antena | DOC-05 §3–§4 |
| 9 | Tiempo de conmutación | «µs» como afirmación | descomposición por contribución + protocolo de medición con dos métodos y 200 transiciones | una cifra sin método no se puede defender; además la transición a «apagado» es más lenta que la de «encendido» y nadie la medía | DOC-05 §6, DOC-07 T-05 |
| 10 | Modo sensado | «varianza temporal de RSSI/CSI por sector» | métrica `M-07` con ventana `W = 10 s`, decisión por sector, protocolo ciego y matriz de confusión 6×6 | «varianza» sin ventana ni umbral no es una métrica; el ensayo ciego evita el sesgo del operador | N-03, DOC-07 T-06 |
| 11 | Profundidad de nulo esperada | no declarada | 10–20 dB declarado como expectativa realista | el techo de −50 dB de la literatura usa varactores; prometer eso con PIN es indefendible ante un jurado que conoce el tema | N-01 §3, N-02 §2 |
| 12 | Verificación | `A1`–`A5` con «método de verificación» en una línea | 10 protocolos con montaje, procedimiento, tamaño de muestra, criterio con banda de guarda y destino de datos | sin protocolo, dos personas obtienen dos resultados; con protocolo, el resultado es comparable y replicable (`C4.2`) | DOC-07 |
| 13 | Incertidumbre | no tratada | presupuesto de 3–4 dB con término dominante identificado y regla `valor − 3 dB ≥ meta` | `A2` y `A3` están en 10 dB y la incertidumbre es de 3–4 dB: sin banda de guarda, un 10.0 dB medido no significa nada | N-03 §4 |
| 14 | Trazabilidad | no existía | `R# → DR-## → A# → T-## → campaña` con cobertura completa | es lo que permite que una frase de la propuesta se defienda o se caiga | N-04 |
| 15 | Riesgos | lista cualitativa por tecnología | 12 riesgos con disparador, mitigación y compuerta fechada, más 3 riesgos aceptados explícitamente | un riesgo sin disparador no se detecta; una compuerta sin fecha no se respeta | DOC-08 |
| 16 | Mecánica del montaje | no tratada | tolerancias de fabricación, procedimiento de ajuste, rearmado ≤ 10 min, caja de transporte | `C3.3` evalúa robustez de demo y transporte, y en 2025 ganó un sistema mecánico | DOC-04 §6, DOC-07 T-09 |

## 3. Lo que **no** se cambió

| Elemento | Por qué se conserva |
| --- | --- |
| Tecnología ESPAR frente a RIS y píxeles | la decisión de DOC-01/DOC-02 está bien fundada: puntaje, valor esperado y cumplimiento sin condiciones |
| Banda 2400–2483.5 MHz | decisión `D-02`: iluminadores abundantes y componentes baratos |
| Siete elementos (1 + 6) | es el menor número con sectores regulares de 60° y simetría C6 exacta (DEC-04) |
| Diodos PIN como mecanismo | restricción del mentor y criterio de bajo costo |
| Modos comunicación y sensado | es la aplicación ISAC que da originalidad (`C1`) |
| Monopolos de varilla | acceso mecánico al nodo del interruptor y ajuste por corte (DEC-03) |

## 4. Qué gana la propuesta de 4 páginas

Concretamente, estas afirmaciones hoy se pueden sostener y antes no:

1. **«El sistema cubre 360° en azimut con seis sectores»** — respaldado por la simetría C6 demostrada
   y por 20 estados enumerados, no por una suposición.
2. **«La mejora de SIR se mide contra el estado omnidireccional»** — con protocolo, tamaño de muestra
   e incertidumbre declarada.
3. **«El diseño es replicable»** — con BOM, tolerancias, procedimiento de ajuste y 10 protocolos:
   cualquier grupo puede repetirlo (`C4.2`, que es criterio de evaluación).
4. **«La conmutación es sub-milisegundo»** — con la descomposición por contribución y el método de
   medición.
5. **«Cada requisito de las bases está cubierto»** — con la matriz `R → DR` completa y sin huecos.

## 5. Lo que sigue flojo, y se declara

Un documento de mejora que no reconoce lo pendiente es propaganda.

| Pendiente | Consecuencia sobre la propuesta |
| --- | --- |
| Ningún `A#` medido: no hay prototipo | la propuesta del 31-dic depende de que G1 y G2 se cumplan; si no, los resultados se rotulan como expectativa y el plan se declara |
| Implementación de la etapa D de DOC-04 (ajuste de cotas) | las cotas de la propuesta son de partida, no finales |
| Lectura completa de las referencias [2], [3], [6], [7], [8] | las cifras de ganancia y `F/B` esperadas son expectativas, no datos verificados |
| Respuestas `P1`–`P3` | el protocolo `T-01` y el cómputo del costo pueden cambiar |
| Choque y `V_f` del PIN sin medir | el punto de operación de DOC-05 es calculado, no caracterizado |

## 6. Costo de las mejoras

Cada mejora agregó algo a cambio. Se declara para que no sorprenda:

| Mejora | Lo que agrega | Costo |
| --- | --- | --- |
| Red de adaptación (1) | 2 componentes y una iteración de ajuste | un cálculo más que puede fallar; mitigado con el plan B de red conmutada |
| Polarización detallada (8) | 5 componentes por línea, 30 en total | más soldaduras y más superficie de error de montaje (`RSK-02`) |
| Pin de monitoreo y pull-downs (7) | 7 componentes | ninguno relevante |
| Verificación formal (12) | ~20 horas de banco | tiempo que sale de la construcción; se priorizó porque sin medición no hay propuesta |

Ninguna mejora cambia el costo del sistema de forma apreciable frente al tope de US$1500.

## 7. Conclusión

DOC-02 acertó en la decisión y falló en la trazabilidad. Este conjunto de documentos no reemplaza esa
decisión: la hace **defendible**. La diferencia entre ambos estados del proyecto es la que hay entre
«creemos que funciona porque el cálculo cierra» y «podemos mostrar el protocolo, el dato y el margen de
error».

Esa diferencia es, en este concurso, la que separa una propuesta del montón de una finalista.
