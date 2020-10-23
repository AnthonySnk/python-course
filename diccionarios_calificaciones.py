# -*-coding:utf-8 -*-
def run():
    calificaciones  = {}
    calificaciones ['algoritmo']  = 9
    calificaciones ['matematicas'] = 10
    calificaciones ['web']  = 9
    calificaciones ['baseDe_Datos'] = 10
    # vamos a iterar las propiedades
    for keys in calificaciones:
        print(keys) 
    # vamos a recorrer los valores
    for valores in calificaciones.values():
        print(valores)
    # vamos a recorrer todo
    for key,value in calificaciones.items():
        print("{} ---- nota:{}".format(key,value))

if (__name__ == '__main__'):
    run()