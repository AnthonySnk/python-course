import pickle

lista_nombre=["Pedro","Ana","Maria","Isabel"]
fichero_binario=open("lista_nombres","wb") #Write binary
pickle.dump(lista_nombre,fichero_binario)
fichero_binario.close()
del (fichero_binario) # borramos el archivo en memoria


#!Leyendo el archivo
# import pickle
fichero_binario=open("lista_nombres","rb") #read binary
lista=pickle.load(fichero_binario)
print(lista)