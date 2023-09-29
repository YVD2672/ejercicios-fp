def es_bisiesto(año: int) -> bool:
    return (año % 400 == 0) or ((año % 4 == 0) and (año % 100 != 0))
