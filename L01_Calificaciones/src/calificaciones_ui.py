from typing import Union

nota = Union[float, None]


def solicita_notas() -> tuple[str, tuple[nota, nota, nota, nota], tuple[nota, nota]]:
    nombre = input("Introduce tu nombre: ")
    
    notas_teoria = [None] * 4

    for i in range(4):
        nota = input(f"Nota del examen teórico {i + 1} (- si no se ha presentado): ")
        notas_teoria[i] = float(nota) if nota != "-" else None

    notas_practica = [None] * 4

    for i in range(2):
        nota = input(f"Nota del examen práctico {i + 1} (- si no se ha presentado): ")
        notas_practica[i] = float(nota) if nota != "-" else None


    return nombre, notas_teoria, notas_practica
