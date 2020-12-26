from tkinter import *

root=Tk()
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()
minombre=StringVar()

#?==========================================
            #?TODOS LOS TXTBOX
#?==========================================

cuadroNombre=Entry(miFrame,textvariable=minombre)
#Asociamos el cuador con una variable
#!Crear una cuadricula en el frame (row, column)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDirecion=Entry(miFrame)
cuadroDirecion.grid(row=3, column=1, padx=10, pady=10)

cuadroComentario=Text(miFrame,width=16,height=5)
cuadroComentario.grid(row=4,column=1,padx=10,pady=10)

#?==========================================
#?Creamos un scrol para el cuadro de tExto
#?==========================================

scrollVert=Scrollbar(miFrame,command=cuadroComentario.yview)
#Para que se adapte al tamaño del cuadroComentario
scrollVert.grid(row=4,column=2 ,sticky="nsew")
#Para que siga el curzor la varra
cuadroComentario.config(yscrollcommand=scrollVert.set) 


#?==========================================
            #?TODOS LOS LABELS
#?==========================================

nombreLabel=Label(miFrame, text="Nombre:")  # Valor del Label
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10) # !sticky es para alinear el texto
passwordLabel=Label(miFrame, text="Password")
passwordLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)


#?==========================================
            #?TODOS LOS BOTONES
#?==========================================
def codigoBoton():
    minombre.set('Anthony')
#El parametro commando es lo que hara el boton
botonEnvio=Button(root,text="Enviar",command=codigoBoton) 
botonEnvio.pack()



root.mainloop()
