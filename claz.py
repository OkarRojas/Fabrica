from tkinter import *
import tkinter as tk
from tkinter import ttk

class cuadro:
    
    def __init__(self, ventana, foto, nombre, stock):
        self.ventana = ventana
        self.foto = foto
        self.nombre = nombre
        self.stock = stock

    def pre(self):

        image = tk.PhotoImage(file=self.foto)
        etiqueta3 = tk.Label(self.ventana, image=image, bg="red")
        etiqueta3.image = image
        etiqueta3.grid(row=0, column=0, padx=10, pady=10)
        
        etiqueta1 = tk.Label(self.ventana, text=self.nombre, bg="lightblue")
        etiqueta1.grid(row=1, column=0, padx=10, pady=10)

        etiqueta2 = tk.Label(self.ventana, text=self.stock, bg="lightblue")
        etiqueta2.grid(row=2, column=0, padx=10, pady=10)
        
    

        
    
    
