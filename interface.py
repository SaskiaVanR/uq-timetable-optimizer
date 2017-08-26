from urllib import request

import tkinter as tk

file_name = "timetables.html"

def output_timetable():
    thing = True

# Create window
window = tk.Tk()
window.configure(background="white")

# Give window a title
window.title("UQ Timetable Optimizer")

window.geometry('320x480')

entry_width = 12

subject_lbl = tk.Label(window, text = "Enter your subject codes (leave blank if N/A):")
subject_1_lbl = tk.Label(window, text="Subject 1", justify="right")
subject_1_tbx = tk.Entry(window, width=entry_width)
subject_2_lbl = tk.Label(window, text="Subject 2", justify="right")
subject_2_tbx = tk.Entry(window, width=entry_width)
subject_3_lbl = tk.Label(window, text="Subject 3", justify="right")
subject_3_tbx = tk.Entry(window, width=entry_width)
subject_4_lbl = tk.Label(window, text="Subject 4", justify="right")
subject_4_tbx = tk.Entry(window, width=entry_width)

subject_lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
subject_1_lbl.grid(row=1, column=0, sticky="e", padx=5, pady=5)
subject_1_tbx.grid(row=1, column=1, padx=5, pady=5)
subject_2_lbl.grid(row=2, column=0, sticky="e", padx=5, pady=5)
subject_2_tbx.grid(row=2, column=1, padx=5, pady=5)
subject_3_lbl.grid(row=3, column=0, sticky="e", padx=5, pady=5)
subject_3_tbx.grid(row=3, column=1, padx=5, pady=5)
subject_4_lbl.grid(row=4, column=0, sticky="e", padx=5, pady=5)
subject_4_tbx.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
