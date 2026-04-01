import tkinter as tk
from src.backend import get_topper, get_class_average, get_rank_list

def open_performance_dashboard():
    window = tk.Toplevel()
    window.title("Performance Dashboard")
    window.geometry("600x400")

    topper = get_topper()
    if topper:
        tk.Label(window, text=f"Topper: {topper['name']} ({round(topper['percentage'],2)}%)").pack()

    avg = get_class_average()
    tk.Label(window, text=f"Class Average: {round(avg,2)}%").pack()

    tk.Label(window, text="Rank List").pack()

    for i, s in enumerate(get_rank_list(), start=1):
        tk.Label(window, text=f"{i}. {s['name']} - {round(s['percentage'],2)}%").pack()