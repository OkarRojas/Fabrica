from tkinter import *
import tkinter as tk
from tkinter import ttk

class MateriaPrima:
    def __init__(self, nombre, stock, foto):
        self.nombre = nombre
        self.stock = stock
        self.foto = foto

class CuadroMateriaPrima:
    def __init__(self, ventana, materia_prima):
        self.ventana = ventana
        self.materia_prima = materia_prima

    def mostrar(self):
        image = tk.PhotoImage(file=self.materia_prima.foto)

        etiqueta3 = tk.Label(self.ventana, image=image, bg="white")
        etiqueta3.image = image
        etiqueta3.grid(row=0, column=0, padx=10, pady=0)
        
        etiqueta1 = tk.Label(self.ventana, text=self.materia_prima.nombre, bg="lightblue")
        etiqueta1.grid(row=1, column=0, padx=10, pady=0 )

        etiqueta2 = tk.Label(self.ventana, text=self.materia_prima.stock, bg="lightblue")
        etiqueta2.grid(row=2, column=0, padx=10, pady=0)


class ModificarStock:
    def __init__(self, ventana, materia_prima):
        self.ventana = ventana
        self.materia_prima = materia_prima

    def modificarm(self):
        stock = int(self.materia_prima.stock.split(": ")[1])  # Example modification
        stock -= 10
        self.materia_prima.stock = f"Stock: {stock}"
        for widget in self.ventana.grid_slaves(row=2, column=0):
            if isinstance(widget, tk.Label):
                widget.config(text=self.materia_prima.stock)

    def modificarp(self):
        stock = int(self.materia_prima.stock.split(": ")[1])  # Example modification
        stock += 10
        self.materia_prima.stock = f"Stock: {stock}"
        for widget in self.ventana.grid_slaves(row=2, column=0):
            if isinstance(widget, tk.Label):
                widget.config(text=self.materia_prima.stock)

    def crear_boton(self):

        celda = tk.Frame(self.ventana)
        celda.grid(row=3, column=0)

        boton_modificar = tk.Button(celda, text="-", command=self.modificarm)
        boton_modificar.pack(side=LEFT, padx=10, pady=0)

        boton_modificarp = tk.Button(celda, text="+", command=self.modificarp)
        boton_modificarp.pack(side=LEFT, padx=10, pady=10)

class VenProducto:
    def __init__(self, CuadroMateriaPrima):
        self.ventana = CuadroMateriaPrima.ventana
        
    def on (self):
        self.ventana.bind("<Button-1>", self.mostrar)
        
    def mostrar(self, event):

        nueva_ventana = tk.Tk() 
        nueva_ventana.title("Nueva ventana")
        nueva_ventana.geometry("300x200")
        etiqueta = tk.Label(nueva_ventana, text="Esta es una nueva ventana")
        etiqueta.pack(pady=20)
        

        