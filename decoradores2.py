
def function_decoradora(funcion_parametro):

    """Estamos creando una funcion decoradora"""
    # funcion_parametro es la funcion que deseamos decorar
    def function_interior(*args,**kwargs):

        # Acciones Adicionales que decorar
        print('Vamos a realizar un calculo:')

        funcion_parametro(*args,**kwargs)
        # function_decoradora => EJECUTAMOS LA FUNCTION SUMA
        # Acciones adicionales que decoran

        print('Hemos terminado el calculo')

    return function_interior


@function_decoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)


@function_decoradora
def resta(num1,num2):
    print(num1-num2)

@function_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))


if __name__ =='__main__':
    suma(7,5,1)
    resta(9,10)
    potencia(5,3)
    potencia(base=5 ,exponente=4)
    print(function_decoradora.__doc__)
    help(function_decoradora)
