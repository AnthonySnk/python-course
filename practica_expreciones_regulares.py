import re

# cadena ="Vamos a aprender expreciones regulares en Python. Python es un lenguaje sencillo"
# # print(re.search("aprender",cadena)) 
# #parametro: texto que andamos buscando, varible
# #devuelve none si no encuentra nada

# textoBuscar ="Python"
# if re.search(textoBuscar,cadena) is not None:
#     print('He encontrado el texto')
# else:
#     print('No he encontrado el texto')

# textoGuardado = re.search(textoBuscar,cadena)
# print(textoGuardado.start()) # donde comienza
# print(textoGuardado.end()) # donde termina
# print(textoGuardado.span()) # devuelve una tupla de (start, end)

# textoGuardado = re.findall(textoBuscar,cadena) # devuelve una lista de plabra
# print(textoGuardado)
# textoGuardado = len(re.findall(textoBuscar,cadena)) # cantidad de plabra
# print(textoGuardado)

# listaNombre=[
#             'Ana Gómez',
#             'Maria Martín',
#             'Sandra López',
#             'Santiago Martín',
#             'Sandra Fernandez',
#             ]

# for elemento in listaNombre:
#     if re.findall('^Sandra',elemento): # ^  para decir que comience con 
#         print(elemento)


listaNombre=[
            'Ana',
            'Maria',
            'Sandra',
            'Santiago',
            'Sandra',
            ]

for elemento in listaNombre:
    if re.findall('[o-t]',elemento): # ^  para decir que comience con 
        print(elemento)

