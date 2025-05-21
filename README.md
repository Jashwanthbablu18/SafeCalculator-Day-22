# 🧮 Day 22 - Safe Calculator with Exception Handling

Hey there! 👋  
Welcome to **Day 22** of my **#30DaysOfPythonChallenge**. Today I focused on making programs more **error-resilient** using Python’s exception handling system.

---

## 📌 What’s This About?
Today’s focus:
- Using `try`, `except`, and `raise` to manage errors gracefully
- Handling common input and runtime issues in a calculator app

---

## 💭 Why Is This Useful?
Users can (and will) make mistakes — bad inputs, typos, even dividing by zero!  
Exception handling ensures your program doesn't crash, and gives helpful feedback instead. ✅

---

## 💡 Features

Here’s what the app supports:
- 🧪 Input validation for numbers and operators
- ⚠️ Graceful error handling:
  - `ValueError` for invalid numbers or operators
  - `ZeroDivisionError` for division by zero
- 🔁 Loop until user enters `q` to quit
- 📢 User-friendly messages instead of crashes

---

## 🛠️ Tech Stuff

Built with:
- 🐍 **Python 3**
- 🧯 `try`, `except`, `raise` blocks
- 🧠 Logical checks for safe execution

---

## 🚀 Getting It Running

### ✅ What You’ll Need
Just Python 3!  
Run the program with:
```bash
python Day-22Code.py
