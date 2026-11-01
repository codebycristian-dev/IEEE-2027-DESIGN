# software/codebook

Generación, validación y análisis del libro de códigos.

Va acá:
- Script que enumera las 2⁶ combinaciones y las agrupa por simetría rotacional.
- Verificación de que la simetría se cumple en la práctica, con datos medidos.
- La lista de configuraciones que se cargan, con su justificación.

Salida esperada: una tabla estable `estado → patrón → categoría` que el firmware y el análisis
consumen sin duplicar la lógica.
