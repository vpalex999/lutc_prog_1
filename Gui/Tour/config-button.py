from tkinter import *


root = Tk()

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='hand2')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='blue')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()
