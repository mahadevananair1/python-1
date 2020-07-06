from tkinter import *

root = Tk()

# Creating label (Creating things)
label1 = Label(root, text="Hello World!")
label2 = Label(root, text="My name is Jan Poonthong")


# Making grid row and column (Putting on the screen)
label1.grid(row=0, column=0)
label2.grid(row=1, column=5)

root.mainloop()