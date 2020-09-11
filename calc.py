""" Importing tkinter """
import tkinter as tk
from unicodedata import name

class CalcApp:
    """ Calculator app """
    def __init__(self, root):
        """ Init class """
        self.root = root
        root.title("Calculator")

# Creating the app
root = tk.Tk()
calc_app = CalcApp(root)

# Tkinter mainloop
if __name__ == '__main__':
    root.mainloop()
