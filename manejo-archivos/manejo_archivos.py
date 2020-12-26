from io import *

#!ESCRIBIENDO EN UN ARCHIVO
archivo_texto = open("archivo.txt", "w") # Abirendo archivo en modo escritura
frase = "Estupendo dia para estudiar pyhton\nSabado"
archivo_texto.write(frase)
archivo_texto.close()

#!lEYENDO UN ARCHIVO
archivo_texto = open("archivo.txt","r")
texto = archivo_texto.read()
archivo_texto.close()
print(texto)

#!Almacenando cada linea de texto en una lista
archivo_texto = open("archivo.txt","r")
texto = archivo_texto.readlines() #lista de texto manipulables
archivo_texto.close()
print(texto)
print(texto[0])

#!Abrir un archivo para agregar informacion
archivo_texto = open("archivo.txt","a") # a == append ==añadir, agregar
archivo_texto.write("\nSimpre es una buena ocación para aprender py")
archivo_texto.close()
