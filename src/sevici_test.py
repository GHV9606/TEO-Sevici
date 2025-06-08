from sevici import *

def test_lee_estaciones(fichero):
    estaciones=lee_estaciones(fichero)
    print(f'las tres primeras estaciones son:')
    for e in estaciones[:3]:
        print(e)
    print(f'las tres últimas estaciones son:')
    for e in estaciones[-3:]:
        print(e)


def test_estaciones_bicis_libres(fichero,k=5):
    
    estaciones=lee_estaciones(fichero)
    e_bicis_libres=estaciones_bicis_libres(estaciones,k)

    print(f'Hay estaciones con {k} o más bicis libres y las 5 primeras son:')
    for e in e_bicis_libres[:5]:
        print(e)




def main():
    test_lee_estaciones('./data/estaciones.csv')
    test_estaciones_bicis_libres('./data/estaciones.csv')
    test_estaciones_bicis_libres('./data/estaciones.csv',10)
    test_estaciones_bicis_libres('./data/estaciones.csv',1)


if __name__ == '__main__':
    main()