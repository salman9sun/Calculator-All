from tkinter import *  # Functionality

# Functionality
def button_press(num):
    global equation_text
    num_str = str(num)
    if equation_text and equation_text[-1] in "+-×÷" and num_str in "+-×÷":
        return
    equation_text = equation_text + num_str
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        equation_text = equation_text.replace('÷', '/').replace('×', '*')
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, NameError):
        equation_label.set("Error")
        equation_text = " "
    except (ZeroDivisionError):
        equation_label.set("Can't divide by zero!")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set(" ")
    equation_text = " "

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def square(): button_press('**2')
def cube(): button_press('**3')
def percentage():
    global equation_text
    try:
        value = eval(equation_text)
        result = str(value / 100)
        equation_label.set(result)
        equation_text = result
    except:
        equation_label.set("Error!")
        equation_text = ""

def key_press(event):
    key = event.char
    if key in "0123456789+-*/().÷×":
        button_press(key)
    elif key == '%':
        percentage()
    elif event.keysym == "Return":
        equal()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

# UI Setup
window = Tk()
window.title("Calculator")
window.configure(bg="#F5F5F5")
window.geometry("450x750")
window.resizable(False, False)
window.bind("<Key>", key_press)

equation_text = ""
equation_label = StringVar()

# Display label for the equation
label = Label(window, textvariable=equation_label, font=('Segoe UI', 30, 'bold'),
              bg="white", fg="black", width=20, height=2)
label.pack(pady=20, padx=15)

# Create a frame to hold the buttons
frame = Frame(window, bg="#F5F5F5")
frame.pack()

# Adjusted button size for larger buttons
button_params = {'font': ('Segoe UI', 22, 'bold'), 'width': 5, 'height': 2, 'bd': 0, 'bg': 'white', 'fg': 'black'}
button_params1 = {'font': ('Segoe UI', 22, 'bold'), 'width': 5, 'height': 2, 'bd': 0, 'bg': 'white', 'fg': '#FF4500'}  # Custom orange color

# Buttons for special operations
btnsquare = Button(frame, text="x²", **button_params1, command=square)
btnsquare.grid(row=0, column=0, padx=5, pady=5)

btncube = Button(frame, text="x³", **button_params1, command=cube)
btncube.grid(row=0, column=1, padx=5, pady=5)

btnpercentage = Button(frame, text="%", **button_params1, command=percentage)
btnpercentage.grid(row=0, column=2, padx=5, pady=5)

btnclear = Button(frame, text="C", **button_params1, command=clear)
btnclear.grid(row=0, column=3, padx=5, pady=5)

# Brackets and Backspace
btnbracket1 = Button(frame, text="(", **button_params1, command=lambda: button_press("("))
btnbracket1.grid(row=1, column=0, padx=5, pady=5)

btnbracket2 = Button(frame, text=")", **button_params1, command=lambda: button_press(")"))
btnbracket2.grid(row=1, column=1, padx=5, pady=5)

btnbackspace = Button(frame, text="⌫", **button_params1, command=backspace)
btnbackspace.grid(row=1, column=2, padx=5, pady=5)

# Apply orange color to operators (+, -, ×, ÷)
btndivition = Button(frame, text="÷", **button_params1, command=lambda: button_press("÷"))
btndivition.grid(row=1, column=3, padx=5, pady=5)

btnmultiplication = Button(frame, text="×", **button_params1, command=lambda: button_press("×"))
btnmultiplication.grid(row=2, column=3, padx=5, pady=5)

btnminus = Button(frame, text="-", **button_params1, command=lambda: button_press("-"))
btnminus.grid(row=3, column=3, padx=5, pady=5)

btnplus = Button(frame, text="+", **button_params1, command=lambda: button_press("+"))
btnplus.grid(row=4, column=3, padx=5, pady=5)

# Number Buttons
btn7 = Button(frame, text=7, **button_params, command=lambda: button_press(7))
btn7.grid(row=2, column=0, padx=5, pady=5)

btn8 = Button(frame, text=8, **button_params, command=lambda: button_press(8))
btn8.grid(row=2, column=1, padx=5, pady=5)

btn9 = Button(frame, text=9, **button_params, command=lambda: button_press(9))
btn9.grid(row=2, column=2, padx=5, pady=5)

btn4 = Button(frame, text=4, **button_params, command=lambda: button_press(4))
btn4.grid(row=3, column=0, padx=5, pady=5)

btn5 = Button(frame, text=5, **button_params, command=lambda: button_press(5))
btn5.grid(row=3, column=1, padx=5, pady=5)

btn6 = Button(frame, text=6, **button_params, command=lambda: button_press(6))
btn6.grid(row=3, column=2, padx=5, pady=5)

btn1 = Button(frame, text=1, **button_params, command=lambda: button_press(1))
btn1.grid(row=4, column=0, padx=5, pady=5)

btn2 = Button(frame, text=2, **button_params, command=lambda: button_press(2))
btn2.grid(row=4, column=1, padx=5, pady=5)

btn3 = Button(frame, text=3, **button_params, command=lambda: button_press(3))
btn3.grid(row=4, column=2, padx=5, pady=5)

btn00 = Button(frame, text="00", **button_params, command=lambda: button_press("00"))
btn00.grid(row=5, column=0, padx=5, pady=5)

btn0 = Button(frame, text=0, **button_params, command=lambda: button_press(0))
btn0.grid(row=5, column=1, padx=5, pady=5)

btndecimal = Button(frame, text=".", **button_params, command=lambda: button_press("."))
btndecimal.grid(row=5, column=2, padx=5, pady=5)

btnequal = Button(frame, text="=", font=('Segoe UI', 22, 'bold'), width=5, height=2, bd=0,
                  bg="orange", fg="white", padx=5, pady=5, command=equal)
btnequal.grid(row=5, column=3, padx=5, pady=5)

# Adjust row and column configuration
for i in range(6):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

# Run the main loop
window.mainloop()
