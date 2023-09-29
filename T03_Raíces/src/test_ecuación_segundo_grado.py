from ecuacion_segundo_grado import raices  # https://www.geeksforgeeks.org/why-import-star-in-python-is-a-bad-idea/

def main() -> None:
    print(
        "Programa para la resolución de una ecuación de segundo grado dados sus términos. Por Jaime Argilés."
    )

    a, b, c = (
        float(input("Término cuadrático: ")),
        float(input("Término lineal: ")),
        float(input("Término independiente: ")),
    )

    print(f"Las raíces de la ecuación son (x1, x2) = {raices(a, b, c)}")


if __name__ == "__main__":
    main()
    

