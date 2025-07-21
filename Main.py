import tkinter as tk
from tkinter import *
import claz


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



# m1 = Label(frame1, text="Materia prima 1", font=("Arial", 10), bg="#862DB9", fg="white")
# m1.place(x=0, y=0)

# s1 = Label(frame1, text="Stock: 100", font=("Arial", 10), bg="#752DB9", fg="white")
# s1.place(x=0, y=20)

# image1 = tk.PhotoImage(file="src\\img\\imagen (2).png")
# logo1 = Label(frame1, image=image1, bg="#053D38")
# logo1.image1 = image1
# logo1.place(x=0, y=3)


cuadro1 = claz.cuadro(frame1, "src\\img\\1(1).png", "Materia prima 1", "Stock: 100")
cuadro1.pre()


pWindow.mainloop()
