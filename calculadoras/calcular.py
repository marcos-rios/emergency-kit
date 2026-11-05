#!/usr/bin/env python3
"""Calcula cantidades de reserva según personas y días.

Uso:
    python3 calcular.py --personas 4 --dias 3

Lee cantidades.csv (base: familia de 4 personas) y escala cada fila.
Todos los resultados son ESTIMACIÓN. Solo usa la biblioteca estándar.
"""

import argparse
import csv
import math
import sys
from pathlib import Path

LITROS_POR_PERSONA_DIA = 3
LITROS_POR_BIDON = 20
COMIDAS_POR_DIA = 3
PERSONAS_BASE = 4

CSV_CANTIDADES = Path(__file__).resolve().parent / "cantidades.csv"


def entero_positivo(texto):
    valor = int(texto)
    if valor < 1:
        raise argparse.ArgumentTypeError("tiene que ser un entero mayor o igual a 1")
    return valor


def redondear_arriba(valor, decimales=0):
    factor = 10 ** decimales
    # Se resta un épsilon para que 2.0000000001 no suba a 2.1 por error de coma flotante.
    return math.ceil(valor * factor - 1e-9) / factor


def formatear(valor, decimales=0):
    if decimales == 0:
        return str(int(valor))
    texto = f"{valor:.{decimales}f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")


def agua_litros(personas, dias):
    return personas * dias * LITROS_POR_PERSONA_DIA


def bidones(litros):
    return math.ceil(litros / LITROS_POR_BIDON)


def escalar(fila, personas, dias):
    """Devuelve el texto de la cantidad para una fila con escala=si."""
    base_3d = float(fila["base_3d"])
    base_7d = float(fila["base_7d"])
    if dias <= 3:
        base = base_3d / 3 * dias
    elif dias == 7:
        base = base_7d
    else:
        base = base_7d / 7 * dias
    valor = base * personas / PERSONAS_BASE
    decimales = 1 if fila["unidad"] == "kg" else 0
    return formatear(redondear_arriba(valor, decimales), decimales)


def sin_escala(fila, dias):
    """Las filas con escala=no se copian tal cual (texto incluido)."""
    return fila["base_3d"] if dias <= 3 else fila["base_7d"]


def calcular(personas, dias, ruta_csv=CSV_CANTIDADES):
    litros = agua_litros(personas, dias)
    filas = []
    with open(ruta_csv, encoding="utf-8", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            if fila["item"] == "Agua potable":
                cantidad = formatear(litros)
            elif fila["escala"] == "calc":
                cantidad = formatear(bidones(litros))
            elif fila["escala"] == "si":
                cantidad = escalar(fila, personas, dias)
            else:
                cantidad = sin_escala(fila, dias)
            filas.append(
                {
                    "categoria": fila["categoria"],
                    "item": fila["item"],
                    "cantidad": cantidad,
                    "unidad": fila["unidad"],
                    "nota": fila["nota"],
                }
            )
    # sorted es estable: dentro de cada categoría se respeta el orden del CSV.
    return sorted(filas, key=lambda f: f["categoria"])


def imprimir_tabla(filas):
    columnas = ["categoria", "item", "cantidad", "unidad", "nota"]
    titulos = {
        "categoria": "Categoría",
        "item": "Ítem",
        "cantidad": "Cantidad",
        "unidad": "Unidad",
        "nota": "Nota",
    }
    anchos = {
        c: max(len(titulos[c]), *(len(f[c]) for f in filas)) for c in columnas
    }
    print("  ".join(titulos[c].ljust(anchos[c]) for c in columnas).rstrip())
    print("  ".join("-" * anchos[c] for c in columnas))
    categoria_anterior = None
    for fila in filas:
        if categoria_anterior is not None and fila["categoria"] != categoria_anterior:
            print()
        categoria_anterior = fila["categoria"]
        celdas = [
            fila[c].rjust(anchos[c]) if c == "cantidad" else fila[c].ljust(anchos[c])
            for c in columnas
        ]
        print("  ".join(celdas).rstrip())


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Calcula cantidades de reserva para N personas y D días (ESTIMACIÓN)."
    )
    parser.add_argument("--personas", type=entero_positivo, required=True)
    parser.add_argument("--dias", type=entero_positivo, required=True)
    args = parser.parse_args(argv)

    personas, dias = args.personas, args.dias
    litros = agua_litros(personas, dias)
    filas = calcular(personas, dias)
    latas = sum(int(fila["cantidad"]) for fila in filas if fila["unidad"] == "latas")

    print(f"Reserva para {personas} personas y {dias} días (ESTIMACIÓN)")
    print()
    print(f"Agua para bebida y comidas: {litros} L ({personas} × {dias} × {LITROS_POR_PERSONA_DIA} L)")
    print("Sumá agua para higiene y otros usos; esa reserva no está incluida.")
    print(f"Bidones de {LITROS_POR_BIDON} L: {bidones(litros)}")
    print(f"Comidas: {personas * dias * COMIDAS_POR_DIA} ({personas} × {dias} × {COMIDAS_POR_DIA})")
    print(f"Latas en total: {latas} (suma de las filas redondeadas de la tabla)")
    print()
    imprimir_tabla(filas)
    print()
    print("Las cantidades son orientativas. Dosis de medicamentos: consultá a un médico o farmacéutico.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
