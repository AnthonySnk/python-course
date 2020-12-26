from tkinter import * #!Invocando el modulo

raiz=Tk() #!Es como tener un boton infinito

#? poniendole titulo a la ventana
raiz.title("Ventana de pruebas") 
#?Redimencionar la ventana, ancho-alto (true,false)
raiz.resizable(1,1) 
#?Nuestro icono
raiz.iconbitmap("gingerbread_man.ico") 
#?Damos el tamoño deseado
raiz.geometry("650x350")
#?ASignando un color a la ventana
raiz.config(bg="#e43445")
#?Creamos un frame
miFrame=Frame()
#?Rellenar la raiz con el frame x,y,both,
# miFrame.pack(fill="both", expand="True")
#?en paquetar nuestro frame en la raiz
miFrame.pack() #el frame se pega arriba,centro de la raiz
# miFrame.pack(side="right") #el frame se pega derecha,centro de la raiz
# miFrame.pack(side="right",anchor="n") #archivo equivale a los puntos cardinales
#?Fondo para el frame
miFrame.config(bg="#ff20cc")
#?dandole tamaño al frame
miFrame.config(width="650",height="350")
#?Tamaño del border
miFrame.config(bd="35")
#?Tipo de borde para el frame
miFrame.config(relief="groove")
#?Cambiar curso dentro del frame
miFrame.config(cursor="pirate")

raiz.mainloop() #!Esta a la escucha de una accion, siempre dejarlo al final