import tkinter as tk


class Recommender(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Movie Recommender')
        label.pack(pady=10, padx=10)
        logout = tk.Button(self, text='Logout', command=lambda: controller.show_frame(Login))
        logout.pack()
        # this is where we throw all of the recommendation logic
