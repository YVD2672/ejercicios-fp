from typing import Union

nota = Union[float, None]


def nota_teoria(nota_examen_1: nota, nota_examen_2: nota) -> float:
    nota_examen_1 = nota_examen_1 or 0  # convertir 'None' a 0
    nota_examen_2 = nota_examen_2 or 0

    return (nota_examen_1 + nota_examen_2) / 2


def nota_cuatrimestre(notas_teoria: tuple[nota, nota], nota_practico: nota) -> float:
    media_teoria = nota_teoria(*notas_teoria)
    nota_practico = nota_practico or 0  # convertir 'None' a 0

    if media_teoria < 4:
        return 0

    return 0.2 * media_teoria + 0.8 * nota_practico


def nota_continua(
    notas_teoria: tuple[nota, nota, nota, nota], notas_practico: tuple[nota, nota]
) -> float:
    for i in notas_teoria:  # convertir cualquier 'None' a 0
        i = i or None

    for i in notas_practico:
        i = i or None

    return (
        nota_cuatrimestre(notas_teoria[:2], notas_practico[0])
        + nota_cuatrimestre(notas_teoria[2:], notas_practico[1])
    ) / 2


