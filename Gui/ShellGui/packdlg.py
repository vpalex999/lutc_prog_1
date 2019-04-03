""" выводит диалог ввода параметров для сценария packer и запускает его """

from glob import glob
from tkinter import *
from packer import pack
from formrows import makeFormRow


def packDialog():
    win = Toplevel()
    win.title('Enter Pack Parameters')
    var1 = makeFormRow(win, label='Output file')
    var2 = makeFormRow(win, label='Files to pack', extend=True)
    Button(win, text='OK', command=win.destroy).pack()
    win.grab_set()
    win.focus_set()
    win.wait_window()

    return var1.get(), var2.get()


def runPackDialog():
    output, patterns = packDialog()
    print("Pack:\n{}\n{}".format(output, patterns))
    pack('pack.txt', output)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=runPackDialog).pack(fill=X)
    root.mainloop()
