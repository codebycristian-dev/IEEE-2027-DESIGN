# 04 — Aplicación ISAC

| | |
| --- | --- |
| Artefacto / estado | Esqueleto de capítulo de la propuesta de 4 páginas — `esqueleto`, sin redacción |
| Fuente principal | `DOC-03` §6 (modos de operación) y `DOC-06` §4 (libro de códigos) |
| Apoyo | `DOC-07` §4–§8 (protocolos y muestras), `N-03` (`M-03`, `M-04`, `M-07`) |
| Ubicación y fecha | Página 3 (cuerpo principal); se redacta el 2026-12-22, después de G4 |

## Objetivo del capítulo

Mostrar cómo la antena hace ISAC con un receptor comercial: un modo para comunicar eligiendo dirección
y otro para sensar movimiento suprimiendo el trayecto directo. Es el capítulo que responde a «¿y esto
para qué sirve?».

## Qué va

- **Los tres modos y su métrica.** Comunicación: barrido de los seis sectores y se fija el de mayor
  RSSI del TX deseado (`M-04`, `DR-04`, `DR-06`). Sensado: nulo hacia el iluminador más barrido de los
  seis restantes (`M-07`, `DR-05`, `DR-09`). Simultáneo: alternancia estado a estado entre paquetes
  (`DR-07`, `DR-08`). Fuente: `DOC-03` §6.
- **El aporte conceptual.** El nulo no se usa para cancelar interferencia: suprime el trayecto directo
  para dejar visible la energía reflejada por un cuerpo en movimiento (`N-02` §9, punto 2).
- **Libro de códigos: 20 estados, no 64.** `K0` referencia omnidireccional, `KS1`–`KS6` haz de sector,
  `KW1`–`KW6` haz ancho, `KN1`–`KN6` nulo más haz, `KX1` nulos múltiples. Los 44 restantes no se cargan
  y por eso no están obligados a cumplir `A1`; veinte es el máximo medible con la repetibilidad exigida
  antes del 31-dic (`DOC-06` §4).
- **Cómo se demuestra: cinco filas con protocolo y muestra.** `A1` con `T-02` (60 barridos: 20 estados ×
  3 repeticiones), `A2` con `T-03` (10 estados × 72 puntos × 30 paquetes), `A3` con `T-04` (3
  configuraciones × 3 sesiones), `A4` con `T-05` (100 transiciones por sentido y por método) y `A5` con
  `T-06` (60 ensayos ciegos) (`N-04` §4, `DOC-07` §4–§8).
- **Honestidad estadística.** Para `A5` se publica la matriz de confusión 6×6, no un porcentaje global:
  la tasa global esconde los sectores que fallan siempre (`DOC-07` §8).
- **Figura.** Patrón de azimut medido de `K0` contra un `KS`, o el mapa estado → dirección si la
  campaña de patrones no llegó (`mediciones/AAAA-MM-patrones/`).

## Qué no va

- La tabla completa de los 20 estados con su valor hexadecimal: vive en `DOC-06` §4 y en el firmware.
  A la propuesta va el conteo por bloque y el nombre de los bloques.
- La demostración de las 14 órbitas y el lema de Burnside.
- El presupuesto de tiempo de barrido por modo (`DOC-06` §6), salvo una frase: el refresco es ≤ 1 s en
  operación y no en modo medición (`DR-10`).
- Los procedimientos paso a paso de los diez protocolos: van el nombre, la muestra y el criterio.
- Cualquier resultado. Hoy `DOC-07` §13 marca los diez protocolos como «no ejecutado»; si al 22-dic
  sigue así, la tabla se rotula como expectativa con el protocolo pendiente.

## Extensión prevista

Página 3, **≈ 40 de las 46 líneas** disponibles (las otras 6 cierran el capítulo 03). Distribución:
modos 10, aporte conceptual 4, libro de códigos 8, criterios y muestras 12, epígrafe de figura 3.

## Lista de verificación antes de cerrar el capítulo

- [ ] Cada criterio cita su `A#` y su `T-##`, y la muestra coincide con `DOC-07`.
- [ ] Las metas son las de `N-04` §4, con la banda de guarda declarada al lado.
- [ ] El conteo de estados cierra en 20 y los bloques se llaman igual que en `DOC-06`.
- [ ] Ninguna fila presenta un valor medido que no exista en `mediciones/`.
- [ ] El nulo se describe como supresión del trayecto directo, no como cancelación de interferencia.
- [ ] Toda afirmación tiene un ID detrás (`DR-##`, `A#`, `T-##`, `M-##`).
