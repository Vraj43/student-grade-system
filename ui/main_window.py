import tkinter as tk
from tkinter import ttk, messagebox
from ui.add_student_ui import open_add_student
from src.backend import get_students, delete_students, update_student

def view_students():
    window = tk.Toplevel()
    window.title("All Students")
    window.geometry("700x400")

    columns = ("ID", "Name", "Age", "Class")

    tree = ttk.Treeview(window, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True)

    def load_data():
        tree.delete(*tree.get_children())
        for student in get_students():
            tree.insert("", "end", values=(
                student["student_id"],
                student["name"],
                student["age"],
                student["class_name"]
            ))

    load_data()

    # 🔴 DELETE FUNCTION
    def delete_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student")
            return

        values = tree.item(selected[0])["values"]
        student_id = values[0]

        delete_students(student_id)
        load_data()

    # 🟡 UPDATE FUNCTION
    def update_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student")
            return

        values = tree.item(selected[0])["values"]

        edit_window = tk.Toplevel(window)
        edit_window.title("Update Student")

        tk.Label(edit_window, text="Name").pack()
        name = tk.Entry(edit_window)
        name.insert(0, values[1])
        name.pack()

        tk.Label(edit_window, text="Age").pack()
        age = tk.Entry(edit_window)
        age.insert(0, values[2])
        age.pack()

        tk.Label(edit_window, text="Class").pack()
        class_name = tk.Entry(edit_window)
        class_name.insert(0, values[3])
        class_name.pack()

        def save_update():
            update_student(values[0], name.get(), age.get(), class_name.get())
            load_data()
            edit_window.destroy()

        tk.Button(edit_window, text="Save", command=save_update).pack()

    # Buttons
    tk.Button(window, text="Delete", command=delete_selected).pack(pady=5)
    tk.Button(window, text="Update", command=update_selected).pack(pady=5)


def run_app():
    root = tk.Tk()
    root.title("Student Grade Management System")
    root.geometry("500x400")

    tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Add Student", command=open_add_student).pack(pady=10)
    tk.Button(root, text="View Students", command=view_students).pack(pady=10)

    root.mainloop()