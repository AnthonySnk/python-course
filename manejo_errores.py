# -*- coding: utf-8 -*-
countries = {
    'venezuela': 31,
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}
def run():
    while True:
        country= input('Escribe el nombre del pais: ').lower()
        try:
            print('La poblacion de {} es: {} millones'.format(country,countries[country]))
        except KeyError:
            poblacion  = input('No tenemos el dato de la poblacion de {}\n¿Deseas agregar población a este pais?\n'.format(country))

if __name__ == '__main__':
    run()