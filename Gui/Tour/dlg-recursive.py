import sys
from tkinter import *


def dialog():
    win = Toplevel()
    Label(win, text='Hard drive reformatted!').pack()
    Button(win, text='OK', command=win.quit).pack()
    win.protocol('WM_DELETE_WINDOW', win.quit)
    
    win.focus_set()     # принять фокус ввода
    win.grab_set()      # запретить доступ до окна, пока открыт диалог
    win.mainloop()
    win.destroy()
    print('dialog exit')


root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()
