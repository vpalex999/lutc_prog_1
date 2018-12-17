from user_preferense import bcolor, bfont, bsize
from tkinter import *


class ThemedButton(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.pack()
        self.config(bg='black', font=(bfont, bsize))


def onSpam():
    print('Hello onSpam!')


def onEggs():
    print('Hello onEggs!')

ThemedButton(text='spam', command=onSpam)
ThemedButton(text='eggs', command=onEggs)


class MyButton(ThemedButton):
    def __init__(self, parent=None, **configs):
        ThemedButton.__init__(self, parent, **configs)
        self.config(text='subclass')

MyButton(command=onSpam)

mainloop()

