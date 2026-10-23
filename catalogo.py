import json
from funciones_base import obtener_posicion
from satelite import Satelite

def leer (ruta):
    with open (ruta,"r") as datos:
        return json.load(datos)

def catalogo(datos):
    catalogo=[]
    for dato in datos:
        latitud,longitud,elevacion = obtener_posicion(dato)
        catalogo.append(Satelite(dato["OBJECT_NAME"],dato["NORAD_CAT_ID"],latitud,longitud,elevacion))
    return catalogo


def resumen_orbita(lista_objetos):
    resumen = {}

    for satelite in lista_objetos:
        tipo = satelite.tipo_orbita()
        altitud = satelite.altitud

        if tipo not in resumen:
            resumen[tipo] = {
                "cantidad": 0,
                "minimo": altitud,
                "maximo": altitud,
                "suma": 0
            }

        resumen[tipo]["cantidad"] += 1
        resumen[tipo]["suma"] += altitud

        if altitud < resumen[tipo]["minimo"]:
            resumen[tipo]["minimo"] = altitud

        if altitud > resumen[tipo]["maximo"]:
            resumen[tipo]["maximo"] = altitud

    for tipo in resumen:
        cantidad = resumen[tipo]["cantidad"]
        suma = resumen[tipo]["suma"]

        resumen[tipo]["promedio"] = suma / cantidad
        del resumen[tipo]["suma"]

    return resumen

