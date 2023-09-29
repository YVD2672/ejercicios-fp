from cadena import es_palindromo


def main() -> None:
    palabra = input("Introduce una palabra: ")
    
    print(f"{palabra}{'' if es_palindromo(palabra) else ' no'} es un palíndromo")
    
    
if __name__ == "__main__":
    main()
 