from tkinter import *

import tkinter

top = Tk()

mb = Menubutton(top, text="condiments", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

abmeldenVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label="abmelden",
                        variable=abmeldenVar)
mb.menu.add_checkbutton(label="ketchup",
                        variable=ketchVar)

mb.pack()
top.mainloop()