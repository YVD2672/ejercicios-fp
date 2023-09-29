from functools import lru_cache

@lru_cache(100)
def factorial(n: int) -> int:
    """Implementación recursiva con caché, debería ser más rápida para inputs menores a 100"""
    
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un núm. negativo")
    
    if n <= 1:
        return 1
    
    return factorial(n - 1) * factorial(n - 2)


def numero_combinatorio(m: int, n: int) -> int:
    if m < n:
        raise ValueError("El denominador no puede ser mayor que el numerador")
    
    return factorial(m) // (factorial(n) * factorial(n - m))
