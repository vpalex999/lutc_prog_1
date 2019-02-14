"""
##############################################################################
класс, “подмешиваемый” во фреймы: реализует общие методы вызова стандартных
диалогов, запуска программ, простых инструментов отображения текста и так далее;
метод quit требует, чтобы этот класс подмешивался к классу Frame (или его
производным)
##############################################################################
"""

import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from launchmodes import PortableLauncher, System


class GuiMixin:
    def infobox(self, title, text, *args):  # диалоги
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error!', text)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        showerror('Not implemented', 'Option not available')

    def quit(self):
        ans = self.question('Verify quit', 'Are you sure want to quit?')
        if ans:
            Frame.quit(self)  # нерекурсивный вызов quit!

    def help(self):
        self.infobox('RTFM', 'See figure 1...')

    def selectOpenFile(self, file='', dir='.'):
        return askopenfilename(initialdir=dir, initialfile=file)

    def selectSaveFile(self, file="", dir="."):
        return asksaveasfilename(initialfile=file, initialdir=dir)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)

    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)
    

if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)
            Button(self, text='notDone', command=self.notdone).pack(fill=X)

        def other(self):
            self.spawn('guimixin.py')

    TestMixin().mainloop()
