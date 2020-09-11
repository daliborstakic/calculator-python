""" Importing tkinter """
import tkinter as tk
from tkinter import Entry, Label

class CalcApp:
    """ Calculator app """
    def __init__(self, root):
        """ Init class """
        self.root = root
        root.title("Calculator")

        # Number entry fields
        self.first_label = Label(root, text="First number:").grid(row=0, column=0, padx=5, pady=5)
        self.first_entry = Entry(root)

        self.first_entry.grid(row=0, column=1, pady=5, padx=5)

        self.second_label = Label(root, text="Second number:").grid(row=1, column=0, padx=5, pady=5)
        self.second_entry = Entry(root)

        self.second_entry.grid(row=1, column=1, pady=5, padx=5)

# Creating the app
root = tk.Tk()
calc_app = CalcApp(root)

# Tkinter mainloop
if __name__ == '__main__':
    root.mainloop()
