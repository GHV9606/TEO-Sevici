import csv
import math
from collections import namedtuple
import folium
import webbrowser
import os


Coordenadas=namedtuple('Coordenadas','longitud,latitud')
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
            coordenadas=Coordenadas(longitud,latitud)
            estacion=Estacion(nombre,bornetas,bornetas_vacias,bicis_disponibles,coordenadas)
            estaciones.append(estacion)
    return estaciones

def estaciones_bicis_libres(estaciones,k=5):
    hay_bicis_libres=[]

    for est in estaciones:
        if est.bicis_disponibles >= k:
            hay_bicis_libres.append((est.bicis_disponibles,est.nombre))
    
    hay_bicis_libres_ordenada=sorted(hay_bicis_libres, reverse=True)
    return hay_bicis_libres_ordenada
    #la solución del test en el notebook está mal,
    # ya que da la solución si no se ordenan por 
    # cantidad de bicis disponibles

def calcula_distancia(coordenadas1, coordenadas2):
    x1=coordenadas1.longitud
    y1=coordenadas1.latitud
    x2=coordenadas2.longitud
    y2=coordenadas2.latitud
    
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    return distancia

def estaciones_cercanas(estaciones,coordenadas, k=5):
    estaciones_cerca=[]
    
    for est in estaciones:
        distancia=calcula_distancia(est.coordenadas,coordenadas)
        estaciones_cerca.append((distancia,est.nombre,est.bicis_disponibles))
    
    estaciones_cerca_orden=sorted(estaciones_cerca, 
                                  key= lambda estacion_cerca : estacion_cerca[0])

    return estaciones_cerca_orden[:k]

def crea_mapa(latitud,longitud,zoom=9):
    mapa= folium.Map(location=[latitud,longitud], zoom_start=zoom)
    # en location si falla resultado revisar si es longitud,latitud o al revés (latitud,longitud)
    return mapa

def crea_marcador(latitud, longitud, etiqueta,color):
    marcador=folium.Marker([latitud,longitud],
                           popup=etiqueta,
                           icon=folium.Icon(color=color,
                                             icon='info_sign'))
    return marcador

def media_coordenadas(estaciones):
    latitudes=[]
    longitudes=[]
    
    for est in estaciones:
        latitudes.append(est.coordenadas.latitud)
        longitudes.append(est.coordenadas.longitud)
    
    media_lat=sum(latitudes)/len(latitudes)
    media_long=sum(longitudes)/len(longitudes)
    coord_media=Coordenadas(media_lat,media_long)
    #se puede hacer esto con las namedtuple?
    
    return coord_media

def funcion_color(estacion):
    return 'blue'

def crea_mapa_estaciones(estaciones, funcion_color):
    centro_mapa=media_coordenadas(estaciones)
    mapa=crea_mapa(centro_mapa.latitud,
                   centro_mapa.longitud,
                   13)

    for est in estaciones:
        color=funcion_color(est)
        marcador=crea_marcador(est.coordenadas.latitud,
                               est.coordenadas.longitud,
                               est.nombre,
                               color)
        marcador.add_to(mapa)
    return mapa

def guarda_mapa(mapa, ruta_fichero):
    mapa.save(ruta_fichero)
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))