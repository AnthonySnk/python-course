from tkinter import *
from tkinter import font
root=Tk()
myFrame=Frame(root, width=700,height=700)
myFrame.pack()
# myLabel= Label(myFrame,text="Hola alummnos de Python")
# myLabel.place(x=50,y=50)#!Nos permetira poner el label en cualquier lugar mediante cordenadas
Label(myFrame,text="Hola alummnos de Python",fg="red",font=("Comic Sans MS" , 18)).place(x=50,y=50)
myImage = PhotoImage(file="wtf.png")
Label(myFrame,image=myImage).place(x=100,y=100)
root.mainloop()