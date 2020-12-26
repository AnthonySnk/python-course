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

coche1 =Vehiculos("Mazda","MX5")
coche2 =Vehiculos("Seat","Leon")
coche3 =Vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]

#!SERAILIZANDO OBJETOS
fichero=open("loscoches","wb")#escribiendo byte
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

#!LEYENDO LOS OBJETOS SERIALIZADOS

fichero=open("loscoches","rb")
miscoches = pickle.load(fichero)
fichero.close()

for c in miscoches:
    print(c.estado())