from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.geometry("400x400")

def show():
    label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="You have Check the box", offvalue="You has Uncheck the box")
c.deselect()
c.pack()


button = Button(root, text="Show Selection", command=show).pack()




root.mainloop()
