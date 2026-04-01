import tkinter as tk
from src.backend import add_students

def open_add_student():
    window = tk.Toplevel()
    window.title("Add Student")

    tk.Label(window, text="ID").pack()
    sid = tk.Entry(window)
    sid.pack()

    tk.Label(window, text="Name").pack()
    name = tk.Entry(window)
    name.pack()

    tk.Label(window, text="Age").pack()
    age = tk.Entry(window)
    age.pack()

    tk.Label(window, text="Class").pack()
    cls = tk.Entry(window)
    cls.pack()

    def submit():
        add_students(sid.get(), name.get(), age.get(), cls.get())
        window.destroy()

    tk.Button(window, text="Submit", command=submit).pack()