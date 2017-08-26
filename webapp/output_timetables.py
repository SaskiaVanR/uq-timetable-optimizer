import classfile


def output_timetables(subject_codes):

    timetable = classfile.get_test_timetable()
    print(timetable.streams)

    file_name = "timetables.html"
    timetables_file = open(file_name, "w")

    timetables_file.write('''
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/css/materialize.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/js/materialize.min.js"></script>
    <head>
    
    <body>
    <nav>
      <div class="nav-wrapper">
        <a href="#" class="brand-logo center">Here are your optimized timetables:</a>
      </div>
    </nav>
    <table>
    <thead>
      <tr>
        <th>Time</th>
        <th>Monday</th>
        <th>Tuesday</th>
        <th>Wednesday</th>
        <th>Thursday</th>
        <th>Friday</th>
      </tr>
    </thead>\n
    ''')

    # Create a 2D array for the timetable
    timetablegrid = [[""] * 24]
    for i in range(7):
        timetablegrid.append([""] * 24)

    for i in timetable.streams:
        if i == 0:
            timetables_file.write("<tr><td>" + timetable.codes[i] + "</td></tr>\n")
            timetables_file.write("<tr><td>" + timetable.streams[i] + "</td></tr>\n")
        # Update the 2D array
        for j in range(len(i.days)):
            for k in range(i.ends[j] - i.starts[j]):
                timetablegrid[i.days[j]][i.starts[j] + k] = i.name

    for time in range(1, 24):
        for day in range(0,4):
            if time == timetable.streams.starts[0]:
                D = 1

    timetables_file.write("</table></body>\n</html>")
