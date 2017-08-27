import sys
import ctypes
import tkinter as tk
from tkinter import ttk
from tkinter import font
sys.path.append("../modules")
import branchandbound
import helpers


def output_timetables(subject_codes, max_hours, search_type, ignored_types):

    i = 0
    while i<len(subject_codes):
        subject_codes[i] = subject_codes[i].upper()
        i += 1

    # Remove ignored types
    if len(ignored_types) > 0:
        for i in subject_codes:
            helpers.remove_streams_from_course_name(i, ignored_types)

    nodes = []
    if search_type == 1:
        nodes = branchandbound.optimize(subject_codes, max_hours)
    else:
        nodes = branchandbound.optimizeDays(subject_codes, max_hours)

    window = tk.Tk()
    window.configure(background="white")

    window.title("Optimized Timetables")

    font_head = ""
    font_body = ""
    if 'win' in sys.platform:  # If windows
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        font_head = "Segoe UI semilight"
        font_body = "Segoe UI"

    font_head_size = 16
    font_body_size = 12

    ttk.Style().configure('.', font=font_body)

    frames = []
    background_grid = []
    classes = []
    days = []
    times = []

    numSolutions = len(nodes)

    if len(nodes)>10:
        nodes = nodes[:10]

    note = ttk.Notebook(window)

    for nindex, n in enumerate(nodes):

        frames += [ttk.Frame(note)]
        note.add(frames[nindex], text='Option '+str(nindex+1))

        for x in range(8):
            for y in range(8, 21):
                background_grid += [tk.Label(frames[nindex], text="", relief="groove", borderwidth=1)]
                background_grid[-1].grid(column=x, row=y+1, sticky="nsew")
                background_grid[-1].configure(background="white")

        for sindex, s in enumerate(n.timetable.streams):
            for dindex, d in enumerate(s.days):
                classes += [tk.Label(frames[nindex], text=s.code + '\n' + s.name, relief="groove", borderwidth=1, font=(font_body, font_body_size))]

                classes[-1].grid(column=s.days[dindex]+1, row=s.starts[dindex]+1,
                                     rowspan=s.ends[dindex]-s.starts[dindex], sticky="nsew", ipadx=5, ipady=5)
                #classes[-1].configure(background="#e5eefc")

        for i in range(7):
            days += [tk.Label(frames[nindex], text=helpers.int_to_day(i), relief="groove", borderwidth=1, font=(font_body, font_body_size))]
            days[-1].grid(column=i+1, row=0, sticky='nsew', ipadx=5, ipady=5)
            days[-1].configure(background="white")

        for i in range(8,21):
            times += [tk.Label(frames[nindex], text=str(i)+":00\n", relief="groove", borderwidth=1, font=(font_body, font_body_size))]
            times[-1].grid(column=0, row=i+1, sticky='nsew', ipadx=5, ipady=5)
            times[-1].configure(background="white")

    note.pack()

    window.mainloop()
