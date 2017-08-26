import sys
import ctypes
import tkinter as tk

import output_timetables as ot
from data_interact import does_course_exist


def check_codes():
    subject_1_code = str(subject_1_tbx.get())
    subject_2_code = str(subject_2_tbx.get())
    subject_3_code = str(subject_3_tbx.get())
    subject_4_code = str(subject_4_tbx.get())

    subject_codes = [subject_1_code, subject_2_code, subject_3_code, subject_4_code]
    subject_codes = list(filter(None, subject_codes))

    all_codes_valid = True

    if len(subject_codes) == 0:
        subject_check_error.set("Enter some subjects")

    elif len(subject_codes) == len(set(subject_codes)):

        for i in subject_codes:
            # Check the code exists
            if does_course_exist(i) is False:
                all_codes_valid = False

        if all_codes_valid:
            ot.output_timetables(subject_codes)
        else:
            subject_check_error.set("There are invalid subjects")

    else:
        subject_check_error.set("There are duplicate subjects")

font_head = ""
font_body = ""
if 'win' in sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    font_head = "Segoe UI semilight"
    font_body = "Segoe UI"

# Create window
window = tk.Tk()
window.configure(background="white")

# Give window a title
window.title("UQ Timetable Optimizer")

subject_check_error = tk.StringVar()

entry_width = None
font_size = 12

subject_lbl = tk.Label(window, text="Enter your subjects (leave blank when N/A):", font=(font_head, 16))
subject_1_lbl = tk.Label(window, text="Subject 1", justify="right", font=(font_body, font_size))
subject_1_tbx = tk.Entry(window, width=entry_width, font=(font_body, font_size))
subject_2_lbl = tk.Label(window, text="Subject 2", justify="right", font=(font_body, font_size))
subject_2_tbx = tk.Entry(window, width=entry_width, font=(font_body, font_size))
subject_3_lbl = tk.Label(window, text="Subject 3", justify="right", font=(font_body, font_size))
subject_3_tbx = tk.Entry(window, width=entry_width, font=(font_body, font_size))
subject_4_lbl = tk.Label(window, text="Subject 4", justify="right", font=(font_body, font_size))
subject_4_tbx = tk.Entry(window, width=entry_width, font=(font_body, font_size))
subject_check_lbl = tk.Label(window, text="", textvariable=subject_check_error, font=(font_body, font_size))
options_lbl = tk.Label(window, text="Options:", font=(font_head, 16))
output_timetables_btn = tk.Button(window, text="Output timetables", command=check_codes, font=(font_body, font_size))


subject_lbl.grid(row=0, columnspan=2, padx=10, pady=10)
subject_1_lbl.grid(row=1, column=0, sticky="e", padx=5, pady=5)
subject_1_tbx.grid(row=1, column=1, padx=5, pady=5)
subject_2_lbl.grid(row=2, column=0, sticky="e", padx=5, pady=5)
subject_2_tbx.grid(row=2, column=1, padx=5, pady=5)
subject_3_lbl.grid(row=3, column=0, sticky="e", padx=5, pady=5)
subject_3_tbx.grid(row=3, column=1, padx=5, pady=5)
subject_4_lbl.grid(row=4, column=0, sticky="e", padx=5, pady=5)
subject_4_tbx.grid(row=4, column=1, padx=5, pady=5)
subject_check_lbl.grid(row = 5, columnspan=2, padx=5, pady=5)
options_lbl.grid(row=6, columnspan=2, padx=5, pady=5)
output_timetables_btn.grid(row=7, columnspan=2, padx=5, pady=5)

subject_lbl.configure(background="white")
subject_1_lbl.configure(background="white")
subject_1_tbx.configure(background="white")
subject_2_lbl.configure(background="white")
subject_2_tbx.configure(background="white")
subject_3_lbl.configure(background="white")
subject_3_tbx.configure(background="white")
subject_4_lbl.configure(background="white")
subject_4_tbx.configure(background="white")
subject_check_lbl.configure(background="white")
options_lbl.configure(background="white")

window.mainloop()
