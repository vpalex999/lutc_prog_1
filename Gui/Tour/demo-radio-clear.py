"""
берегите переменные переключателей (о чем действительно легко можно забыть)
"""

from tkinter import *

root = Tk()


def radio1():
    #global tmp # сделав их глобальными, вы решите проблему
    tmp = IntVar()

    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)


radio1()
root.mainloop()
