from collections import namedtuple


Persona = namedtuple("Persona", "dni, nombre, apellidos, edad, ciudad, provincia")


def filtrar_por_edad(personas: list[Persona], edad: int) -> list[Persona]:
    return [i for i in personas if i.edad < edad]


def obtener_nombre_y_dni(personas: list[Persona]) -> list[Persona]:
    return [(i.dni, i.nombre) for i in personas]


def obtiene_edades_distintas(personas: list[Persona]) -> list[Persona]:
    """Solución sencilla"""
    return len({i.edad for i in personas})


def obtiene_edades_distintas2(personas: list[Persona]) -> list[Persona]:
    """Solución optimizada (en realidad es más lenta en Python, pero en lenguajes de programación de bajo nivel es mucho más rápida)"""
    edades = 0
    for i in personas:
        edades |= (1 << (i.edad))

    return edades.bit_count()

def calculasumaedades(personas:list[Persona])->int:
    res=0
    for i in personas:
        res=res+i.edad
    return res


def calculapromedioedades(personas:list[Persona],prov:str='SEVILLA')->float:
    res=None
    suma=0
    contador=0
    for persona in personas:
        if persona.provincia==prov:
            suma+=persona.edad
            contador+=1
        if contador>0:
            res=suma/contador
    return res