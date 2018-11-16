

# this will be the new script that runs the whole program

# create a Login() object
# if login is successful, create a Recommender() object

import tkinter as tk
from tkinter import *
from Workers import Engine

"""
Proof of concept for window creation in Python
"""

# TODO: The big decision for this file is to decide if we want a desktop app or web app


# TODO: create spaces to collect user info
# TODO: create spaces to collect movie info
# TODO: figure out how to send that data to an Engine() object
# TODO: look up drop-down menus for genres? --In progress


def click():
    title = title_entry.get()
    title_entry.delete(0, END)
    movie_out.insert(END, title)


def change_genre(*args):
    print(chosen_genre.get())


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

genres = ['Action', 'Adventure', 'Animation' 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science'
          'Thriller', 'War', 'Western']

chosen_genre = StringVar(window)
# sets the default genre to 'Action'
chosen_genre.set(genres[0])
genre_menu = OptionMenu(window, chosen_genre, *genres)
Label(window, text='Choose a genre').grid(row=6, column=1)
genre_menu.grid(row=7, column=1)

chosen_genre.trace('w', change_genre)

window.mainloop()
