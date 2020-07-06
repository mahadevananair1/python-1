from tkinter import *

root = Tk()

# Creating typing box
e = Entry(root, width=50, fg="blue", bg='pink', borderwidth=10)
e.pack()
e.insert(0, "Enter your name")

# Make a funtion
def button():
    hello = "Hello " + e.get()
    label = Label(root, text=hello)
    label.pack()

# Create a button
button = Button(root, text='Enter your name', padx=20, command=button, fg="Green", bg="Pink")
button.pack()

root.mainloop()
