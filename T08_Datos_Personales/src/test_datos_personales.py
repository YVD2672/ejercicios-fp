from datos_personales import (
    Persona,
    filtrar_por_edad,
    obtener_nombre_y_dni,
    obtiene_edades_distintas,
    obtiene_edades_distintas2,
    calculasumaedades,
    calculapromedioedades,
)

personas = [
    Persona("12345678A", "JUAN", "AFAN POSTIGO", 22, "SEVILLA", "SEVILLA"),
    Persona("12345678B", "NICOLAS", "AGUILAR SAUCEDO", 20, "DOS HERMANAS", "SEVILLA"),
    Persona("12345678C", "LUCAS", "ACEJO GARCÍA", 20, "UTRERA", "SEVILLA"),
    Persona("12345678D", "CLAUDIA", "ÁLVAREZ GARCÍA", 21, "VISO DEL ALCOR", "SEVILLA"),
    Persona("12345678E", "PAULA", "ALBENDÍN CAMINO", 19, "TOMARES", "SEVILLA"),
    Persona("12345678F", "ANA", "LOBATO ÁLVAREZ", 18, "PUNTA UMBRÍA", "HUELVA"),
    Persona("12345678G", "ANTONIO", "DÍAZ NARANJO", 18, "CHIPIONA", "CADIZ"),
    Persona("12345678H", "SOFÍA", "GUERRERO CANTARERO", 20, "CHIPIONA", "CADIZ"),
]
EDAD = ...

def test_calculasumaedades(personas:list[Persona]):
    print("\nla suma de las edades es:",
        calculasumaedades(personas))   
    
def test_calculapromedioedades(personas:list[Persona]):
    print('Edades de Jaén: ',calculapromedioedades(personas,'JAEN'))
    print('Edades de Cádiz: ',calculapromedioedades(personas,'CADIZ'))
    print('Edades de Sevilla: ',calculapromedioedades(personas))

def main() -> None:
    #print(obtiene_edades_distintas(personas))
    #print(obtiene_edades_distintas2(personas))
    #print(test_calculasumaedades(personas))
    print(test_calculapromedioedades(personas))


if __name__ == "__main__":
    main()
