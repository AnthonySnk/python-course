def crearTabla(tabla):
    # contador = 1
    # while contador <= 10:
    #     resultado = tabla*contador
    #     print(str(tabla) + "X" + str(contador) + "=" + str(resultado))
    #     contador = contador +1
    for i in range(1,11):
        resultado = tabla*i
        print(str(tabla) + "X" + str(i) + "=" + str(resultado))

def run():
    menu = """     Hola terricola! 😎
    Escribe el numero del que deseas una tabla
    de multiplicar hasta el 10:\n"""
    tabla = int(input(menu))

    crearTabla(tabla)
    

if __name__ == '__main__':
    run()