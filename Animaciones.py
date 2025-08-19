import tkinter as tk   # Importamos tkinter para la interfaz gráfica
import time

class LineaAnimada:
    def __init__(self, canvas, velocidad=50, x1=0, y1=0, x2=0, y2=0, tipo="vertical"):

        self.canvas = canvas
        self.velocidad = velocidad
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.tipo = tipo

        # Variables para controlar la línea animada
        self.linea = None        # Guardará el objeto línea del canvas
        self.y_actual = 0        # Posición actual de la parte baja de la línea
        self.altura_max = self.y2    # Hasta dónde crecerá la línea

        # Al crear la clase, se inicia automáticamente la animación
        if self.tipo == "vertical":
            self.iniciar_animacion()
        elif self.tipo == "horizontal":
            self.iniciar_animacion_horizontal()
        else:
            raise ValueError("Tipo de animación no soportado. Use 'vertical' o 'horizontal'.")
##############################################################################

##############################################################################
        

    def iniciar_animacion(self):
        # Limpiamos el canvas (por si hubiera algo dibujado antes)
        #self.canvas.delete("all")

        # Creamos la línea inicial (empieza sin longitud)
        self.linea = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="white", width=3)

        # La parte inferior de la línea comienza en Y=50 (igual que arriba)
        self.y_actual = 50

        # Iniciamos el proceso de animación
        self.animar()

    def animar(self):
        # Mientras la línea no haya llegado a la altura máxima...
        if self.y_actual < self.altura_max:
            # Incrementamos la posición de la parte baja de la línea (crece hacia abajo)
            self.y_actual += 1

            # Actualizamos las coordenadas de la línea en el canvas
            self.canvas.coords(self.linea, self.x1, self.y1, self.x2, self.y_actual)

            # Volvemos a llamar a "animar" después de cierto tiempo
            self.canvas.after(self.velocidad, self.animar)

    def iniciar_animacion_horizontal(self):
        # Limpiamos el canvas (por si hubiera algo dibujado antes)
        self.canvas.delete("all")

        # Creamos la línea inicial (empieza sin longitud)
        self.linea = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="white", width=3)

        # La parte derecha de la línea comienza en X=15 (igual que la izquierda)
        self.x_actual = 15
        self.ancho_max = self.x2

        # Iniciamos el proceso de animación
        self.animar_horizontal()

    def animar_horizontal(self):
        # Mientras la línea no haya llegado al ancho máximo...
        if self.x_actual < self.ancho_max:
            # Incrementamos la posición de la parte derecha de la línea (crece hacia la derecha)
            self.x_actual += 1

            # Actualizamos las coordenadas de la línea en el canvas
            self.canvas.coords(self.linea, self.x1, self.y1, self.x_actual, self.y2)

            # Volvemos a llamar a "animar" después de cierto tiempo
            self.canvas.after(self.velocidad, self.animar_horizontal)
    
    ################################################################################

    ################################################################################

    ################################################################################

    def iniciar_animacion_i(self):
        # Limpiamos el canvas (por si hubiera algo dibujado antes)
        #self.canvas.delete("all")

        # Creamos la línea inicial (empieza sin longitud)
        self.linea = self.canvas.create_line(15, 50, 15, 50, fill="white", width=3)

        # La parte inferior de la línea comienza en Y=50 (igual que arriba)
        self.y_actual = 50

        # Iniciamos el proceso de animación
        self.animar_i()

    def animar_i(self):
        # Mientras la línea no haya llegado a la altura máxima...
        if self.y_actual < self.altura_max:
            # Incrementamos la posición de la parte baja de la línea (crece hacia abajo)
            self.y_actual -= 1

            # Actualizamos las coordenadas de la línea en el canvas
            self.canvas.coords(self.linea, self.x1, self.y1, self.x2, self.y_actual)

            # Volvemos a llamar a "animar" después de cierto tiempo
            self.canvas.after(self.velocidad, self.animar)

    def iniciar_animacion_horizontal_i(self):
        # Limpiamos el canvas (por si hubiera algo dibujado antes)
        self.canvas.delete("all")

        # Creamos la línea inicial (empieza sin longitud)
        self.linea = self.canvas.create_line(15, 50, 15, 50, fill="white", width=3)

        # La parte derecha de la línea comienza en X=15 (igual que la izquierda)
        self.x_actual = 15
        self.ancho_max = self.x2

        # Iniciamos el proceso de animación
        self.animar_horizontal_i()

    def animar_horizontal_i(self):
        # Mientras la línea no haya llegado al ancho máximo...
        if self.x_actual < self.ancho_max:
            # Incrementamos la posición de la parte derecha de la línea (crece hacia la derecha)
            self.x_actual -= 1

            # Actualizamos las coordenadas de la línea en el canvas
            self.canvas.coords(self.linea, self.x1, self.y1, self.x_actual, self.y2)

            # Volvemos a llamar a "animar" después de cierto tiempo
            self.canvas.after(self.velocidad, self.animar_horizontal_i)


class Animaciones_label:
    def __init__(self, label, velocidad=50, canvas=None, start_y=50, end_y=150, start_x=10, end_x=100):
        self.label = label
        self.velocidad = velocidad
        self.canvas = canvas
        self.start_y = start_y
        self.end_y = end_y
        self.start_x = start_x
        self.end_x = end_x

    def animar_label_verticales(self):
        delta_y = (self.end_y - self.start_y) / 20

        def mover(paso=0):
            if paso <= 20:
                y = int(self.start_y + delta_y * paso)
                self.label.place(x=self.start_x, y=y)
                self.canvas.after(self.velocidad, lambda: mover(paso + 1))
                paso += 1
        mover()
        