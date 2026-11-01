# firmware/espar-esp32

Firmware del ESP32 que conmuta los seis diodos PIN y adquiere métricas.

Va acá:
- Código fuente y su configuración de compilación.
- Tabla de pines: GPIO → parásito → estado.
- La lista cerrada de configuraciones que se cargan, coincidente con el libro de códigos documentado.
- Medición del tiempo de conmutación, con un pin de monitoreo dedicado.
- Configuración de recepción estricta: el firmware **no transmite** (`R1` de las bases).

Regla: el firmware implementa el libro de códigos documentado; no inventa configuraciones.
