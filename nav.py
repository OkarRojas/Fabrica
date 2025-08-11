from tkinter import *
import tkinter as tk

class nav:
    def __init__(self, photo, title):
        self.photo = photo
        self.title = title

    def create_nav(self, window):
        nav_frame = Frame(window, bg="#34675C")
        nav_frame.pack(side=TOP, fill=X)

        logo = Label(nav_frame, image=self.photo, bg="#34675C")
        logo.image = self.photo
        logo.pack(padx=10, side=LEFT)

        title_label = Label(nav_frame, text=self.title, font=("Arial", 30), bg="#34675C", fg="white")
        title_label.pack(padx=10, side=LEFT)

        return nav_frame