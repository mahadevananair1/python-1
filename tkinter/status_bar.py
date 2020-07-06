from tkinter import *
# Modeules that insert image
from PIL import ImageTk,Image

root = Tk()
root.title('Learning Tkinter')

root.iconbitmap('images/icon.ico')

# Insert image
img1 = ImageTk.PhotoImage(Image.open("images/love.png"))
img2 = ImageTk.PhotoImage(Image.open("images/cartoon.png"))
img3 = ImageTk.PhotoImage(Image.open("images/family.png"))
img4 = ImageTk.PhotoImage(Image.open("images/logo1.png"))
img5 = ImageTk.PhotoImage(Image.open("images/crying.png"))

image_list = [img1, img2, img3, img4, img5]

# Status bar
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Image to display on the screen
label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

# Functions
def forward(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    # Display on the screen
    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Status bar
    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    return

def back(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Display on the screen
    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Status bar
    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    return

# Button
button_back = Button(root, text="<<", command=lambda: back(1))
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Put on the screen
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()
