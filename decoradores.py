# -*- coding:utf-8 -*-

def funcion_decorador(func):
    
    def funcion_interna(password):
        if password == 'platzi':
            return func()
        else:
            print('Contraseña incorrecta') 
    return funcion_interna

@funcion_decorador
def protected_func():
    print("Tu constraseña es correcta")

if __name__  == '__main__':
    password = input('Ingresa tu contraseña:\n')

    # wrapper = protected(protected_func)
    # wrapper =(password)

    protected_func(password)