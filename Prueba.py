from tkinter import Tk, Canvas
import time
from tkinter import Button
root = Tk()
root.title("Ventana con Canvas")
root.geometry("600x400")

canvas = Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# ejemplo: dibujar algunos elementos

i = canvas.create_text(300, 250, text="Canvas en Tkinter", font=("Arial", 16))

def mover_abajo():
    while True:
        coords = canvas.coords(i)
        canvas.move(i, 0, -1)
        root.update()
        time.sleep(0.01)

boton = Button(root, text="Mover abajo", command=mover_abajo)
boton.pack(pady=5)

root.mainloop()