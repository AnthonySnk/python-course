import random

def run():
    numero_pensado= random.randint(1,100)
    vida= 5
    numero = int(input("Eligue un numero del 1 al 100:\n"))
    while numero != numero_pensado:
        if vida == 0:
            print("""GAME OVER
            El numero que pensé era """ + str(numero_pensado) )
            perdio = True
            break
        if numero < numero_pensado:
            vida -=1
            print("VIDAS RESTANTES "+ str(vida))
            numero = int(input("Busca un numero mas grande:\n"))

        elif numero > numero_pensado:
            vida -=1
            print("VIDAS RESTANTES "+ str(vida))
            numero = int(input("Busca un numero mas pequeño:\n"))
    if not perdio:
        print("Ganaste!")


if __name__ == "__main__":
    run()