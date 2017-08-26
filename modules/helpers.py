from classfile import Timetable
from classfile import Stream
from classfile import Course
from classfile import returnDictionary

# Function that takes a day of the week formatted as a string
# and returns an integer, 0 = Monday, 6 = Sunday
def day_to_int(day):
    if day.lower() == "monday":
        return 0
    elif day.lower() == "tuesday":
        return 1
    elif day.lower() == "wednesday":
        return 2
    elif day.lower() == "thursday":
        return 3
    elif day.lower() == "friday":
        return 4
    elif day.lower() == "saturday":
        return 5
    elif day.lower() == "sunday":
        return 6
    else:
        return None

# Function that takes a day of the week as an integer and returns a string
def int_to_day(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"
    else:
        return None

# Function that takes a timetable and tells you the
# course codes with stream names, returning a list of strings
def get_stream_names_from_timetable(timetable):
    names = []
    for i in timetable.streams:
        names.append(i.code + " " + i.name)
    return names

# Function that takes a course code and a stream name and tells you
# When classes in the stream are on, returning a list of strings
def get_classes_from_stream(coursecode, streamname):
    classes = []
    course = returnDictionary()[coursecode]
    for i in course.streams:
        if i != 0:
            for j in i:
                for k in range(len(j.days)):
                    if j.name == streamname:
                        nextClass = (int_to_day(j.days[k]))
                        nextClass += (" " + str(j.starts[k]))
                        nextClass += ("-" + str(j.ends[k]))
                        classes.append(nextClass)
    return classes
