import tkinter as tk



class cuadro:
    def __init__(self, ventana, foto, nombre, stock):
        self.ventana = ventana
        self.lado = foto
        self.nombre = nombre
        self.stock = stock

    def pre(self):

        image = tk.PhotoImage(file=self.lado)
        etiqueta3 = tk.Label(self.ventana, image=image, bg="lightgreen")
        etiqueta3.grid(column=1, row=2)
        
        etiqueta1 = tk.Label(self.ventana, text=self.nombre, bg="lightblue")
        etiqueta1.grid(column=2, row=0)

        etiqueta2 = tk.Label(self.ventana, text=self.stock, bg="lightblue")
        etiqueta2.grid(column=1, row=1)

        
    

        
    
    
