from tkinter import *
import math

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, NameError):
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def sqrt():
    global equation_text
    try:
        result = str(math.sqrt(float(equation_text)))
        equation_label.set(result)
        equation_text = result
    except ValueError:
        equation_label.set("Math Error")
        equation_text = ""

def percent():
    global equation_text
    try:
        result = str(float(equation_text) / 100)
        equation_label.set(result)
        equation_text = result
    except ValueError:
        equation_label.set("Math Error")
        equation_text = ""

def key_press(event):
    key = event.char
    if key in "0123456789+-*/().":
        button_press(key)
    elif key == "^":
        button_press("**")
    elif event.keysym == "Return":
        equal()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

window = Tk()
window.title("Calculator Program")
window.geometry("500x650")
window.configure(bg="grey")
window.bind("<Key>", key_press)

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=28, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('0', 3, 1),
    ('+', 0, 3), ('-', 1, 3), ('*', 2, 3), ('/', 3, 3),
    ('(', 3, 0), (')', 3, 2), ('.', 4, 3),
    ('=', 4, 2), ('C', 4, 1), ('⌫', 4, 0),
    ('√', 5, 0), ('^', 5, 1), ('%', 5, 2)
]

for (text, row, col) in buttons:
    action = lambda x=text: button_press(x) if x not in ('=', 'C', '\u232B', '√', '^', '%') else None
    cmd = {'=': equal, 'C': clear, '\u232B': backspace, '√': sqrt, '^': lambda: button_press('**'), '%': percent}
    button = Button(frame, text=text, font=35, width=9, height=4, command=cmd.get(text, action))
    button.grid(row=row, column=col)

window.mainloop()
