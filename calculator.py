# -*- coding: utf-8 -*-

from Tkinter import *

# ---------------- Functions ---------------- #

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# ---------------- Window ---------------- #

root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# ---------------- Display ---------------- #

entry = Entry(root,
              font=("Arial", 20),
              justify=RIGHT,
              bd=10)

entry.pack(fill=X, padx=10, pady=10, ipady=10)

# ---------------- Buttons ---------------- #

frame = Frame(root)
frame.pack(expand=True, fill=BOTH)

buttons = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

for row in buttons:

    row_frame = Frame(frame)
    row_frame.pack(expand=True, fill=BOTH)

    for btn in row:

        if btn == 'C':
            command = clear
        elif btn == 'DEL':
            command = backspace
        elif btn == '=':
            command = calculate
        else:
            command = lambda x=btn: click(x)

        b = Button(row_frame,
                   text=btn,
                   font=("Arial", 16, "bold"),
                   command=command,
                   width=6,
                   height=2)

        b.pack(side=LEFT, expand=True, fill=BOTH, padx=2, pady=2)

root.mainloop()