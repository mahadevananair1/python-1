from tkinter import Tk, Button, Entry


def clear():
    pass


def buttons():
    Button(screen, text="C", width="40", height="2", command=clear).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x400")
    screen.title("Calculator")
    Entry(screen, width="50", textvariable=answer).pack()
    buttons()

    screen.mainloop()


main_screen()
