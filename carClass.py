import os
import sys

def run():

    realCar = Automovil()
    while True:
        menu = '''
        ¿Que deseas hacer con tu automovil?

        [E]ncender.
        [A]pagar.
        [Ac]elerar.
        [F]renar.
        [Su]bir personas.
        [B]ajar personas.
        [C]argar nafta.
        [Mo]strar TODO.
        [S]alir.

        '''
        option = input(menu)

        if(option == 'E' or option == 'e'):
            if (realCar.is_running==False and realCar.is_turned_on==False):
                realCar.turnON()
            elif (realCar.is_running):
                realCar.statusCAR()
            elif(realCar.is_turned_on and realCar.is_running==False):
                os.system('cls')
                resp0 = input('''
                    EL AUTOMOVIL ESTA ENCENDIDO
                    ¿Deseas Apagarlo?
                    [S]í
                    [N]o

                ''')
                if(resp0=='s' or resp0=='S'):
                    realCar.is_running=False
                    realCar.turnOFF()
                    realCar.statusCAR()
                else:
                    realCar.statusCAR()

            
        elif(option == 'A' or option == 'a'):
            realCar.turnOFF()
        elif(option =='Ac' or option =='AC' or option=='ac'):
            realCar.speedUp()
        else:
            sys.exit()


class Automovil:
    _CARS = ['''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
                 `( o )----( o )-'
                   `-'      `-
                   -ENCENDIDO-''',
             '''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
                 `( o )----( o )-'
                   `-'      `-
                    -APAGADO-''',

             '''
                    _______
            _-_-  _/\______\\__
         _-_-__  / ,-. -|-  ,-.`-.
            _-_- `( o )----( o )-'
                   `-'      `-
                   --EN MARCHA--'''
             ]

    # *VAMOS A DEFINIR EL METODO INICIAL
    def __init__(self):
        self.is_turned_on = False
        self.defoult_values()

    def defoult_values(self):
        self.current_speed: 0
        self.is_running = False
        self.speed = 0
        self._capacidad_maxima_nafta = 20000
        self._nafta_level = self._capacidad_maxima_nafta
        self._velocidad_maxima = 200
        self._consumo_nafta_por_metro = 2
        self._capacidad_maxima_personas = 5
        self._personas_a_bordo = 1
        self._metros_recorridos = 0
        self._tiempo_en_viaje = 0

    def turnON(self):
        self.is_turned_on = True
        self.is_running = False
        self.statusCAR()

    def turnOFF(self):
        self.is_turned_on = False
        self.is_running = False
        self.statusCAR()

    def statusCAR(self):
        os.system('cls')
        if self.is_turned_on and self.is_running==False:
            print(self._CARS[0])
        elif self.is_running:
            print(self._CARS[2])
        else:
            print(self._CARS[1])

    def speedUp(self):
        os.system('cls')
        try:
            speedUpNumber = int(input('¿Cuanto km/h aceleraras?\n'))
            if(speedUpNumber>=0):
                if self.is_turned_on:
                    if self.speed>=self._velocidad_maxima:
                        print('Ya estas al maximo de velocidad')
                    else:
                        self.speed +=speedUpNumber
                        print('Velocidad Actual: {}'.format(self.speed))
                        self.statusCAR()
                else:
                    resp = input('''
                    NO PUEDES ACELERAR CON EL AUTOMOVIL APAGADO
                    
                    ¿Deseas enceder el Automovil?
                    [S]í
                    [N]o

                    ''')
                    if(resp=='S' or resp =='s'):
                        self.is_turned_on=True
                        self.is_running=True
                        self.statusCAR()
                    else:
                        self.turnOFF()
            else:
                print('Ingresa una velocidad válida')
                self.speed()

        except TypeError :
            print('Ingresa una velocidad válida')
            self.speed()
        

if __name__ == '__main__':
    run()
