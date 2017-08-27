import sys
import ctypes
import tkinter as tk
sys.path.append("../modules")
import output_timetables as ot
from data_interact import does_course_exist

checked_subject_codes = []

# Function for when return is hit in the checkbox
def hit_return(event):
    check_codes()

def check_codes():
    # Get subject codes from text boxes
    subject_code = str(subject_tbx.get())

    # Clear the textbox
    subject_tbx.delete(0, 'end')

    # Put them into an array

    # Check that text has been inputted
    if subject_code == "":
        subject_check_error.set("Enter a subject")

    else:
        if does_course_exist(subject_code):
            if checked_subject_codes.count(subject_code) == 0:
                checked_subject_codes.append(subject_code)
                added_subjects.set("Added subjects: " + ", ".join(checked_subject_codes))
                subject_check_error.set("")
            else:
                subject_check_error.set("You've already entered this subject")

        else:
            subject_check_error.set("This in an invalid subject")


def submit_codes():
    if len(checked_subject_codes) != 0:
        ot.output_timetables(checked_subject_codes)
    else:
        subject_check_error.set("Add some subjects")


def reset():
    subject_tbx.delete(0, 'end')
    subject_check_error.set("")
    checked_subject_codes.clear()
    added_subjects.set("Added subjects: ")

# Set widget fonts
font_head = ""
font_body = ""
if 'win' in sys.platform:  # If windows
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    font_head = "Segoe UI semilight"
    font_body = "Segoe UI"

# Create window
window = tk.Tk()
window.configure(background="white")
#window.minsize(width = 800, height = 600)

# Give window a title
window.title("UQ Timetable Optimizer")

# Variables for widgets
subject_check_error = tk.StringVar()
added_subjects = tk.StringVar()
added_subjects.set("Added subjects:")

entry_width = None  # Width of text boxes
font_head_size = 16
font_body_size = 12

# Create widgets
# Label saying to enter codes
subject_lbl = tk.Label(window, text="Enter your subject codes:", font=(font_head, font_head_size))
# Entry field for entering codes
subject_tbx = tk.Entry(window, width=entry_width, justify="center", font=(font_body, font_body_size), relief="solid")
subject_tbx.bind('<Return>', hit_return)
subject_tbx.focus_set()
# Button for adding them
add_subject_btn = tk.Button(window, text="Add", command=check_codes, font=(font_body, font_body_size), relief="flat")
# List of added subjects (currently label, TODO change to list)
added_subjects_lbl = tk.Label(window, text="Added subjects:", textvariable=added_subjects, font=(font_body, font_body_size))
subject_check_lbl = tk.Label(window, text="", textvariable=subject_check_error, font=(font_body, font_body_size))

# Label for setting options
options_lbl = tk.Label(window, text="Options:", font=(font_head, font_head_size))
# TODO: add options

# Button for outputting timetables
output_timetables_btn = tk.Button(window, text="Output timetables", command=submit_codes, font=(font_body, font_body_size), relief="flat")
# Button for clearing selection
reset_btn = tk.Button(window, text="Clear", command=reset, font=(font_body, font_body_size), relief="flat")

# Align widgets to grid
subject_lbl.grid(row=0, columnspan=2, padx=10, pady=10)
subject_tbx.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
add_subject_btn.grid(row = 1, column=1, padx=5, pady=5, ipadx=5, sticky="we")
added_subjects_lbl.grid(row=2, columnspan=2, padx=5, pady=5)
subject_check_lbl.grid(row = 3, columnspan=2, padx=5, pady=5)

options_lbl.grid(row=4, columnspan=2, padx=5, pady=5)
output_timetables_btn.grid(row=5, column=0, padx=5, pady=5, ipadx=5, sticky="we")
reset_btn.grid(row=5, column=1, padx=5, pady=5, ipadx=5, sticky="we")

# Give widgets white background
subject_lbl.configure(background="white")
subject_tbx.configure(background="white")
added_subjects_lbl.configure(background="white")
subject_check_lbl.configure(background="white")

options_lbl.configure(background="white")

# Show window
window.mainloop()
