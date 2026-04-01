import tkinter as tk
from src.backend import add_students

def open_add_student():
    window = tk.Toplevel()
    window.title("Add Student")

    tk.Label(window, text="ID").pack()
    entry_id = tk.Entry(window)
    entry_id.pack()

    tk.Label(window, text="Name").pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    tk.Label(window, text="Age").pack()
    entry_age = tk.Entry(window)
    entry_age.pack()

    tk.Label(window, text="Class").pack()
    entry_class = tk.Entry(window)
    entry_class.pack()

    def submit():
        add_students(
            entry_id.get(),
            entry_name.get(),
            entry_age.get(),
            entry_class.get()
        )

    tk.Button(window, text="Submit", command=submit).pack()