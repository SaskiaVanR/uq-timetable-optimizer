import sys
sys.path.append("../modules")
import branchandbound
import data_interact

# check argv size
if len(sys.argv) < 2:
    sys.stderr.write("USAGE: python3 cli_interface.py <coursecodes>\n")
    sys.exit()

# get arguments
args = sys.argv

# Remove first arg
del args[0]

# Make everything uppercase and check course code
for i in range(len(args)):
    args[i] = args[i].upper()
    if data_interact.does_course_exist(args[i]) == False:
        sys.stderr.write(args[i] + " is not a valid course.\n")
        sys.exit()

# Optimize the timetable
# This will rely on the optimize function printing output
# If that changes this program will also need to be changed
branchandbound.optimize(sys.argv)
