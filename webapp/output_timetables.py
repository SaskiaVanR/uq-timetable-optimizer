from urllib import *

def output_timetables(subject_codes):

    timetables = []

    file_name = "timetables.html"
    timetables_file = open(file_name, "w")

    timetables_file.write('''
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/css/materialize.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/js/materialize.min.js"></script>
    <head>
    <body>

    ''')

    for i in timetables:
        timetables_file.write("<tr><td>" + "</td></tr>\n")

    timetables_file.write("</body>")