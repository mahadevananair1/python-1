from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Tkinter')

#r = IntVar()
#r.set("2")

Modes = [
    ("Jan", "Jan"),
    ("Devon", "Devon"),
    ("Strager", "Strager"),
    ("Python", "Python")
]

names = StringVar()

for text, mode in Modes:
    Radiobutton(root, text=text, variable=names, value=mode).pack(anchor=W)

def click(value):
    label = Label(root, text=value)
    label.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: click(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: click(r.get())).pack()

lable = Label(root, text=names.get()).pack()

button = Button(root, text="Click Me!", command=lambda: click(names.get())).pack(anchor=W)

root.mainloop()