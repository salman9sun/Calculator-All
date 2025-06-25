# 🧮 CustomTkinter Calculator

A modern and customizable calculator app built using **Python** and **CustomTkinter**.


---

## 📥 Download

> 🖱️ Click below to download the latest `.exe` version — **no Python required**:

[![Download Calculator](https://img.shields.io/badge/Download-.exe-blue?style=for-the-badge&logo=windows)](
https://drive.google.com/file/d/1zvNPEAvZpcsSHNJ2GgOnN6DD9QhuDS6i/view?usp=sharing)

---

## 🚀 Features

- 🌓 **Light/Dark theme toggle**  
- 🧠 **Calculation history** with clear option  
- 📱 **Responsive display** with auto font scaling  
- ➗ **Advanced operations**: square root, exponentiation, percentage  
- 🔁 **ANS (last answer)** memory  
- ⌨️ **Keyboard shortcuts** for efficiency  
- 🚫 **Robust error handling**

---

## 🖥️ UI Overview

- Window size: `350x650 px`  
- Expression display (read-only)  
- 4×6 calculator button grid  
- Control buttons: History | Clear History | Toggle Theme  

---

## ⌨️ Keyboard Shortcuts

| Key              | Action                          |
|------------------|---------------------------------|
| 0-9, + - × ÷ ( ) | Input numbers/operators         |
| `Enter`          | Evaluate expression             |
| `Backspace`      | Delete last character           |
| `Esc`            | Clear entire expression         |
| `r`              | Square root                     |
| `t`              | Toggle light/dark theme         |
| `%`              | Percentage                      |
| `^`              | Power                           |

---

## 🧠 Logic & Safety

- Expression sanitization:  
  - `× → *`, `÷ → /`, `^ → **`  
- `eval()` safely evaluates cleaned expressions  
- Percentage logic handles contextual expressions (e.g., `20 - 60%` → `8`)  
- Catches and reports invalid input or division by zero  

---

## 🔧 Installation & Setup

### ✅ Requirements

- Python 3.x  
- [`customtkinter`]

### 📦 Install Dependencies

```bash
pip install customtkinter
```

### ▶️ Run the App

```bash
python Calculator7.py
```

> Make sure `calcu.ico` (icon file) is in the same folder or update its path in the script.

---

## 🏗️ Convert to `.exe` (Standalone App)

You can convert this app into a single `.exe` using **PyInstaller**.

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Navigate to Your Project Folder

```bash
cd "C:\Path\To\Your\Calculator"
```

### 3. Build the `.exe`

```bash
pyinstaller --noconsole --onefile --icon=calcu.ico Calculator7.py
```

| Option       | Description                         |
|--------------|-------------------------------------|
| `--noconsole`| Hide terminal window (for GUI apps) |
| `--onefile`  | Bundle into a single `.exe` file     |
| `--icon`     | Use a custom icon                   |

### 4. Find the Output

The `.exe` will be inside the `dist/` folder:

```bash
dist/Calculator7.exe
```

---

## 🛠️ Tech Stack

- 🐍 Python 3.x  
- 🧱 CustomTkinter (modern UI library built on Tkinter)  
- 💻 Tkinter (base GUI framework)  
- 🧩 Object-Oriented Programming  

---

## ❗ Known Limitations

- Basic arithmetic only (no scientific or complex math)  
- Expression parsing limited by Python's `eval()`  
- No graphing or equation solving  

---

## 👤 Author

**Salman Farsi**  
[GitHub](https://github.com/salman9sun) · 

---

> 🔎 *Tip: Start small, test often, and improve gradually. Happy coding!*
