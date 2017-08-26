import output_timetables as ot

import tkinter as tk


def check_codes():
    subject_1_code = str(subject_1_tbx.get())
    subject_2_code = str(subject_2_tbx.get())
    subject_3_code = str(subject_3_tbx.get())
    subject_4_code = str(subject_4_tbx.get())

    subject_codes = [subject_1_code, subject_2_code, subject_3_code, subject_4_code]

    ot.output_timetables(subject_codes)

# Create window
window = tk.Tk()
window.configure(background="white")

# Give window a title
window.title("UQ Timetable Optimizer")

window.geometry('320x480')

entry_width = 12

subject_lbl = tk.Label(window, text="Enter your subject (leave blank when N/A):")
subject_1_lbl = tk.Label(window, text="Subject 1", justify="right")
subject_1_tbx = tk.Entry(window, width=entry_width)
subject_2_lbl = tk.Label(window, text="Subject 2", justify="right")
subject_2_tbx = tk.Entry(window, width=entry_width)
subject_3_lbl = tk.Label(window, text="Subject 3", justify="right")
subject_3_tbx = tk.Entry(window, width=entry_width)
subject_4_lbl = tk.Label(window, text="Subject 4", justify="right")
subject_4_tbx = tk.Entry(window, width=entry_width)
options_lbl = tk.Label(window, text="Options:")
output_timetables_btn = tk.Button(window, text="Output timetables", command=check_codes)


subject_lbl.grid(row=0, columnspan=2, padx=5, pady=5)
subject_1_lbl.grid(row=1, column=0, sticky="e", padx=5, pady=5)
subject_1_tbx.grid(row=1, column=1, padx=5, pady=5)
subject_2_lbl.grid(row=2, column=0, sticky="e", padx=5, pady=5)
subject_2_tbx.grid(row=2, column=1, padx=5, pady=5)
subject_3_lbl.grid(row=3, column=0, sticky="e", padx=5, pady=5)
subject_3_tbx.grid(row=3, column=1, padx=5, pady=5)
subject_4_lbl.grid(row=4, column=0, sticky="e", padx=5, pady=5)
subject_4_tbx.grid(row=4, column=1, padx=5, pady=5)
options_lbl.grid(row=5, columnspan=2, padx=5, pady=5)
output_timetables_btn.grid(row=6, columnspan=2, padx=5, pady=5)

subject_lbl.configure(background="white")
subject_1_lbl.configure(background="white")
subject_1_tbx.configure(background="white")
subject_2_lbl.configure(background="white")
subject_2_tbx.configure(background="white")
subject_3_lbl.configure(background="white")
subject_3_tbx.configure(background="white")
subject_4_lbl.configure(background="white")
subject_4_tbx.configure(background="white")
options_lbl.configure(background="white")

window.mainloop()
