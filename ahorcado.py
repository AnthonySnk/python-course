
# -*- coding: utf-8 -*-
import random
import os
IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'democracia',
    'computadora',
    'almuada',
    'rabia',
    'enojo',
]


def ramdom_word():
    idx = random.randint(0,len(WORD)-1)
    return WORD[idx]

def display_board(hidden_word,tries):
    os.system('cls')  
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('')


def run():
    word = ramdom_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word,tries)
        current_letter =input("Escribe una letra:\n")

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes)== 0:
            tries +=1
            if tries ==7:
                print('')
                print('GAME OVER')
                print('La palabra correcta era: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx]  = current_letter
            letter_indexes = []

        try:
            hidden_word.index('-')    
        except ValueError:
            print('')
            print('!FELICIDADES GANASTE!')
            print('La palabra es: {}'.format(word) )
            break

if __name__ == '__main__':
    print("BIENVENIDO A AHORCADOS GAME")
    run()