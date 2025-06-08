import csv
import math
from collections import namedtuple
import folium

Coordenadas=namedtuple('Coordenadas','latitud,longitud')
Estacion=namedtuple('Estacion','nombre,bornetas,bornetas_vacias,bicis_disponibles,coordenadas')


def lee_estaciones(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        estaciones=[]
        for name,slots,empty_slots,free_bikes,latitude,longitude in lector:
            nombre=str(name)
            bornetas=int(slots)
            bornetas_vacias=int(empty_slots)
            bicis_disponibles=int(free_bikes)
            latitud=float(latitude)
            longitud=float(longitude)
            coordenadas=Coordenadas(latitud,longitud)
            estacion=Estacion(nombre,bornetas,bornetas_vacias,bicis_disponibles,coordenadas)
            estaciones.append(estacion)
    return estaciones

def estaciones_bicis_libres(estaciones,k=5):
    hay_bicis_libres=[(int(),str())]

    for e in estaciones:
        if e.bicis_disponibles == k:
            hay_bicis_libres.append((e.bicis_disponibles,e.nombre))

    return hay_bicis_libres
#tengo que cambiar la función para que me 
#ordene las estaciones según el número de bicis