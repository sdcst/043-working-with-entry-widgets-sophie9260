"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.constants import SUNKEN

def math(event):

    A = abox.get()
    B = bbox.get()
    C = cbox.get()
    X = plus1.get()
    Y = plus2.get()

    if A == "1":
        A = float(A)
        error.config(text="Errors will display in the terminal.")    
    else:
        print("Oh no! the value of \"a\" can only be \"1\".")

    if X == "+" or X == "-":
        pass
    else:
        print("Oh no! please select + or - for both comboboxes.")

    try:
        B = float(B)
        C = float(C)
        error.config(text="Errors will display in the terminal.")
    except:
        print("Oh no! the value of \"b\" or/and \"c\" are not valid.")
    
    if X == "+" and Y == "+":
        under = ((B**2)-(4*A*C))**0.5
        add = ((-B)+under)/(2*A)
        print(f"{add}")
        minus = ((-B)-under)/(2*A)
        print(f"{minus}")
        boxe1.delete(0,tk.END)
        boxe1.insert(0,add)

        boxe2.delete(0,tk.END)
        boxe2.insert(0,minus)

    elif X == "+" and Y == "-":
        C = -1*C
        under = ((B**2)-(4*A*C))**0.5
        add = ((-B)+under)/2*A
        print(f"{add}")
        minus = ((-B)-under)/2*A
        print(f"{minus}")
        boxe1.delete(0,tk.END)
        boxe1.insert(0,add)

        boxe2.delete(0,tk.END)
        boxe2.insert(0,minus)

    elif X == "-" and Y == "+":
        B = -1*B
        under = ((B**2)-(4*A*C))**0.5
        add = ((-B)+under)/2*A
        print(f"{add}")
        minus = ((-B)-under)/2*A
        print(f"{minus}")
        boxe1.delete(0,tk.END)
        boxe1.insert(0,add)

        boxe2.delete(0,tk.END)
        boxe2.insert(0,minus)
        
    elif X == "-" and Y == "-":
        B= -1*B
        C = -1*C
        under = ((B**2)-(4*A*C))**0.5
        add = ((-B)+under)/2*A
        print(f"{add}")
        minus = ((-B)-under)/2*A
        print(f"{minus}")

        boxe1.delete(0,tk.END)
        boxe1.insert(0,add)

        boxe2.delete(0,tk.END)
        boxe2.insert(0,minus)

    
win = tk.Tk()
win.attributes('-topmost',True)
win.geometry("380x170")

instruction = tk.Label(win, text="This interface will help factor a trinomial of the type \"ax^2 + bx + c\".\n\"a\" will always remain to be \"1\". \nIf value of \"b\" or \"c\" is negative, \nplease enter the value positive and change the + sign as the - sign. ")

abox = tk.Entry(win, text="value of a", width=5)
bbox = tk.Entry(win, text="value of b", width=5)
cbox = tk.Entry(win, text="value of c", width=5)

Abox = tk.Label(win, text="X^2")
Bbox = tk.Label(win, text="X")


plus1 = ttk.Combobox(win, values=["+","-"], width=3)
plus2 = ttk.Combobox(win, values=["+","-"], width=3)

solve = tk.Button(win, text="Solve")

boxe1 = tk.Entry(win, text="Answer here")
boxe2 = tk.Entry(win, text="Answer here1")
error = tk.Label(win, text="Errors will display here")

solve.bind("<Button-1>",math)

instruction.grid(row=1, column=1, columnspan=7)
abox.grid(row=3, column=1)
Abox.grid(row=3, column=2)
bbox.grid(row=3, column=4)
Bbox.grid(row=3, column=5)
cbox.grid(row=3, column=7)
plus1.grid(row=3, column=3)
plus2.grid(row=3, column=6)

error.grid(row=4, column=1, columnspan=7)


solve.grid(row=5, column=1, columnspan=2)
boxe1.grid(row=5, column=2, columnspan=4)
boxe2.grid(row=6, column=2, columnspan=4)

win.mainloop()
