# software/codebook

Generación, validación y análisis del libro de códigos.

Va acá:
- Script que enumera las 64 combinaciones y las agrupa en las 14 órbitas bajo simetría C6.
- Verificación de que la simetría rotacional se cumple en la práctica, con datos medidos.
- Selección del subconjunto útil y su justificación contra `docs/diseno/DOC-06-libro-de-codigos.md`.

Salida esperada: una tabla estable `estado → órbita → categoría → patrón esperado` que el firmware
y el análisis consumen sin duplicar la lógica.
