from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfile(title="Abrir archivo",initialdir="C://",filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los Ficheros","*")))
    print(fichero) #!<_io.TextIOWrapper name='Z:/Admin/Escritorio/nombreArchivo.txt' mode='r' encoding='cp1252'>

Button(root,text="Abrir fichero",command=abreFichero).pack()

root.mainloop()