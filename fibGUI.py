#!/usr/bin/python
from tkinter import *


def get_input():
    num = input_box.get()
    text.delete(0.0, END)
    try:
        num = int(num)
        text.insert(0.0, str(fib(num)))
    except:
        text.insert(0.0, 'Please type a number.')


def fib(num):
    y = []
    x = num
    a = x
    b = a * 2
    if b == 0:
        b = 1
    for i in range(0, 10):
        temp = a
        a = b
        b = temp + b
        y.append(a)
    num = ', '.join(str(e) for e in y)
    return num

root = Tk()
root.title('Fibonacci Sequence')
root.geometry('525x100')
app = Frame(root)
app.grid()
# Input label - - - - - - - - - - - - - -
input_label = Label(app, text='Enter a number: ')
input_label.grid(row=0, column=0, pady=5)
# Input Box - - - - - - - - - - - - - - -
input_box = Entry(app, width=10)
input_box.grid(row=0, column=1, pady=5)
# Button - - - - - - - - - - - - - - - -
btn = Button(app, text="Go!")
btn['command'] = get_input
btn.grid(row=1, column=0, pady=5)
# Text box - - - - - - - - - - - - - - -
text = Text(app, width=50, height=2)
text.grid(row=1, column=1, pady=5)

root.mainloop()
