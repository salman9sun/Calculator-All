import customtkinter as ctk
from tkinter import StringVar

# --- App Config ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x750")
        self.minsize(400, 750)

        self.expression = ""
        self.is_dark_mode = True
        self.history_shown = False

        self.display = StringVar()
        self.create_widgets()
        self.bind("<Key>", self.handle_keypress)

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, textvariable=self.display, font=('Segoe UI', 28), height=80, anchor='e')
        self.label.pack(fill='x', padx=10, pady=(10, 0))

        self.top_row = ctk.CTkFrame(self, fg_color="transparent")
        self.top_row.pack(fill='x', pady=(5, 5))

        self.btn_style = {'font': ('Segoe UI', 18), 'height': 40, 'corner_radius': 10, 'width': 80}

        self.history_btn = ctk.CTkButton(self.top_row, text="History", command=self.toggle_history_view, **self.btn_style)
        self.history_btn.pack(side='left', padx=(10, 5))

        self.clear_history_btn = ctk.CTkButton(self.top_row, text="Clear", command=self.clear_history, **self.btn_style)
        self.clear_history_btn.pack_forget()

        self.theme_btn = ctk.CTkButton(self.top_row, text="☀️ Light", command=self.flip_theme, **self.btn_style)
        self.theme_btn.pack(side='right', padx=(5, 10))

        self.history_frame = ctk.CTkFrame(self)
        self.history_box = ctk.CTkTextbox(self.history_frame, height=100, font=('Consolas', 13))
        self.history_box.pack(fill='both', expand=True)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True)

        self.build_buttons()

    def build_buttons(self):
        self.frame.destroy()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True)

        def get_color_settings(text):
            white = "#ffffff"
            black = "#000000"
            red = "#d00000"
            dark_bg = "#2c2c2c"
            hover = "#dcdcdc" if not self.is_dark_mode else "#3a3a3a"

            if text in ('C', '⌫'):
                return {'fg_color': red, 'text_color': white, 'hover_color': hover}
            elif text in ('+', '-', '×', '÷'):
                return {'fg_color': black, 'text_color': white, 'hover_color': hover}
            else:
                return {
                    'fg_color': white if not self.is_dark_mode else dark_bg,
                    'text_color': black if not self.is_dark_mode else white,
                    'hover_color': hover
                }

        buttons = [
            ('√', self.do_square_root), ('^', lambda: self.press_key('^')), ('C', self.clear_all), ('⌫', self.delete_last),
            ('(', lambda: self.press_key('(')), (')', lambda: self.press_key(')')), ('%', self.do_percentage), ('÷', lambda: self.press_key('÷')),
            ('7', lambda: self.press_key('7')), ('8', lambda: self.press_key('8')), ('9', lambda: self.press_key('9')), ('×', lambda: self.press_key('×')),
            ('4', lambda: self.press_key('4')), ('5', lambda: self.press_key('5')), ('6', lambda: self.press_key('6')), ('-', lambda: self.press_key('-')),
            ('1', lambda: self.press_key('1')), ('2', lambda: self.press_key('2')), ('3', lambda: self.press_key('3')), ('+', lambda: self.press_key('+')),
            ('00', lambda: self.press_key('00')), ('0', lambda: self.press_key('0')), ('.', lambda: self.press_key('.')), ('=', self.evaluate),
        ]

        for idx, (txt, cmd) in enumerate(buttons):
            colors = get_color_settings(txt)
            btn = ctk.CTkButton(self.frame, text=txt, command=cmd, **self.btn_style, **colors)
            btn.grid(row=idx // 4, column=idx % 4, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame.grid_rowconfigure(i, weight=1)

        for btn in [self.history_btn, self.clear_history_btn, self.theme_btn]:
            colors = get_color_settings(btn.cget("text"))
            btn.configure(**colors)

    def press_key(self, val):
        if val in "+×÷" and (not self.expression or self.expression[-1] in "+-×÷"):
            return
        if val == '-' and self.expression and self.expression[-1] in "+-×÷":
            return
        self.expression += val
        self.display.set(self.expression)

    def evaluate(self):
        try:
            result = eval(self.expression.replace('÷', '/').replace('×', '*').replace('^', '**'))
            result = int(result) if result == int(result) else result
            self.history_box.insert("end", f"{self.expression} = {result}\n")
            self.expression = str(result)
            self.display.set(self.expression)
        except ZeroDivisionError:
            self.display.set("Can't divide by zero")
            self.expression = ""
        except:
            self.display.set("Error")
            self.expression = ""

    def clear_all(self):
        self.expression = ""
        self.display.set("")

    def delete_last(self):
        self.expression = self.expression[:-1]
        self.display.set(self.expression)

    def do_square_root(self):
        try:
            if not self.expression:
                return
            val = eval(self.expression.replace('÷', '/').replace('×', '*').replace('^', '**'))
            if val < 0:
                self.display.set("Invalid Input")
                self.expression = ""
                return
            sqrt_val = val ** 0.5
            result = int(sqrt_val) if sqrt_val == int(sqrt_val) else sqrt_val
            self.expression = str(result)
            self.display.set(self.expression)
            self.history_box.insert("end", f"√({val}) = {result}\n")
        except:
            self.display.set("Error")
            self.expression = ""

    def do_percentage(self):
        try:
            if not self.expression:
                return
            original = self.expression + '%'
            for op in "+-×÷":
                if op in self.expression:
                    parts = self.expression.split(op)
                    if len(parts) == 2:
                        left, right = map(float, parts)
                        right = left * right / 100
                        res = {
                            '+': left + right,
                            '-': left - right,
                            '×': left * right,
                            '÷': left / right if right != 0 else float('inf')
                        }.get(op)
                        break
            else:
                res = float(self.expression) / 100

            final = int(res) if res == int(res) else res
            self.expression = str(final)
            self.display.set(self.expression)
            self.history_box.insert("end", f"{original} = {final}\n")
        except:
            self.display.set("Error")
            self.expression = ""

    def toggle_history_view(self):
        self.history_shown = not self.history_shown
        if self.history_shown:
            self.history_frame.pack(fill='both', expand=False, padx=10, pady=(0, 5))
            self.clear_history_btn.pack(side='left', padx=5)
        else:
            self.history_frame.pack_forget()
            self.clear_history_btn.pack_forget()

    def flip_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        mode = "dark" if self.is_dark_mode else "light"
        self.theme_btn.configure(text="☀️ Light" if mode == "dark" else "🌙 Dark")
        ctk.set_appearance_mode(mode)
        self.build_buttons()

    def clear_history(self):
        self.history_box.delete("1.0", "end")

    def handle_keypress(self, evt):
        key = evt.char
        sym = evt.keysym

        if key in '0123456789.+-*/()':
            self.press_key(key.replace('*', '×').replace('/', '÷'))
        elif key == '\r':
            self.evaluate()
        elif sym == 'BackSpace':
            self.delete_last()
        elif sym == 'Escape':
            self.clear_all()
        elif key == '^':
            self.press_key('^')
        elif key == '%':
            self.do_percentage()
        elif key.lower() == 'r':
            self.do_square_root()
        elif sym.lower() == 't':
            self.flip_theme()


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
