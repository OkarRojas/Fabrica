import tkinter as tk
from tkinter import *
import PVPrin
import nav
import Animaciones
import time

PRODUCTOS = {
    "sagu": 30, "maiz": 50, "trigo": 20, "arroz": 40, "soja": 60
}

def eliminar_producto(jk ):
    # Placeholder for product deletion logic
    print("Producto eliminado")
    # Clear the canvas
    for widget in jk.winfo_children():
        widget.destroy()
 
jk = 0
def animar_productos(canvas):
    global jk
    if jk == 0:
        # liena_Menu = Animaciones.LineaAnimada(canvas, velocidad=2, x1=15, y1=75, x2=75, y2=75, tipo="horizontal")
        # liena_Menu2 = Animaciones.LineaAnimada(canvas, velocidad=2, x1=15, y1=50, x2=15, y2=100, tipo="vertical")
        # # Animar el desplazamiento del label verticalmente
        # animaciones_label = Animaciones.Animaciones_label(destroy, velocidad=30, canvas=canvas, start_y=50, end_y=100)
        # animaciones_label.animar_label_verticales()
        run = True
        xvel =3
        count = 0
        while run:

            if count > 100:
                run = False
            canvas.move(destroy, 0, xvel)
            canvas.update()
            time.sleep(0.01)
            count += 1

    else:
        animaciones_label2 = Animaciones.Animaciones_label(destroy, velocidad=30, canvas=canvas, start_y=1000, end_y=50)
        animaciones_label2.animar_label_verticales()
        jk = 0
        canvas.delete("all")
        liena_Menu4 = Animaciones.LineaAnimada(canvas, velocidad=2, x1=15, y1=75, x2=75, y2=75, tipo="horizontal")
        liena_Menu4.iniciar_animacion_horizontal_i()

# Paleta armónica
COLOR_PRINCIPAL = "#E27D0A"      # Naranja
COLOR_ANALOGO1 = "#E2B10A"       # Amarillo mostaza
COLOR_ANALOGO2 = "#E25A0A"       # Naranja rojizo
COLOR_NEUTRO_CLARO = "#FFF3E0"   # Beige claro
COLOR_NEUTRO_OSCURO = "#3E2723"  # Marrón oscuro

class MainWindow:
    def __init__(self, productos):
        self.root = tk.Tk()
        self.root.title("Rozvi")
        self.root.geometry("1280x600")
        self.root.resizable(False, False)
        self.root.configure(bg=COLOR_NEUTRO_OSCURO)

        self.productos = productos
        self.setup_ui()

    def setup_ui(self):
        nav_bar = nav.nav(photo=tk.PhotoImage(file="src\\img\\1(1).png"), title="Rozvi")
        nav_bar.create_nav(self.root)

        menuL = Canvas(self.root,  bg=COLOR_NEUTRO_OSCURO, width=200)
        menuL.pack(side=LEFT, fill=Y)
        productos = tk.Label(
            menuL,
            text="Productos",
            font=("Arial", 15),
            bg=COLOR_NEUTRO_OSCURO,
            fg="white"
        )
        productos.place(x=10, y=10)
        productos.bind("<Button-1>", lambda event: animar_productos(menuL))
        

        fron = Frame(self.root, bg=COLOR_PRINCIPAL)
        fron.pack(side=RIGHT, fill=BOTH, expand=True)

        Label(
            fron,
            text="Materias primas disponibles",
            font=("Arial", 20),
            bg=COLOR_PRINCIPAL
        ).place(x=50, y=10)
        

        ##########

        mt = Canvas(fron, bg=COLOR_ANALOGO2, highlightthickness=0)
        mt.pack(fill=BOTH, pady=(75,0), expand=True)

        self.crear_cuadros(mt)

        global destroy
        destroy = Canvas.create_text(menuL, 40, 100, text="Producto", fill="white", font=("Arial", 15), anchor="center")
        



    def crear_cuadros(self, parent):
        cols = 7
        for idx, (nombre, stock) in enumerate(self.productos.items()):
            row, col = divmod(idx, cols)
            frame = Frame(parent, bg=COLOR_NEUTRO_CLARO, highlightbackground=COLOR_NEUTRO_OSCURO, highlightthickness=1)
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            producto = PVPrin.MateriaPrima(nombre, f"Stock: {stock}", "src\\img\\1(1).png")
            cuadro = PVPrin.CuadroMateriaPrima(frame, producto)
            cuadro.mostrar()

            modificar_stock = PVPrin.ModificarStock(frame, producto)
            modificar_stock.crear_boton()

            on_click = PVPrin.VenProducto(cuadro)
            on_click.on()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MainWindow(PRODUCTOS).run()
