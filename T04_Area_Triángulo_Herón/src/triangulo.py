from math import sqrt
from typing import Union

def perimetro(a: float, b: float, c: float) -> float:    
    return a + b + c


def area_por_heron(a: float, b: float, c: float) -> float:
    semi_perimetro = perimetro(a, b, c) / 2
    
    return sqrt(semi_perimetro * (semi_perimetro - a) * (semi_perimetro - b) * (semi_perimetro - c))
