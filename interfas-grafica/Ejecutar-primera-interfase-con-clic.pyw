from tkinter import * #!Invocando el modulo

raiz=Tk() #!Es como tener un boton infinito

raiz.title("Ventana de pruebas") #? poniendole titulo a la ventana
raiz.resizable(1,0) #?Redimencionar la ventana, ancho-alto (true,false)
raiz.iconbitmap("gingerbread_man.ico")  #?Nuestro icono
raiz.geometry("650x350")    #?Damos el tamoño deseado
raiz.config(bg="#e43445")     #?ASignando un color a la ventana
raiz.mainloop() #!Esta a la escucha de una accion, siempre dejarlo al final