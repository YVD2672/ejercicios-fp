from combinatoria import numero_combinatorio

def main() -> None:
    m, n = (
        int(input("Introduce el numerador: ")),
        int(input("Introduce el denominador: ")),
    )
    
    print(f"{m} sobre {n} es {numero_combinatorio(m, n)}")

if __name__ == "__main__":
    main()
