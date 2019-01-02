import sys
from tkinter import *

makemodal = (len(sys.argv) > 1)


def dialog():
    win = Toplevel()
    Label(win, text='Hard drive reformatted!').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:
        win.focus_set()     # принять фокус ввода
        win.grab_set()      # запретить доступ до окна, пока открыт диалог
        win.wait_window()   # ждать, пока win не будет уничтожен
    print('dialog exit')


root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()
