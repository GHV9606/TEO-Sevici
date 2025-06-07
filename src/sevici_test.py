from sevici import *

def test_lee_estaciones(fichero):
    estaciones=lee_estaciones(fichero)
    print(f'las tres primeras estaciones son:')
    for e in estaciones[:3]:
        print(e)
    print(f'las tres últimas estaciones son:')
    for e in estaciones[:-3]:
        print(e)

def main():
    test_lee_estaciones('./data/estaciones.csv')


if __name__ == '__main__':
    main()