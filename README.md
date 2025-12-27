# Python Complete Course 🐍

Welcome to the **Python Complete Course** repository!  
This repository documents my Python learning journey from **beginner to advanced**, organized **class by class**.

---

## 📚 Course Overview
This course is designed for **beginners** who want to learn Python **step by step**.  
Each class contains:

- Clear Python examples  
- Simple explanations  
- Practice-friendly code  

---

## 🧠 Topics Covered
### ✅ Class 01 – Introduction to Python
- What is Python?  
- Printing output  
- Basic syntax  
- Comments  
- Running Python code  

### ✅ Class 02 – Variables & Data Types
- Strings (`str`)  
- Integers (`int`)  
- Floats (`float`)  
- Type hints  
- Lists basics  
- List methods: `append`, `extend`, `remove`  

### ✅ Class 03 – Operators & Calculators
- Arithmetic operators: `+`, `-`, `*`, `/`  
- Assignment operators  
- Simple calculator with Python / Streamlit  
- Practical exercises  

### ✅ Class 04 – Coming Soon
- Conditional statements  
- Loops  
- Functions  
- File handling  
- Object-Oriented Programming  
- Mini projects  

---

## 📁 Folder Structure
```text
python-complete-course/
│
├── class-01/
│   └── hello_world.py
│
├── class-02/
│   └── lists_and_variables.py
│
├── class-03/
│   └── calculator.py
│
├── class-04/   # Coming soon
│
└── README.md
🧪 Example Code
Hello World
python
Copy code
print("Hello, World!")
print("This is a simple Python script.")
List Example
python
Copy code
party_items: list[str] = ["samosa", "pani puri", "chocolate", "roll"]

party_items.append("ice cream")
party_items.extend(["chips", "cookies"])
party_items.remove("pani puri")

print(party_items)
Simple Calculator (Streamlit)
python
Copy code
import streamlit as st

st.title("Simple Calculator")
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero not allowed")
            result = None
    if result is not None:
        st.success(f"Result: {result}")
🎯 Goals of This Repository
Build strong Python fundamentals

Practice clean and readable code

Prepare for exams and real-world projects

Track learning progress on GitHub

🚀 Future Plan
Conditional statements

Loops

Functions

File handling

Object-Oriented Programming

Mini projects

👨‍💻 Author
Affan

Learning Python step by step

Uploading regular updates

⭐ Support
If you find this repository helpful:

Give it a ⭐

Follow for updates

yaml
Copy code
