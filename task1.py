"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
from tkinter.constants import CENTER 

def run(E):
    print(E)
    data1 = name.get()
    data2 = GR.get()
    data3 = SN.get()

    data = f"{data1}/{data2}/{data3}"

    total.config(text=data)
    total.delete(0,tk.END)
    total.insert(0,data)
    


win = tk.Tk()
win.geometry("340x200")
name = tk.Entry(win,width=15)
GR = tk.Entry(win, width=15)
SN = tk.Entry(win,width=15)

N = tk.Label(win, text = "Name")
g = tk.Label(win, text = "Grade")
s = tk.Label(win, text = "Student Number")
T = tk.Label(win, text = "System (N/GR/SN)")

total = tk.Entry(win, width=25, text="Original Text")
b1 = tk.Button(win, text="Load student")

b1.bind("<Button-1>",run)

N.place(x=30, y=40, anchor= CENTER )
g.place(x=130, y=40, anchor= CENTER)
s.place(x=255, y=40, anchor= CENTER)
T.place(x=10, y=130)

name.place(x=60, y=60, anchor= CENTER)
GR.place(x=160, y=60, anchor= CENTER)
SN.place(x=260, y=60, anchor= CENTER)
total.place(x=10, y=150)

b1.place(x=50, y=100, anchor= CENTER)

win.mainloop()