from tkinter import *

root = Tk()

# Make a funtion
def button():
    label = Label(root, text="Nigger")
    label.pack()

# Create a button
button = Button(root, text='Login in', padx=20, command=button, fg="Green", bg="Pink")
button.pack()

root.mainloop()