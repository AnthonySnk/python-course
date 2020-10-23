# -*- coding: utf-8 -*-
import sys
import os
# import lamp 
# quedaria de esta manera
# lamp = lamb.Lamp(is_turned_on=False)
# lamp es el nombre del archivo
from lamp import Lamp,Foco
def run():
    # intanciar la clase
    lamp = Lamp(is_turned_on=False)
    while True:
        command = input('''
        ¿Qué deseas hacer?

        [p]render
        [a]pagar
        [s]alir

        ''')
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            sys.exit()


if __name__ == '__main__':
    run()
