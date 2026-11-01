# mediciones

Campañas de medición. Una carpeta por campaña, nombrada `AAAA-MM-asunto`.

Cada campaña contiene:
- `crudo/` datos tal como los entregó el instrumento, sin editar.
- `procesado/` resultados intermedios regenerables por script.
- `figuras/` las figuras exportadas.
- `README.md` escrito **antes** de medir: qué se mide, con qué instrumento y calibración, distancias,
  alturas, orientación, condiciones del entorno, quién midió y qué se esperaba encontrar.

Reglas:
- El crudo no se toca ni se "limpia" a mano.
- Si el resultado se aparta de lo esperado, se anota en el README de la campaña antes de corregir nada.
- Campañas de más de 20 MB se avisan antes de commitear.
