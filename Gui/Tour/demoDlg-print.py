"""
то же, что и предыдущий пример, но выводит значения, возвращаемые диалогами;
lambda-выражение сохраняет данные из локальной области видимости для передачи их
обработчику (обработчик события нажатия кнопки обычно не получает аргументов,
а автоматические ссылки в объемлющую область видимости некорректно работают
с переменными цикла) и действует подобно вложенной инструкции def, такой как:
def func(key=key): self.printit(key)
"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text='Basic demos').pack()
        for key in demos:
            funct = (lambda key=key: self.printit(key))
            Button(self, text=key, command=funct).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns =>', demos[name]())


if __name__ == '__main__': Demo().mainloop()