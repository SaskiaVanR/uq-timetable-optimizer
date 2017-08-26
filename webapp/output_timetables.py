import branchandbound
import webbrowser


def output_timetables(subject_codes):

    nodes = branchandbound.optimize(subject_codes)
    print(nodes[0].timetable.streams)

    # streams (

    file_name = "timetables.html"
    timetables_file = open(file_name, "w")

    timetables_file.write('''
    <!DOCTYPE html>
    <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/css/materialize.min.css">
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/js/materialize.min.js"></script>
    <head>
    
    <body>
    <nav>
      <div class="nav-wrapper">
        <a href="#" class="brand-logo center">Here are your optimized timetables:</a>
      </div>
    </nav>
    <div class="row">
    <div class="col s12">
      <ul class="tabs">
    ''')

    for i in range(len(nodes)):
        timetables_file.write('    <li class="tab col s3"><a href="#timetable' + str(i+1) + '">Option ' + str(i+1) + '</a></li>')

    timetables_file.write('''
      </ul>
    </div>
    \n''')

    for i in range(len(nodes)):
        timetables_file.write('<div id="timetable' + str(i+1) + '" class="col s12">')
        timetables_file.write('''
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
        </thead>
        ''')

        timetables_file.write('</table></div>')

    # # Create a 2D array for the timetable
    # timetablegrid = [[""] * 24]
    # for i in range(7):
    #     timetablegrid.append([""] * 24)
    #
    # for i in timetable.streams:
    #     if i == 0:
    #         timetables_file.write("<tr><td>" + timetable.codes[i] + "</td></tr>\n")
    #         timetables_file.write("<tr><td>" + timetable.streams[i] + "</td></tr>\n")
    #     # Update the 2D array
    #     for j in range(len(i.days)):
    #         for k in range(i.ends[j] - i.starts[j]):
    #             timetablegrid[i.days[j]][i.starts[j] + k] = i.name
    #
    # for time in range(1, 24):
    #     for day in range(0,4):
    #         if time == timetable.streams.starts[0]:
    #             D = 1

    timetables_file.write("</body>\n</html>")
    webbrowser.open(file_name)