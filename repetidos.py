"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""
def run(sentence):
    seen_letters  = {}
    for idx, letter in enumerate(sentence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx,1)#Vamos a meter las letras
        else: seen_letters[letter] = (seen_letters[letter][0],seen_letters[letter][1]+1)

    final_letters =[]
    for key,value in seen_letters.items():
        if value[1] ==1:
            final_letters.append((key,value))

            # ordenando por indices
    not_repeated_letters = sorted(final_letters,key=lambda value:value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__  == '__main__':
    sentence =   input("Digite una cuenecia de carracteres:\n")
    result  = run(sentence)
    if result =='_':
        print("Todos los caracteres se repiten")
    else:
        print("El primer caracter no repetido es: {}".format(result))
