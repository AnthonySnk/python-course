def run():
    counter = 0
    with open('Numeros.txt', 'w') as archivo:
        for i in range(10):
            archivo.write(str(i))


def aleph():

    palabra = input('Ingresa la palabra que deseas buscar\n')
    counter = 0
    #! imprimir todo el archivo
    # with open('alpeph.txt',encoding="utf8") as archivo1:
    #     print(archivo1.readlines())
    with open('alpephChanged.txt', encoding='utf-8') as archivo1:
        for line in archivo1:
            counter += line.count(palabra)
    print('La palabra *{}* se encuentra {} veces en el texto\n'.format(palabra, counter))
    respuesta = input("""\t¿Qué deseas hacer con las palabras?\n
    1--- Reemplazar las palabras
    2--- Eliminar las palabras
    3--- Poner todas las palabras en Mayusculas
    4--- Poner todas las palabras en Minusculas
    5--- Nada
    """)
if __name__ == '__main__':
    # run()
    aleph()
