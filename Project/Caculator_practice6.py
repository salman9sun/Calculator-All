from tkinter import *

def button_press(num):
    global equation
    if num in "+-×÷" and (not equation or equation[-1] in "+-×÷"):
        return
    equation += num
    display.set(equation)

def calculate():
    global equation
    try:
        result = eval(equation.replace('÷', '/').replace('×', '*').replace('^', '**'))
        result = str(int(result)) if result == int(result) else str(result)
        history_box.insert(END, f"{equation} = {result}")
        equation = result
        display.set(result)
    except ZeroDivisionError:
        display.set("Can't divide by zero")
        equation = ""
    except:
        display.set("Error")
        equation = ""

def clear():
    global equation
    equation = ""
    display.set("")

def backspace():
    global equation
    equation = equation[:-1]
    display.set(equation)

def square_root():
    global equation
    equation = f"({equation})**0.5"
    calculate()
def percentage():
    global equation
    try:
        if not equation or equation[-1] == '%':
            return

        for op in reversed('+-×÷'):
            if op in equation:
                left, right = equation.rsplit(op, 1)
                if right:
                    base = eval(left.replace('×', '*').replace('÷', '/'))
                    percent = float(right) / 100
                    if op == '+':
                        result = base + (base * percent)
                    elif op == '-':
                        result = base - (base * percent)
                    elif op == '×':
                        result = base * percent
                    elif op == '÷':
                        if percent == 0:
                            display.set("Can't divide by zero")
                            equation = ""
                            return
                        result = base / percent
                    result = int(result) if result == int(result) else result
                    display.set(str(result))
                    equation = str(result)
                    return

        result = float(equation) / 100
        result = int(result) if result == int(result) else result
        display.set(str(result))
        equation = str(result)
    except:
        display.set("Error")
        equation = ""

def toggle_history():
    global history_visible
    history_visible = not history_visible
    if history_visible:
        history_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)
    else:
        history_frame.pack_forget()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    bg = "#121212" if dark_mode else "#ffffff"
    fg = "white" if dark_mode else "black"
    entry_bg = "#1E1E1E" if dark_mode else "white"
    list_bg = "#1A1A1A" if dark_mode else "#f0f0f0"
    list_fg = "white" if dark_mode else "black"

    window.configure(bg=bg)
    label.config(bg=entry_bg, fg=fg)
    frame.config(bg=bg)
    history_frame.config(bg=bg)
    top_row.config(bg=bg)
    history_box.config(bg=list_bg, fg=list_fg)
    theme_btn.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg, text="\ud83c\udf19 Dark" if not dark_mode else "\u2600\ufe0f Light")

    for b in frame.winfo_children():
        text = b.cget("text")
        if text == '=':
            b.config(bg='white', fg='black')
        elif text in "+-×÷":
            b.config(bg='black', fg='white')
        elif text in ['C', '⌫']:
            b.config(bg='red', fg='white')
        else:
            b.config(bg="#333" if dark_mode else "#ddd", fg=fg)

def key_press(event):
    key = event.char
    keysym = event.keysym

    if key in '0123456789.+-*/()':
        button_press(key.replace('*', '×').replace('/', '÷'))
    elif key == '\r':
        calculate()
    elif keysym == 'BackSpace':
        backspace()
    elif keysym == 'Escape':
        clear()
    elif key == '^':
        button_press('^')
    elif key == '%':
        percentage()
    elif key.lower() == 'r':
        square_root()
    elif keysym.lower() == 't':
        toggle_theme()

window = Tk()
window.title("Calculator")
window.geometry("400x750")
window.minsize(400, 750)
window.resizable(True, True)

equation = ""
display = StringVar()
dark_mode = True
history_visible = False

label = Label(window, textvariable=display, font=('Segoe UI', 24, 'bold'), height=2, bd=0, anchor='e', justify='right')
label.pack(fill=X, padx=10, pady=(10, 0))

top_row = Frame(window)
top_row.pack(fill=X)

history_toggle_btn = Button(top_row, text="History", command=toggle_history, font=('Segoe UI', 12, 'bold'), relief="flat")
history_toggle_btn.pack(side=LEFT, padx=10)

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

btn_style = {'font': ('Segoe UI', 16, 'bold'), 'height': 2, 'bd': 0, 'relief': 'flat', 'width': 5}
buttons = [
    ('√', square_root), ('^', lambda: button_press('^')), ('C', clear), ('⌫', backspace),
    ('(', lambda: button_press('(')), (')', lambda: button_press(')')), ('%', percentage), ('÷', lambda: button_press('÷')),
    ('7', lambda: button_press('7')), ('8', lambda: button_press('8')), ('9', lambda: button_press('9')), ('×', lambda: button_press('×')),
    ('4', lambda: button_press('4')), ('5', lambda: button_press('5')), ('6', lambda: button_press('6')), ('-', lambda: button_press('-')),
    ('1', lambda: button_press('1')), ('2', lambda: button_press('2')), ('3', lambda: button_press('3')), ('+', lambda: button_press('+')),
    ('00', lambda: button_press('00')), ('0', lambda: button_press('0')), ('.', lambda: button_press('.')), ('=', calculate),
]

for i, (txt, cmd) in enumerate(buttons):
    Button(frame, text=txt, command=cmd, **btn_style).grid(row=i//4, column=i%4, padx=3, pady=3, sticky=NSEW)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1, uniform="equal")
for i in range(5):
    frame.grid_rowconfigure(i, weight=1, uniform="equal")

history_frame = Frame(window)
history_frame.pack_forget()
history_box = Listbox(history_frame, height=6, font=('Consolas', 12, 'bold'), bd=0)
history_box.pack(fill=BOTH, expand=True)

theme_btn = Button(window, text="\u2600\ufe0f Light", command=toggle_theme, font=('Segoe UI', 11, 'bold'), relief="flat")
theme_btn.pack(side=RIGHT, padx=10)

apply_theme()
window.bind("<Key>", key_press)
window.mainloop()
