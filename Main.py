import tkinter as tk
from tkinter import *
import claz

def abrir_ventana(event):
    nueva_ventana = tk.Tk() 
    nueva_ventana.title("Nueva ventana")
    nueva_ventana.geometry("300x200")
    etiqueta = tk.Label(nueva_ventana, text="Esta es una nueva ventana")
    etiqueta.pack(pady=20)

pWindow = tk.Tk()  
pWindow.title("Rozvi")
pWindow.geometry("1280x600")
pWindow.resizable(False, False)
pWindow.configure(bg="#A3CCAB")

menuf = Frame(pWindow, height=75, bg="#053D38") 
menuf.pack(side=TOP, fill=X)

image = tk.PhotoImage(file="src\\img\\1(1).png")
logo = Label(menuf, image=image, bg="#053D38")
logo.image = image
logo.pack(padx=10, side=LEFT)

titulo = Label(menuf, text="Rozvi", font=("Arial", 30), bg="#053D38", fg="white")
titulo.pack(padx=10, side=LEFT)

menuL = Frame(pWindow, width=200, bg="#34675C")
menuL.pack(side=LEFT, fill=Y)

fron = Frame(pWindow, bg="#A3CCAB")
fron.pack(side=RIGHT, fill=BOTH, expand=True)

mat = Label(fron, text="Materias primas disponibles", font=("Arial", 20), bg="#A3CCAB", fg="black")
mat.place(x=50, y=10)

mt = Frame(fron, bg="#B92D39")
mt.pack(fill=BOTH, pady=(75,0), expand=True)

frame1 = Frame(mt, bg="#ffffff")
frame1.pack(padx=50, pady=30, expand=True)

producto1 = claz.MateriaPrima("Materia prima 1", "Stock: 100", "src\\img\\1(1).png")
cuadro1 = claz.CuadroMateriaPrima(frame1, producto1)
cuadro1.mostrar()



modificar_stock = claz.ModificarStock(frame1, producto1)
modificar_stock.crear_boton()




pWindow.mainloop()
