# firmware/espar-esp32

Firmware del ESP32 que conmuta los seis diodos PIN y adquiere métricas.

Va acá:
- Código fuente y su `platformio.ini` (o equivalente).
- Tabla de pines: GPIO → parásito → estado.
- Implementación del libro de códigos de `docs/diseno/DOC-06-libro-de-codigos.md`.
- Medición del tiempo de conmutación: marca de tiempo en la conmutación y prueba de `A4`.
- Modo receptor estricto: el firmware no debe transmitir. Ver `R1` en `docs/teoria/04`.

Regla: los estados del código son los `K*` de DOC-06. El firmware no inventa configuraciones.
