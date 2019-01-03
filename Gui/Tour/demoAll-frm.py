"""
4 класса демонстрационных компонентов (вложенных фреймов) в одном окне;
в одном окне присутствуют также 5 кнопок Quitter, причем щелчок на любой из
них приводит к завершению программы; графические интерфейсы могут повторно
использоваться, как фреймы в контейнере, независимые окна или процессы;
"""

from tkinter import *
from quitter import Quitter

demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)   # импортировать по имени в виде строки
        part = module.Demo(root)
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)


def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=" ")
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')


root = Tk()
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
