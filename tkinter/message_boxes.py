from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learning Tkinter')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You Click Yes!").pack()
    else:
        Label(root, text="You Click No!").pack()


Button(root, text="Popup", command=popup).pack()





mainloop()