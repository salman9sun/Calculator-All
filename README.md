# Calculator
My Project,
Download Now(●'◡'●)


https://drive.google.com/file/d/1zvNPEAvZpcsSHNJ2GgOnN6DD9QhuDS6i/view?usp=sharing

# 🧮 CustomTkinter Calculator App

A modern, user-friendly calculator built with Python and CustomTkinter. This project features dynamic theming, expression evaluation, and a history panel, demonstrating GUI development using object-oriented principles.

## 🚀 Features

- 🌓 Light/Dark theme toggle  
- 🧠 Calculation history with clear option  
- 📱 Responsive display with auto font adjustment  
- ➗ Square root and percentage operations  
- 🔁 ANS (last answer) reuse  
- ⌨️ Keyboard shortcuts (Enter, Backspace, r, t, etc.)  
- 🚫 Error handling for invalid operations  

## 🖥️ UI Overview

- Default window size: `350x650 px`  
- Control buttons: History, Clear, Theme  
- Read-only expression display  
- 4×6 calculator button grid  

## ⚙️ Installation

Make sure you have Python 3.x installed. Then, install the required library:

```bash
pip install customtkinter
```

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/customtkinter-calculator.git
cd customtkinter-calculator
```

## ▶️ Running the App

Simply run the main Python file:

```bash
python calculator.py
```

If you're using an icon (`calcu.ico`), ensure the path is correct or update it in the script.

## 🎯 Keyboard Shortcuts

| Key              | Action                          |
|------------------|---------------------------------|
| 0-9, + - * / ( ) | Input numbers/operators       |
| Enter            | Evaluate expression             |
| Backspace        | Delete last character           |
| Esc              | Clear entire expression         |
| r                | Square root                     |
| t                | Toggle theme                    |
| %                | Percentage                      |
| ^                | Power                           |

## 🧠 Logic

- Evaluates sanitized expressions using `eval()`  
- Custom symbol replacement (`× → *`, `÷ → /`, `^ → **`)  
- Percentage logic applies contextual calculations (e.g., `20 - 60%` → `8`)  
- Handles edge cases like division by zero or invalid input gracefully  

## 🛠️ Tech Stack

- Python 3.x  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- Tkinter (base GUI)  
- Object-Oriented Design  

## ❗ Known Issues

- Limited to basic arithmetic  
- No complex number support  
- Expression parser relies on `eval()` (safe due to sanitization, but still basic)  

## 🤝 Contributing

Feel free to fork the project and submit pull requests! Suggestions and improvements are welcome.

1. Fork this repo  
2. Create your feature branch: `git checkout -b feature/YourFeature`  
3. Commit your changes: `git commit -m "Add YourFeature"`  
4. Push to the branch: `git push origin feature/YourFeature`  
5. Open a pull request  

## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

## 🙌 Acknowledgements

- [freeCodeCamp](https://www.youtube.com/c/Freecodecamp)  
- [Tech With Tim](https://www.youtube.com/@TechWithTim)  
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com)  

---

> 🔎 **Tip:** Start small, test often, and add features gradually!

---

### 👤 Author

**Salman Farsi**
