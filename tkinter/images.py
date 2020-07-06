from tkinter import *
# Modeules that insert image
from PIL import ImageTk,Image

root = Tk()
root.title('Learning Tkinter')

root.iconbitmap('images/icon.ico')

# Insert image
img = ImageTk.PhotoImage(Image.open("images/love.png"))
label = Label(image=img)
label.pack()

# Exit button
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()


root.mainloop()