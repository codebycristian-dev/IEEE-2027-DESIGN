# software/instrumentos

Adquisición desde el NanoVNA/LiteVNA y desde el ESP32.

Va acá:
- Script de barrido de `S11` por configuración, con la calibración SOL documentada.
- Script de captura de patrones sobre la plataforma giratoria.
- Exportadores a CSV con encabezado autocontenido: fecha, instrumento, calibración, estado, ángulo.

Regla: todo archivo que produce este código va a `mediciones/AAAA-MM-asunto/crudo/` sin editar a mano.
La reproducibilidad del análisis depende de eso.
