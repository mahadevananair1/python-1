from tkinter import  *

# Set screen
root = Tk()
root.geometry("400x400")
root.title("Password Generator")

draw_title = Label(root, text="PASSWORD GENERATOR", width="300", height="3", font=("Times", 20)).pack() 
draw_password = Label(root, text="Password", font=("Helvetica", 16)).pack()
button = Button(root, text="Generate").pack()

root.mainloop()
