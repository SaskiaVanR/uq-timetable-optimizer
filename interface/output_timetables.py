import sys
import ctypes
import tkinter as tk
from tkinter import ttk
sys.path.append("../modules")
import branchandbound
import helpers


def output_timetables(subject_codes):

    i = 0
    while i<len(subject_codes):
        subject_codes[i] = subject_codes[i].upper()
        i+=1

    nodes = branchandbound.optimize(subject_codes)
    print(nodes[0].timetable.streams)

    window = tk.Tk()
    window.configure(background="white")

    window.title("Optimized Timetables")

    note = ttk.Notebook(window)

    font_head = ""
    font_body = ""
    if 'win' in sys.platform:  # If windows
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        font_head = "Segoe UI semilight"
        font_body = "Segoe UI"

    font_head_size = 16
    font_body_size = 12

    frames = []

    classes = []

    days = []

    times = []
    numSolutions = len(nodes)


    if len(nodes)>10:
        nodes = nodes[:10]


    for nindex, n in enumerate(nodes):

        frames += [ttk.Frame(note)]
        note.add(frames[nindex], text='Option '+str(nindex+1))

        for sindex, s in enumerate(n.timetable.streams):
            for dindex, d in enumerate(s.days):
                classes += [tk.Label(frames[nindex], text=s.code + '\n' + s.name + " " + str(s.starts[dindex]))]

                classes[-1].grid(column=s.days[dindex]+1, row=s.starts[dindex]+1,
                                     rowspan=s.ends[dindex]-s.starts[dindex], sticky="ns")

                classes[-1].configure(background="white")

        for i in range(7):
            days += [tk.Label(frames[nindex], text=helpers.int_to_day(i))]
            days[-1].grid(column=i+1, row=0)

        for i in range(8,21):
            times += [tk.Label(frames[nindex], text=str(i)+":00\n")]
            times[-1].grid(column=0, row=i+1)

    note.pack()

    window.mainloop()