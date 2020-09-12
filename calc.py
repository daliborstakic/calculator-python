""" Importing tkinter """
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar

class CalcApp:
    """ Calculator app """
    def __init__(self, root):
        """ Init class """
        self.root = root
        root.title("Calculator")

        # Equation
        equation = StringVar()

        # Equation entry fields
        self.first_entry = Entry(root, textvariable=equation)
        self.first_entry.grid(columnspan=4, ipadx=70, pady=(5, 0))

        # Setting initial value
        equation.set("Enter your expression")

        # Button first row
        self.button1 = Button(root, text=" 1 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=1, column=0)
        self.button2 = Button(root, text=" 2 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=1, column=1)
        self.button3 = Button(root, text=" 3 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=1, column=2)
        self.add_button = Button(root, text=" + ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=1, column=3)

        # Second row
        self.button4 = Button(root, text=" 4 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=2, column=0)
        self.button5 = Button(root, text=" 5 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=2, column=1)
        self.button6 = Button(root, text=" 6 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=2, column=2)
        self.subtract_button = Button(root, text=" - ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=2, column=3)

        # Third row
        self.button7 = Button(root, text=" 7 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=3, column=0)
        self.button8 = Button(root, text=" 8 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=3, column=1)
        self.button9 = Button(root, text=" 9 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=3, column=2)
        self.multiple_button = Button(root, text=" + ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=3, column=3)

        # Fourth row
        self.button0 = Button(root, text=" 0 ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=4, column=0, pady=(0,5))
        self.clear_button = Button(root, text="Clear", width=7, height=1, bg="#D4C13D", fg="white").grid(row=4, column=1, pady=(0,5))
        self.equal_button = Button(root, text=" = ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=4, column=2, pady=(0,5))
        self.divide_button = Button(root, text=" / ", width=7, height=1, bg="#D4C13D", fg="white").grid(row=4, column=3, pady=(0,5))

# Creating the app
root = tk.Tk()
calc_app = CalcApp(root)

# Tkinter mainloop
if __name__ == '__main__':
    root.mainloop()
