from tkinter import *
from tkinter import messagebox  #!Para poder usar las alertas
root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de anthony","Procesador de texto 2020") #!(titulo-venta,info-a-mostrar)

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia SNK")

def salirAplicacion():
    # valor=messagebox.askquestion("Salir","¿Deseas salir del programa?")
    valor = messagebox.askokcancel("Salir","¿Deseas salir del programa?")
    if valor=="yes" or valor==True: 
        root.destroy()

def cerraDocumento():
    valor = messagebox.askretrycancel("Reintentar","Imposible cerrar documento")
    if valor==False: 
        root.destroy()

        
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#!Asigando a que menu corresponde,quitamos el separar de un menu vacio
archivoMenu.add_command(label="Nuevo")#!Asigando el subnivel
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator() #!Agregando un alinea separadora
archivoMenu.add_command(label="Cerrar", command=cerraDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de",command=infoAdicional)


#!Asigando el texto a los elementos del menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
root.mainloop()