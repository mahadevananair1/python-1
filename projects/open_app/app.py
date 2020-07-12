#!/usr/bin/python

import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess

root = tk.Tk()
root.title("Run files in one click")
apps = []
filename = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray").pack()

def runApps():
    for app in apps:
        subprocess.call(["xdg-open", app])

canvas = tk.Canvas(root, height=800, width=800, bg="#263D42").pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp).pack()

runApps = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="#263D42", command=runApps).pack()

for app in apps:
    label = tk.Label(frame, text=app).pack()

root.mainloop()
