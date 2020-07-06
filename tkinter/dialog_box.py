from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
 
root = Tk()
root.title('Learning Tkinter')
 
def open():
    global images
    root.filename = filedialog.askopenfilename(initialdir="/Tkinter/images", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    label = Label(root, text=root.filename).pack()
    images = ImageTk.PhotoImage(Image.open(root.filename))
    images_label = Label(image=images).pack()
 
btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
