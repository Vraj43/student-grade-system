# 🎓 Student Grade Management System

A simple desktop-based Student Management System built using Python and Tkinter.  
This application allows you to manage student records, marks, and performance analytics efficiently.

---

## 🚀 Features

### 👨‍🎓 Student Management
- Add new students
- Update student details
- Delete students
- View all students in a structured table

### 📊 Marks Management
- Add subject-wise marks for each student
- Automatically stored in JSON format

### 📈 Performance Analytics
- Calculate percentage and GPA
- View class average
- Identify topper
- Rank list generation

### 🔍 Search & Filter
- Search students by name or ID
- Filter students by class

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (GUI)
- **JSON** (Data storage)

---

## 📂 Project Structure
Student Grade Management System/
│
├── main.py
├── src/
│ ├── backend.py
│ └── config.py
│
├── ui/
│ ├── main_window.py
│ ├── add_student_ui.py
│ ├── add_marks_ui.py
│ └── performance_ui.py
│
├── data/
│ ├── students.json
│ └── marks.json
│
└── README.md

---

## ⚙️ How It Works

- Student data is stored in:  
  📄 :contentReference[oaicite:0]{index=0}  

- Marks data is stored in:  
  📄 :contentReference[oaicite:1]{index=1}  

- Backend handles:
  - Data storage
  - Calculations (percentage, GPA)
  - Search & filtering  
  📄 :contentReference[oaicite:2]{index=2}  

- GUI is built using Tkinter:  
  📄 :contentReference[oaicite:3]{index=3}  

---

## ▶️ How to Run

1. Install Python (3.x recommended)

2. Clone or download the project

3. Run the application:

```bash
python main.py