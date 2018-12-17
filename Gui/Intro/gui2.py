import sys
from tkinter import *


widget = Button(None, text='Hello widget world', command=sys.exit)
widget.config(text='Hello GUI world!')
widget.pack()
widget.mainloop()
