import random

def generatorPassword():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = MAYUS + MINUS + NUMS + CHARS
    password  = []
    for i in range(16):
        characters_ramdom  = random.choice(characters)
        password.append(characters_ramdom)
    password  = ''.join(password)
    #Estamos generando un string de nuestra lista
    return password

def run():
    password = generatorPassword()
    print("Your new password is: {}".format(password))


if __name__ ==  "__main__":
    run()