from triangulo import area_por_heron

def main() -> None:
    print("Programa para calcular el área de un triángulo mediante la fórmula de Herón. Por Jaime Argilés.")
    
    a, b, c = (
        int(input("Lado 1: ")),
        int(input("Lado 2: ")),
        int(input("Lado 3: ")),
    )
    
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError("No tiene sentido un lado negativo")

    a, b, c = sorted((a, b, c))
    if (a + b) <= c:
        raise ValueError("Los lados deben cumplir la desigualdad triangular") 
    
    print(f"El área del triángulo calculada mediante la fórmula de Herón es {area_por_heron(a, b, c)}")


if __name__ == "__main__":
    main()
