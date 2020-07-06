from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("First windows")

def open():
    global my_img
    # Creating dual windows
    top = Toplevel()
    top.title("Second windows")
    my_img = ImageTk.PhotoImage(Image.open("images/love.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close", command=top.destroy()).pack()

# Button
btn = Button(root, text="Open Second windows", command=open).pack()


mainloop()