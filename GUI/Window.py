
import tkinter as tk
from tkinter import *
from Workers import Engine
from GUI import Recommender
from GUI import Login



"""
Proof of concept for window creation in Python
"""

# TODO: The big decision for this file is to decide if we want a desktop app or web app


# TODO: create spaces to collect user info
# TODO: create spaces to collect movie info
# TODO: figure out how to send that data to an Engine() object
# TODO: look up drop-down menus for genres? --In progress


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for f in (Login.Login, Recommender.Recommender):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_recommender(self):
        frame = self.frames[Recommender]
        frame.tkraise()


larry = Window()