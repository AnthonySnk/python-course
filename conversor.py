def conversor(tipo_pesos, valor_dollar):
    pesos  = input("¿Cuantos pesos " +tipo_pesos+ " tienes?\n")
    pesos = float(pesos)
    dolares = pesos/valor_dollar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas a dolares 😃

1 - Pesos Colombianos 
2 - Pesos Argentino
3 - Pesos Mexicanos

Elige una opcion:
"""
opcion = input(menu) 
if opcion=='1':
    conversor("Colombianos",3875)
elif opcion=='2':
    conversor("Argentinos",65)
elif opcion=='3':
    conversor("Mexicanos",24)

