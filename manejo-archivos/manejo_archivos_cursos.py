#-*- coding : utf-8 -*-
from io import *
#!DESPLAZAR EL CUROS DONDE QUERRAMOS
#!METODO SEEK(5)
archivo_texto = open("archivo.txt","r+") #!lectura y escritura
# archivo_texto.seek(11) #* posiciona el punturo donde quiero
# print(archivo_texto.read(11)) #* hace una lectura hasta donde le indiquemos
# archivo_texto.seek(len(archivo_texto.read())/2) #* Ubicamos el puntero en la mitad del documento
# print(archivo_texto.read())
# archivo_texto.write("Comienzo del texto")

lista_texto  = archivo_texto.readlines()
lista_texto[1] = "Esta linea ha sido incluida desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()