#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

def multiply(event):
    N = e[0].get()
    NN = e[1].get()

    try:
        N = float(N)
        NN = float(NN)
        X = N*NN
        e[2].delete(0,tk.END)
        e[2].insert(0,X)
        text.config(text="No Errors")
    except:
        text.config(text = "Oh no! That entry did not work, try again...")



def addition(event):
    N = e[0].get()
    NN = e[1].get()

    try:
        N = float(N)
        NN = float(NN)
        X = N+NN
        e[2].delete(0,tk.END)
        e[2].insert(0,X)
        text.config(text="No Errors")
    except:
        text.config(text = "Oh no! That entry did not work, try again...")

def minus(event):
    N = e[0].get()
    NN = e[1].get()

    try:
        N = float(N)
        NN = float(NN)
        X = N-NN
        e[2].delete(0,tk.END)
        e[2].insert(0,X)
        text.config(text="No Errors")
    except:
        text.config(text = "Oh no! That entry did not work, try again...")


def divide(event):
    N = e[0].get()
    NN = e[1].get()

    try:
        N = float(N)
        NN = float(NN)
        X = N/NN
        e[2].delete(0,tk.END)
        e[2].insert(0,X)
        text.config(text="No Errors")
    except:
        text.config(text = "Oh no! That entry did not work, try again...")


w = tk.Tk()
w.attributes("-topmost",True)

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer"))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))

text = tk.Label(w, text="Errors diplayed here:")

b[0].bind("<Button-1>",multiply)
b[1].bind("<Button-1>",addition)
b[2].bind("<Button-1>",minus)
b[3].bind("<Button-1>",divide)

l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e[0].grid(row=3,column=1, columnspan=2)
e[1].grid(row=3,column=3, columnspan=2)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)

text.grid(row=6, column=1, columnspan=4)

w.mainloop()