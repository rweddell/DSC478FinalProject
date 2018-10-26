
import tkinter as tk
from tkinter import *
from Workers import Engine

"""
Proof of concept for window creation in Python
"""

# TODO: create spaces to collect user info
# TODO: create spaces to collect movie info
# TODO: figure out how to send that data to an Engine() object

# does this need to generate a class or can it run as a script?


def click():
    title = title_entry.get()
    title_entry.delete(0, END)
    movie_out.insert(END, title)


window = tk.Tk()
window.title('Greatest Movie Recommender Ever')
window.minsize(500, 500)
window.configure(background='grey')

Label(window, bg='grey', text='Input a movie or genre').grid(row=0, column=1, sticky=W)

title_entry = Entry(window, width=20, bg='white')
title_entry.grid(row=2, column=1, sticky=W)

movie_out = Text(window, width=20, height=1, background='grey')
movie_out.grid(row=5, column=1, sticky=W)

Button(window, text='SUBMIT', width=6, command=click).grid(row=3, column=1, sticky=W)


window.mainloop()
