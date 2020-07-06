from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("images/icon.ico")

frame = LabelFrame(root, text="This is Frame", padx=5, pady=5)
frame.pack(padx=100, pady=100)

b1 = Button(frame, text="Don't Click Here!", command=root.quit)
b2 = Button(frame, text="Or Click Here!", command=root.quit)
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
root.mainloop()
