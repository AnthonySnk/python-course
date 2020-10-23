# importando librerias a usar 
from flask import Flask

# creando una instancia de Flask 
app  = Flask(__name__)

# le decimos la ruta donde lo correremos  
@app.route('/')
def hello_world():
    return "Hola, mundo 👱‍♂️"

if __name__== '__main__':
    app.run()
