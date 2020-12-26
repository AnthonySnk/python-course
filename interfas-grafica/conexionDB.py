
from tkinter import *  # !importando librerias
from tkinter import messagebox  # !Mensajes emergente
import sqlite3

def conexionBBDD():
    miconexion = sqlite3.connect("Usuarios")
    miCursor = miconexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE DATOSUSUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USER VACHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100)
        )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("!Atención¡", "La BBDD ya existe")
