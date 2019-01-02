"""
использует переменные StringVar
компоновка по колонкам: вертикальные координаты виджетов могут не совпадать
(смотрите entry2)
"""

from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'


def fetch(Variables):
    for variable in Variables:
        print('Input => {}'.format(variable.get()))


def makeform(root, fields):
    form = Frame(root)
    left = Frame(form)
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()
