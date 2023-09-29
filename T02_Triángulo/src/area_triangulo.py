def main() -> None:
    print("Programa para calcular el área de triángulo dadas su base y altura. Por Jaime Argilés.")
    
    base, altura = (
        float(input("Valor de la base: ")),
        float(input("Valor de la altura: ")),
    )
    
    if (base < 0) or (altura < 0):
        print("ERROR: ni la base ni la altura pueden ser negativas.")
        return
    
    print(f"El área del triángulo es igual a {base * altura / 2} u^2")
    

if __name__ == "__main__":
    main()
    