from tkinter import *  # !importando librerias
from tkinter import messagebox  # !Mensajes emergente
import sqlite3
from conexionDB import *

# ====================FUNCIONES=================
def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor == 'yes':
        root.destroy()


def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPassword.set("")
    # apartir del primer caracter hasta el final
    textComentario.delete(1.0, END)


def crear():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    try:
        varGestion = (miNombre.get(), miPassword.get(), miApellido.get(
        ), miDireccion.get(), textComentario.get('1.0', END))

        micursor.execute(
            'INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)', varGestion)
        miconexion.commit()
        messagebox.showinfo("Listo!", "Registro insertado con éxito")
    except Exception as e:
        print(e)
        messagebox.showerror("Error!", "Ocurrio un error en BBDD")


def leer():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()
    try:
        micursor.execute('SELECT * FROM DATOSUSUARIOS WHERE ID=' + miId.get())
        elUsuario = micursor.fetchall()
        for user in elUsuario:
            miId.set(user[0])
            miNombre.set(user[1])
            miPassword.set(user[2])
            miApellido.set(user[3])
            miDireccion.set(user[4])
            textComentario.insert(1.0, user[5])
            miconexion.commit()
    except Exception as e:
        print(e)
        messagebox.showerror("Error!", "Ocurrio un error en BBDD")


def actualizar():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()
    varGestionActualizar = (miNombre.get(), miPassword.get(), miApellido.get(
        ), miDireccion.get(), textComentario.get('1.0', END))
    try:
        # micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USER='" + miNombre.get() + "',PASSWORD='" + miPassword.get() +
        # "',APELLIDO='"+miApellido.get() +
        # "',DIRECCION='"+miDireccion.get() +
        # "',COMENTARIOS='"+textComentario.get(1.0, END) +
        # "'WHERE ID="+miId.get())
        micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USER=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID="+miId.get(),varGestionActualizar)
        miconexion.commit()
        messagebox.showinfo("Listo!", "Registro Actualizado con éxito")

    except Exception as e:
        print(e)
        messagebox.showerror("Error!", "Ocurrio un error en BBDD")

def eliminar():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()
    try:
        micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
        miconexion.commit()
        messagebox.showinfo("Listo!", "Registro eliminado con éxito")
    except Exception as e:
        print(e)
        messagebox.showerror("Error!", "Ocurrio un error en BBDD")


# ===========================================================
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# ====================COMIENZO DE MENU=======================
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ====================COMIENZO DE CAMPOS==================
miFrame = Frame(root)
miFrame.pack()

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPassword = StringVar()
miDireccion = StringVar()

cuadroId = Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPassword = Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textComentario = Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)

# =========================COMIENZAN LOS LABELS==============
idLabel = Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel = Label(miFrame, text="Password: ")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# =========================COMIENZAN LOS BOTONES=================
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
