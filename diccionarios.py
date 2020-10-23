def run ():
    mi_diccionario = {
        "llave1" : 1,
        "llave2":2,
        "llave3":3,
    }
    # accediendo a las propiedades
    # print(mi_diccionario['llave1'])

    población_paises = {
        # podemos separar los numeros con guion
        # bajo como si fueran como de la vida real
	'Argentina': 44_938_712,
	'Brasil': 210_147_125,
	'Colombia': 50_372_424
    }
    # print(población_paises["Argentina"])
    for pais in población_paises.keys():
        print(pais)
    for valores in población_paises.values():
        print(valores)
    for paises, piblacion in población_paises.items():
        print(paises + " tiene " + str(piblacion) + " habitantes" )

if __name__ == "__main__":
    run()