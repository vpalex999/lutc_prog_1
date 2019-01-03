
gifdir = '/home/vpalex999/programming/python/lutc_prog_1/gifs/'

from tkinter import *
from glob import glob
import demoCheck
import random


class ButtonPicsDemo(Frame):
    def __init__(self, gifdir=gifdir, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self, text='none', bg='blue', fg='red')
        self.pix = Button(self, text='Press me', command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(gifdir + '*')
        self.images = [(x, PhotoImage(file=x)) for x in files]
        print(files)
        
    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)


if __name__ == '__main__': ButtonPicsDemo().mainloop()
