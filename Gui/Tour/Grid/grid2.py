from tkinter import *

colors = ['red', 'green', 'white', 'yellow', 'blue']


def gridbox(parent):
    """ компоновка по номерам рядов/колонок в сетке """

    row = 0

    for c in colors:
        lab = Label(parent, text=c, relief=RIDGE, width=25)
        ent = Entry(parent, bg=c, relief=SUNKEN, width=50)
        lab.grid(row=row, column=0)
        ent.grid(row=row, column=1)
        ent.insert(0, 'grid')
        row += 1


def packbox(parent):
    """ фреймы-ряды и метки фиксированной длины """
    for c in colors:
        row = Frame(parent)
        lab = Label(row, text=c, relief=RIDGE, width=25)
        ent = Entry(row, bg=c, relief=SUNKEN, width=50)
        row.pack(side=TOP)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        ent.insert(0, 'pack')


if __name__ == '__main__':
    root = Tk()
    gridbox(Toplevel())
    packbox(Toplevel())
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()
