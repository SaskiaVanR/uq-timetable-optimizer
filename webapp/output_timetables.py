import classfile


def output_timetables(subject_codes):

    timetable = classfile.getTestTimetable()
    print(timetable)

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
    </nav>\n
    ''')

    for i in timetable:
        timetables_file.write("<tr><td>" + "" + "</td></tr>\n")

    timetables_file.write("</body>\n</html>")
