from tkinter import *
from typing import Sized

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montania=IntVar()
turismo=IntVar()

def opcionViaje():
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida+=" playa"
    if montania.get()==1:
        opcionEscogida+=" montaña"
    if turismo.get()==1:
        opcionEscogida+=" turismo rural"
    
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="wtf.png")
# Label(root,image=foto).pack()#!empaquetando la imagen

frame=Frame(root)
frame.pack()
Label(frame,text="Elige destinos", width=50).pack()

Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionViaje).pack()
Checkbutton(frame,text="Montaña",variable=montania,onvalue=1,offvalue=0,command=opcionViaje).pack()
Checkbutton(frame,text="Turismo rural",variable=turismo,onvalue=1,offvalue=0,command=opcionViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()