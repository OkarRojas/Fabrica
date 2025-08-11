import tkinter as tk
from tkinter import *
import PVPrin
import nav

pWindow = tk.Tk()  
pWindow.title("Rozvi")
pWindow.geometry("1280x600")
pWindow.resizable(False, False)
pWindow.configure(bg="#A3CCAB")

productos ={"sagu":30, "maiz":50, "trigo":20, "arroz":40, "soja":60}

nav = nav.nav(photo=tk.PhotoImage(file="src\\img\\1(1).png"), title="Rozvi")##Encabezado de la ventana
nav.create_nav(pWindow)

menuL = Frame(pWindow, width=200, bg="#198870")
menuL.pack(side=LEFT, fill=Y)


fron = Frame(pWindow, bg="#A3CCAB")
fron.pack(side=RIGHT, fill=BOTH, expand=True)

mat = Label(fron, text="Materias primas disponibles", font=("Arial", 20), bg="#A3CCAB", fg="black")
mat.place(x=50, y=10)

mt = Canvas(fron, bg="#B92D39")
mt.pack(fill=BOTH, pady=(75,0), expand=True)

cont = 0
cont2 = 0

print("Productos:", len(productos))

for i in productos:
    if cont != 0 and cont % 3 == 0:
        cont2 += 1
        cont = 0
    else:
        pass
    frame = Frame(mt, bg="#ffffff")
    frame.grid(row=cont2, column=cont, padx=10, pady=10, sticky="nsew")
    cont += 1
    producto = PVPrin.MateriaPrima(i, f"Stock: {productos[i]}", "src\\img\\1(1).png")
    cuadro = PVPrin.CuadroMateriaPrima(frame, producto)
    cuadro.mostrar()

    modificar_stock = PVPrin.ModificarStock(frame, producto)
    modificar_stock.crear_boton()

    on_click = PVPrin.VenProducto(cuadro)
    on_click.on()


pWindow.mainloop()
