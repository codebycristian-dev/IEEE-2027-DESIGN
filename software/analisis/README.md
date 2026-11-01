# software/analisis

Procesamiento de las mediciones: patrones, relación delante/detrás, SIR por MAC y detección de movimiento.

Va acá:
- Cálculo de `S11` normalizado y de la máscara de −10 dB.
- Relación delante/detrás por sector.
- SIR y su mejora respecto de la configuración omnidireccional.
- Detección de actividad por sector y su tasa de acierto.
- Generación de las figuras que van a la propuesta, siempre desde `mediciones/`.

Regla: el análisis nunca promedia sin reportar la dispersión. Toda figura de la propuesta debe poder
regenerarse con un comando desde los datos crudos.
