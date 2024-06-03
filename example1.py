#!python3
"""
Use the StrinVar.set() method to change the value of a variable to be used
in a Label widget!
"""

import tkinter as tk 

def run(e):
    #callback function that will be called when button b1 is clicked
    #the event data is stored in the variable e.  It is the only input
    #that a callback function accepts
    print("This does not show up on your gui")
    print(f"The details of the event are {e}")
    data = e1.get()
    l1.config(text=data)
    e2.delete(0,tk.END)
    e2.insert(0,data)


#Create the window and add 3 widgets.
win = tk.Tk()
e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Click to change the text")
e2 = tk.Entry(win,width=15)
l1 = tk.Label(win, width=15, text="Original Text")

#Windows are event driven.  We can bind an event listener to any object in the GUI
#The different kinds of events are dependent on what kind of object we have, and then
#we specify a callback function to execute.  A callback function includes data about the
#event that triggered it
b1.bind("<Button-1>",run)


e1.pack()
l1.pack()
b1.pack()
e2.pack()
win.mainloop()