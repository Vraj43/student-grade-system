import tkinter as tk
from ui.add_student_ui import open_add_student
from src.backend import get_students

def view_students():
    window = tk.Toplevel()
    window.title("All Students")

    students = get_students()

    if not students:
        tk.Label(window, text="No students found").pack()
        return

    for student in students:
        text = f"ID: {student['student_id']} | Name: {student['name']} | Age: {student['age']} | Class: {student['class_name']}"
        tk.Label(window, text=text).pack()

def run_app():
    root = tk.Tk()
    root.title("Student Grade Management System")
    root.geometry("500x400")

    tk.Label(root, text="Student Management System").pack()

    btn_add = tk.Button(root, text="Add Student", command=open_add_student)
    btn_add.pack()

    btn_view = tk.Button(root, text="View Students", command=view_students)
    btn_view.pack()

    root.mainloop()