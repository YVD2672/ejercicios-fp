def es_palindromo(palabra: str) -> bool:
    """Esta es la solución más rápida (en python) y sencilla al problema"""
    return palabra == palabra[::-1]
