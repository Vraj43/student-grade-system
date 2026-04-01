import tkinter as tk
from tkinter import ttk

import ui.add_student_ui as add_student_ui
import ui.add_marks_ui as add_marks_ui
import ui.performance_ui as performance_ui
from src.backend import *

# ---------------- VIEW STUDENTS ---------------- #

def view_students():
    window = tk.Toplevel()
    window.title("Students Dashboard")
    window.geometry("1000x550")
    window.configure(bg="#f5f7fa")

    # 🔷 TOP FRAME (SEARCH + FILTER)
    top_frame = tk.Frame(window, bg="#f5f7fa")
    top_frame.pack(pady=10)

    search_entry = tk.Entry(top_frame, width=25, font=("Arial", 11))
    search_entry.grid(row=0, column=0, padx=10)

    filter_entry = tk.Entry(top_frame, width=25, font=("Arial", 11))
    filter_entry.grid(row=0, column=1, padx=10)

    # 🔷 TABLE FRAME
    table_frame = tk.Frame(window)
    table_frame.pack(pady=10, fill="both", expand=True)

    columns = ("ID", "Name", "Age", "Class", "Percentage", "GPA")

    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    tree.pack(fill="both", expand=True)

    # 🔷 STYLE TABLE
    style = ttk.Style()
    style.theme_use("default")

    style.configure("Treeview",
                    background="#ffffff",
                    foreground="black",
                    rowheight=28,
                    fieldbackground="#ffffff")

    style.map("Treeview", background=[("selected", "#4CAF50")])

    # 🔷 LOAD DATA
    def load_data(data=None):
        tree.delete(*tree.get_children())
        students = data if data else get_students()

        for s in students:
            tree.insert("", "end", values=(
                s["student_id"],
                s["name"],
                s["age"],
                s["class_name"],
                round(calculate_percentage(s["student_id"]), 2),
                calculate_gpa(s["student_id"])
            ))

    load_data()

    # 🔷 BUTTON FRAME
    btn_frame = tk.Frame(window, bg="#f5f7fa")
    btn_frame.pack(pady=15)

    def search():
        load_data(search_students(search_entry.get()))

    def apply_filter():
        load_data(filter_students_by_class(filter_entry.get()))

    def delete_selected():
        selected = tree.selection()
        if not selected:
            return
        values = tree.item(selected[0], "values")
        delete_students(values[0])
        load_data()

    def update_selected():
        selected = tree.selection()
        if not selected:
            return

        values = tree.item(selected[0], "values")

        edit = tk.Toplevel(window)
        edit.geometry("300x250")
        edit.title("Update Student")

        tk.Label(edit, text="Name").pack(pady=5)
        name = tk.Entry(edit)
        name.insert(0, values[1])
        name.pack()

        tk.Label(edit, text="Age").pack(pady=5)
        age = tk.Entry(edit)
        age.insert(0, values[2])
        age.pack()

        tk.Label(edit, text="Class").pack(pady=5)
        cls = tk.Entry(edit)
        cls.insert(0, values[3])
        cls.pack()

        def save():
            update_student(values[0], name.get(), age.get(), cls.get())
            load_data()
            edit.destroy()

        tk.Button(edit, text="Save", bg="#4CAF50", fg="white").pack(pady=10)

    # Styled Buttons
    def styled_button(text, command):
        return tk.Button(btn_frame, text=text, command=command,
                         bg="#4CAF50", fg="white",
                         font=("Arial", 11, "bold"),
                         width=15, height=1)

    styled_button("Search", search).grid(row=0, column=0, padx=10)
    styled_button("Filter", apply_filter).grid(row=0, column=1, padx=10)
    styled_button("Delete", delete_selected).grid(row=0, column=2, padx=10)
    styled_button("Update", update_selected).grid(row=0, column=3, padx=10)


# ---------------- MAIN APP ---------------- #

def run_app():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("600x450")
    root.configure(bg="#f5f7fa")

    # 🔷 CENTER FRAME
    frame = tk.Frame(root, bg="#f5f7fa")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # 🔷 TITLE
    tk.Label(frame, text="Student Management System",
             font=("Arial", 18, "bold"),
             bg="#f5f7fa").pack(pady=20)

    # 🔷 BUTTON STYLE
    def main_btn(text, command):
        return tk.Button(frame, text=text, command=command,
                         width=25, height=2,
                         bg="#4CAF50", fg="white",
                         font=("Arial", 12, "bold"),
                         bd=0)

    main_btn("Add Student", add_student_ui.open_add_student).pack(pady=10)
    main_btn("Add Marks", add_marks_ui.open_add_marks).pack(pady=10)
    main_btn("View Students", view_students).pack(pady=10)
    main_btn("Performance Dashboard", performance_ui.open_performance_dashboard).pack(pady=10)

    root.mainloop()