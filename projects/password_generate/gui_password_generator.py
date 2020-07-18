from tkinter import *
import pyperclip
import random

# Set screen
root = Tk()
root.geometry("400x400")
root.title("Password Generator")

# Value
passstr = StringVar()
passlen = IntVar()


def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for i in range(passlen.get()):
        password += random.choice(pass1)
    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Draw
Label(root, text="PASSWORD GENERATOR", width="300", height="2", font=("Times", 20)).pack()

Label(root, text="Enter Password Length", width="100", height="1", font=("Helvetica", 16)).pack()
Entry(root, textvariable=passlen, width="30").pack()
Button(root, text="Generate Password", command=generate).pack()

Entry(root, textvariable=passstr, width="30").pack()
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()
root.mainloop()
