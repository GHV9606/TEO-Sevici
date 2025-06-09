from sevici import *

def test_lee_estaciones(fichero):
    estaciones=lee_estaciones(fichero)
    
    print(f'las tres primeras estaciones son:')
    for est in estaciones[:3]:
        print(est)
    print(f'las tres últimas estaciones son:')
    for est in estaciones[-3:]:
        print(est)


def test_estaciones_bicis_libres(estaciones,k=5):
    e_bicis_libres_ordenadas=estaciones_bicis_libres(estaciones,k)
    n=len(e_bicis_libres_ordenadas)

    print(f'Hay {n} estaciones con {k} o más bicis libres y las 5 primeras son:')
    for est in e_bicis_libres_ordenadas[:5]:
        print(est)

def test_estaciones_cercanas(estaciones,coordenadas):
    
    xc=coordenadas.longitud
    yc=coordenadas.latitud
    estaciones_cerca=estaciones_cercanas(estaciones,coordenadas)
    print(f'las 5 estaciones más cercanas al punto {xc}, {yc} son:')
    for est in estaciones_cerca:
        print(est)


def main():
    test_lee_estaciones('./data/estaciones.csv')
    estaciones=lee_estaciones('./data/estaciones.csv')
    test_estaciones_bicis_libres(estaciones)
    test_estaciones_bicis_libres(estaciones,10)
    test_estaciones_bicis_libres(estaciones,1)
    test_estaciones_cercanas(estaciones,Coordenadas(-5.9863,37.357659))
    mapa_estaciones=crea_mapa_estaciones(estaciones, color_azul)
    guarda_mapa(mapa_estaciones, "./out/azul.html")
    mapa_estaciones=crea_mapa_estaciones(estaciones, color_bicis_disponibles)
    guarda_mapa(mapa_estaciones, "./out/bicis_disponibles.html")
if __name__ == '__main__':
    main()