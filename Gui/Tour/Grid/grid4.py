""" простая двухмерная таблица, в корневом окне Tk по умолчанию """

from tkinter import *


for i in range(5):
    for j in range(4):
        lab = Label(text='{}.{}'.format(i, j), relief=RIDGE)
        lab.grid(row=i, column=j, sticky=NSEW)


mainloop()
