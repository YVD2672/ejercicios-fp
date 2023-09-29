from es_bisiesto import es_bisiesto

def main() -> None:
    print("Programa para comprobar si un año es bisiesto. Por Jaime Argilés.")
    
    while(
        (año := int(input("Introduce un año (o un núm. negativo para terminar el programa): "))) >= 0
    ):
        if es_bisiesto(año):
            print(f"{año} es bisiesto")
        else:
            print(f"{año} no es bisiesto")
            

if __name__ == "__main__":
    main()
