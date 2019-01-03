
gifdir = '/home/vpalex999/programming/python/lutc_prog_1/gifs/'

import os
from tkinter import *


win = Tk()
img = PhotoImage(file=gifdir + 'zXX.gif')
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(100, 100, image=img, anchor=NW)
win.mainloop()
