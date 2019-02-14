""" простая двухмерная таблица, в корневом окне Tk по умолчанию """

from tkinter import *

rows = []

for i in range(5):
    cols = []
    for j in range(4):
        ent = Entry(relief=RIDGE)
        ent.grid(row=i, column=j, sticky=NSEW)
        ent.insert(END, '{}.{}'.format(i, j))
        cols.append(ent)
    rows.append(cols)


def onPress():
    for row in rows:
        for col in row:
            print(col.get(), end='')
        print()


Button(text='Fetch', command=onPress).grid()
mainloop()
