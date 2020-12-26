import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print(f'Se ha creado una persona nueva - Nombre: {self.nombre}')

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"

class ListaPersona():
    personas = []
    
    def __init__(self):
        listaDePersonas = open("ficheroEXterno", "ab+")  # append binari
        listaDePersonas.seek(0)  # desplazando el cursos al principio
        try:
            self.personas = pickle.load(listaDePersonas)
            #!Almacenando la lectura, en try y catch porque dara error si esta vacio
            print(
                f"Se cargaron {len(self.personas)} personas del fichero externo")
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroEXterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("===========La informacion del fichero externo es:=========")
        for p in self.personas:
            print(p)


miLista = ListaPersona()
# p = Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(p)
# p = Persona("Antonio", "Masculino", 23)
# miLista.agregarPersonas(p)
# p = Persona("Ana", "Femenino", 19)
p = Persona("April", "Femenino", 19)
miLista.agregarPersonas(p)

# miLista.mostarPersonas()
miLista.mostrarInfoFicheroExterno()