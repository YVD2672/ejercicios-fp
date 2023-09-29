from math import sqrt
from typing import Union

def raices(
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> (Union[float, None], Union[float, None]):
    discriminante = b ** 2 - 4 * a * c
    
    if (a != 0) and (discriminante >= 0):
        return (
            (- b + sqrt(discriminante)) / (2 * a),
            (- b + sqrt(discriminante)) / (2 * a),
        )

    return None, None
