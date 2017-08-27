import tkinter as tk
from tkinter import ttk
import branchandbound
import webbrowser


def output_timetables(subject_codes):

    nodes = branchandbound.optimize(subject_codes)
    print(nodes[0].timetable.streams)

    window = tk.Tk()
    window.configure(background="white")

    window.title("Optimized Timetables")

    tabs = ttk.Notebook(window)

    frames = []

    for n in nodes:
        frames[n] = ttk.Frame(tabs)

    window.mainloop()