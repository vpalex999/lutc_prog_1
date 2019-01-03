
gifdir = '/home/vpalex999/programming/python/lutc_prog_1/gifs/'

import os
from sys import argv
from tkinter import *

filename = argv[1] if len(argv) > 1 else 'zXX.gif'


win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
