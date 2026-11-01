# software/analisis

Procesamiento: patrones, relación delante/detrás, SIR por MAC y detección de movimiento.

Va acá:
- Cálculo de `S11` normalizado y de la máscara de −10 dB de `A1`.
- Cálculo de relación delante/detrás por sector (`A2`).
- Cálculo de SIR y su mejora respecto del estado omnidireccional (`A3`).
- Detección de actividad por sector y su tasa de acierto (`A5`).
- Generación de las figuras que van a la propuesta, siempre desde `mediciones/`.

Regla: el análisis nunca promedia sin reportar la dispersión. Toda figura de la propuesta debe
poder regenerarse con un comando desde los datos crudos.
