
gifdir = '/home/vpalex999/programming/python/lutc_prog_1/gifs/'

import os
from tkinter import *


print(os.getcwd())
win = Tk()
img = PhotoImage(file=gifdir + 'zXX.gif')
Button(win, image=img).pack()
win.mainloop()
