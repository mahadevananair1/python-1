from tkinter import Tk, Button, Entry, StringVar

show = ""


def press(num):
    global show
    show += str(num)
    display.set(show)


def clear_display():
    global show
    show = ""
    display.set(show)


if __name__ == "__main__":
    screen = Tk()
    screen.geometry("500x400")
    screen.title("Calculator")

    display = StringVar()

    display_field = Entry(screen, textvariable=show, width="30")
    display_field.grid(row=0, column=1)

    clear = Button(screen, text="Clear", width="40", command=clear_display())
    clear.grid(row=1, column=1)

    button1 = Button(screen, text="1", width="4", height="2", command=lambda: press(1))
    button1.grid(row=2, column=0)

    button2 = Button(screen, text="2", width="4", height="2", command=lambda: press(2))
    button2.grid(row=2, column=1)

    button3 = Button(screen, text="3", width="4", height="2", command=lambda: press(3))
    button3.grid(row=2, column=2)

    button4 = Button(screen, text="4", width="4", height="2", command=lambda: press(4))
    button4.grid(row=3, column=0)

    button5 = Button(screen, text="5", width="4", height="2", command=lambda: press(5))
    button5.grid(row=3, column=1)

    button6 = Button(screen, text="6", width="4", height="2", command=lambda: press(6))
    button6.grid(row=3, column=2)

    button7 = Button(screen, text="7", width="4", height="2", command=lambda: press(7))
    button7.grid(row=4, column=0)

    button8 = Button(screen, text="8", width="4", height="2", command=lambda: press(8))
    button8.grid(row=4, column=1)

    button9 = Button(screen, text="9", width="4", height="2", command=lambda: press(9))
    button9.grid(row=4, column=2)

    button0 = Button(screen, text="0", width="4", height="2", command=lambda: press(0))
    button0.grid(row=5, column=1)

    plus = Button(screen, text="+", width="4", height="2", command=lambda: press("+"))
    plus.grid(row=6, column=0)

    minus = Button(screen, text="-", width="4", height="2", command=lambda: press("-"))
    minus.grid(row=6, column=1)

    multiply = Button(screen, text="*", width="4", height="2", command=lambda: press("*"))
    multiply.grid(row=6, column=2)

    divide = Button(screen, text="/", width="4", height="2", command=lambda: press("/"))
    divide.grid(row=7, column=0)

    equal = Button(screen, text="=", width="4", height="2", command=lambda: press("="))
    equal.grid(row=5, column=2)

    screen.mainloop()
