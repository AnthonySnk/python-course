import pickle
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True
    
    def estado(self):
        print(f"""
        =======================
            Marca: {self.marca}
            Modelo: {self.modelo}
            En marcha: {self.enMarcha}
            Acelerando: {self.acelera}
            Frenando: {self.frena}
        ======================
        """)
fichero=open("loscoches","rb")
miscoches = pickle.load(fichero)
fichero.close()

for c in miscoches:
    print(c.estado())