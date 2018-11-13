import tkinter as tk
import os

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        label = tk.Label(self, text='Enter login information')
        label.pack(pady=10, padx=10)
        username = tk.Entry(parent, width=20, bg='white')
        #password = tk.Entry(parent, width=20, bg='white')
        button = tk.Button(self, text='Login')
        #button = tk.Button(self, text="Login", command=self.attempt_login(username))
        button.pack()

    def attempt_login(self, username):
        userstorage = os.path.join(os.getcwd(), 'UserStorage')
        # TODO: if username exists in the 'database', then print login successful and show next screen
        # if username does not exist, ask user if they want to create a new account or try again
        if os.path.isfile(os.path.join(userstorage, username)):
            # not sure how this works with tk.Button()
            self.controller.show_frame(Recommender)
        return False
