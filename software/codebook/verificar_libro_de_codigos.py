#!/usr/bin/env python3
"""Verifica el libro de codigos de DOC-06 contra su propia enumeracion.

Comprueba tres cosas:
  1. Que las cadenas de 6 bits formen exactamente 14 orbitas bajo rotacion (simetria C6),
     con los tamanos de orbita que declara DOC-06 seccion 3.
  2. Que la tabla de 20 estados de DOC-06 seccion 4 sea coherente: cadena, bits y hex
     dicen lo mismo, y no hay estados repetidos.
  3. Que cada bloque de estados sea el conjunto de rotaciones que el documento afirma.

Uso: python3 software/codebook/verificar_libro_de_codigos.py
Sale con codigo 1 si algo no coincide, e imprime el detalle.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

N_ELEMENTOS = 6
N_ESTADOS = 1 << N_ELEMENTOS
DOC = Path(__file__).resolve().parents[2] / "docs" / "diseno" / "DOC-06-libro-de-codigos.md"

# Tamanos de orbita declarados en DOC-06 seccion 3, ordenados.
TAMANOS_ESPERADOS = sorted([1, 1, 6, 6, 6, 6, 3, 6, 6, 3, 6, 6, 6, 2])

# Bloque al que pertenece cada estado cargado, segun DOC-06 seccion 4.
BLOQUES = {
    "K0": "K0",
    "KS1": "KS", "KS2": "KS", "KS3": "KS", "KS4": "KS", "KS5": "KS", "KS6": "KS",
    "KW1": "KW", "KW2": "KW", "KW3": "KW", "KW4": "KW", "KW5": "KW", "KW6": "KW",
    "KN1": "KN", "KN2": "KN", "KN3": "KN", "KN4": "KN", "KN5": "KN", "KN6": "KN",
    "KX1": "KX",
}

FILA = re.compile(r"^\|\s*(K\w+)\s*\|\s*`([01]{6})`\s*\|\s*([01]{6})\s*\|\s*0x([0-9A-Fa-f]{2})\s*\|")


def rotar(valor: int, k: int, bits: int = N_ELEMENTOS) -> int:
    """Rota circularmente los `bits` bits de `valor` k posiciones."""
    k %= bits
    return ((valor << k) | (valor >> (bits - k))) & ((1 << bits) - 1)


def orbitas() -> dict[int, set[int]]:
    """Agrupa los 64 estados en orbitas bajo el grupo de rotaciones C6."""
    vistas: set[int] = set()
    resultado: dict[int, set[int]] = {}
    for estado in range(N_ESTADOS):
        if estado in vistas:
            continue
        orbita = {rotar(estado, k) for k in range(N_ELEMENTOS)}
        resultado[min(orbita)] = orbita
        vistas |= orbita
    return resultado


def valor_de_cadena(cadena: str) -> int:
    """Convierte una cadena P1..P6 en su valor entero, con P1 como bit 0."""
    return sum(int(bit) << i for i, bit in enumerate(cadena))


def leer_tabla() -> list[tuple[str, str, str, int]]:
    """Extrae las filas de la tabla de estados cargados de DOC-06."""
    filas = []
    for linea in DOC.read_text(encoding="utf-8").splitlines():
        coincidencia = FILA.match(linea)
        if coincidencia:
            id_estado, cadena, bits, hexa = coincidencia.groups()
            filas.append((id_estado, cadena, bits, int(hexa, 16)))
    return filas


def main() -> int:
    errores: list[str] = []

    # 1. Enumeracion de orbitas.
    grupo = orbitas()
    tamanos = sorted(len(o) for o in grupo.values())
    if len(grupo) != 14:
        errores.append(f"orbitas: se esperaban 14, se obtuvieron {len(grupo)}")
    if tamanos != TAMANOS_ESPERADOS:
        errores.append(f"tamanos de orbita: esperados {TAMANOS_ESPERADOS}, obtenidos {tamanos}")
    cubiertos = set().union(*grupo.values())
    if len(cubiertos) != N_ESTADOS:
        errores.append(f"cobertura: las orbitas cubren {len(cubiertos)} de {N_ESTADOS} estados")

    # 2. Tabla de estados cargados.
    filas = leer_tabla()
    if len(filas) != 20:
        errores.append(f"tabla: se esperaban 20 estados, se encontraron {len(filas)}")

    valores: dict[int, str] = {}
    for id_estado, cadena, bits, hexa in filas:
        esperado_valor = valor_de_cadena(cadena)
        if esperado_valor != hexa:
            errores.append(
                f"{id_estado}: cadena {cadena} vale 0x{esperado_valor:02X}, la tabla dice 0x{hexa:02X}"
            )
        bits_calculados = format(esperado_valor, "06b")
        if bits_calculados != bits:
            errores.append(
                f"{id_estado}: bits P6..P1 deberian ser {bits_calculados}, la tabla dice {bits}"
            )
        if hexa in valores:
            errores.append(f"{id_estado}: hex 0x{hexa:02X} repetido con {valores[hexa]}")
        valores[hexa] = id_estado

    # 3. Cada bloque debe ser el conjunto completo de rotaciones de su primer estado.
    for bloque in ("KS", "KW", "KN"):
        miembros = {hexa for hexa, id_estado in valores.items() if BLOQUES.get(id_estado) == bloque}
        if not miembros:
            errores.append(f"bloque {bloque}: vacio")
            continue
        base = min(miembros)
        esperado = {rotar(base, k) for k in range(N_ELEMENTOS)}
        if miembros != esperado:
            faltan = sorted(esperado - miembros)
            sobran = sorted(miembros - esperado)
            errores.append(
                f"bloque {bloque}: no es un conjunto cerrado de rotaciones "
                f"(faltan {[hex(e) for e in faltan]}, sobran {[hex(e) for e in sobran]})"
            )

    # El bloque KN debe ser el complemento del bloque KW: nulo opuesto al haz ancho.
    kw = {hexa for hexa, id_estado in valores.items() if BLOQUES.get(id_estado) == "KW"}
    kn = {hexa for hexa, id_estado in valores.items() if BLOQUES.get(id_estado) == "KN"}
    if kw and kn and {v ^ 0x3F for v in kw} != kn:
        errores.append("bloque KN: no es el complemento bit a bit del bloque KW")

    if errores:
        print("FALLA: el libro de codigos no coincide con DOC-06", file=sys.stderr)
        for error in errores:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"OK: 14 orbitas cubriendo los 64 estados, tamanos {tamanos}")
    print(f"OK: {len(filas)} estados cargados, cadena/bits/hex coherentes y sin repetidos")
    print("OK: bloques KS, KW y KN cerrados bajo rotacion; KN = complemento de KW")
    return 0


if __name__ == "__main__":
    sys.exit(main())
