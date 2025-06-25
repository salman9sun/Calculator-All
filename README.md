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
Calculator7.py
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



> 🔎 **Tip:** Start small, test often, and add features gradually!

---

### 👤 Author

**Salman Farsi**

# 🧮 CustomTkinter Calculator

A modern and customizable calculator app built using **Python** and **CustomTkinter**.  
It supports:

- ✅ Light & dark themes  
- ✅ Calculation history  
- ✅ Keyboard input support  
- ✅ Advanced operations: square root, exponentiation, percentage, and more

![calculator-preview](https://via.placeholder.com/800x400?text=Calculator+Screenshot) <!-- Replace with real image -->

---

## 📥 Download

[![Download Calculator](https://img.shields.io/badge/Download-.exe-blue?style=for-the-badge&logo=windows)](https://github.com/yourusername/your-repo-name/releases)

> 🔗 Click the badge above to download the latest `.exe` version — no Python required!

---

## 🔧 How to Create `.exe` File

You can turn the calculator script into a Windows `.exe` file using **PyInstaller**.

### ✅ Requirements

- Python installed (`python --version`)
- Pip installed (`pip --version`)
- `calculator.py` file (this script)
- Optional: a `.ico` icon (`calcu.ico`) for branding

### 🚀 Steps

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
## 🏗️ Build the `.exe` File

You can convert the Python script into a standalone `.exe` using **PyInstaller**.

### 📁 Navigate to the Project Folder

```bash
cd "C:\Path\To\Your\Calculator"
⚙️ Create the .exe File
```bash
pyinstaller --noconsole --onefile --icon=calcu.ico calculator.py
Option	Meaning
--noconsole	Hide the terminal window (for GUI apps)
--onefile	Pack everything into one .exe file
--icon=...	Add a custom icon (optional)

📂 Find the Output
Your final .exe will be located in the dist/ folder:

```bash
dist/calculator.exe
