"""
##############################################################################
инструмент запуска; использует шаблоны GuiMaker, стандартный диалог завершения
GuiMixin; это просто биб­лиотека классов: чтобы вывести графический интерфейс,
запустите сценарий mytools;
##############################################################################
"""
import sys
import os
print(os.getcwd())
sys.path.append("../../")
print(sys.path)
from tkinter import *
from Gui.Tools.guimixin import GuiMixin
from Gui.Tools.guimaker import *


class ShellGui(GuiMixin, GuiMakerWindowMenu): #
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")

    def handleList(self, event):
        label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def makeWidgets(self):
        sbar = Scrollbar(self)
        list = Listbox(self, bg="white")
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH) # список обрез-ся первым
        for (label, action) in self.fetchCommands(): # добавляется в список,
            list.insert(END, label)
        list.bind("<Double-1>", self.handleList)
        self.listbox = list

    def forToolBar(self, label):
        return True

    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))
        self.toolBar.append(("Quit", self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
                        ("File", 0, [("Quit", -1, self.quit)]),     # имя раскрывающегося меню
                        ("Tools", 0, toolEntries)                   # список элементов меню
                    ]                                               # метка,клавиша,обработчик
        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1, action))     # добавить приложения
                                                        # в меню

##############################################################################
# делегирование операций шаблонным подклассам с разным способом хранения
# перечня утилит, которые в свою очередь делегируют операции
# подклассам, реализующим запуск утилит
##############################################################################


class ListMenuGui(ShellGui):
    def fetchCommands(self):    # myMenu устанавливается в подклассе
        return self.myMenu      # список кортежей (метка, обработчик)

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd:
                action()


class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()

    def runCommand(self, cmd):
        self.myMenu[cmd]()