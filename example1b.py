#!python3
"""
Use the StrinVar.set() method to change the value of a variable to be used
in a Label widget!
"""

import tkinter as tk 


def run(e):
    data = e1Data.get()
    l1Data.set(data)
    e2Data.set(data)
    
win = tk.Tk()

# variables to be used in Tkinter widgets don't follow the standard syntax
# that we developed with basic Python programming
# We need to first create the variable and use new data types
l1Data = tk.StringVar()
e1Data = tk.StringVar()
e2Data = tk.StringVar()
# Note that we can also use an IntVar as an option, although this is
# primarily for widgets that need to return a numerical value like a
# scrollbar  or slider.  In most circumstances, it's probably best to
# use a StringVar() and convert it to a float or int as necessary
# see example2.py
e2IntData = tk.IntVar()

# To make the contents of a label or entry dynamic, we can use the
# option "textvariable" instead of "text".
# text creates a set text content, whereas textvariable will display
# the contents of a variable, and update the contents as soon as the
# variable contents changes.
e1 = tk.Entry(win,width=15,textvariable=e1Data)
l1 = tk.Label(win, width=15, textvariable=l1Data)
e2 = tk.Entry(win, width=15, textvariable = e2Data)
b1 = tk.Button(win,text="Click for do")
b1.bind("<Button-1>",run)


e1.pack()
l1.pack()
e2.pack()
b1.pack()
win.mainloop()