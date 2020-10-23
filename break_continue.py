def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     # no se ejecutara la linea siguiente
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         # corta por completo el ciclo
    #         break
    # texto = input('Escribe un texto: \n')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    # desafio 
    LIMITE = 1000
    contador = 0

    while contador <= LIMITE:
        contador += 1
        if contador == 500:
            # no imprimira el 500
            continue
        elif contador == 510:
            # terminara el proceso
            break
        else:
            print(contador)



    

if __name__ == '__main__':
    run()