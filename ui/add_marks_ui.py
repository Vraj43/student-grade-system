import tkinter as tk
from src.backend import add_marks

def open_add_marks():
    window = tk.Toplevel()
    window.title("Add Marks")

    tk.Label(window, text="Student ID").pack()
    sid = tk.Entry(window)
    sid.pack()

    tk.Label(window, text="Subject").pack()
    subject = tk.Entry(window)
    subject.pack()

    tk.Label(window, text="Marks").pack()
    marks = tk.Entry(window)
    marks.pack()

    def submit():
        add_marks(sid.get(), subject.get(), marks.get())
        window.destroy()

    tk.Button(window, text="Submit", command=submit).pack()