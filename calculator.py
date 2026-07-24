"""

        Simple Calculator using Tkinter


Project : Calculator GUI
Language: Python 2.7
Library : Tkinter

Description:

This is a simple calculator application built using the
Tkinter library in Python 2.7. It allows users to perform
basic arithmetic operations through a graphical interface.

Features:

 Addition (+)
 Subtraction (-)
 Multiplication (*)
 Division (/)
 Percentage (%)
 Decimal Numbers
 Delete Last Character
Clear Screen
 Error Handling

Author : Aprupinath Singh
Date   : 2026

"""

from Tkinter import *

# Function to insert button values
# into the calculator display

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))


# Clear the display

def clear():
    entry.delete(0, END)


# Delete the last entered character

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


# Evaluate the mathematical expression

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


# Create Main Window
root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)


# Calculator Display

entry = Entry(root,
              font=("Arial", 20),
              justify=RIGHT,
              bd=10)

entry.pack(fill=X, padx=10, pady=10, ipady=10)


# Frame for Calculator Buttons

frame = Frame(root)
frame.pack(expand=True, fill=BOTH)

# Button Layout
buttons = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]


# Create Buttons Dynamically

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


# Start the Application

root.mainloop()