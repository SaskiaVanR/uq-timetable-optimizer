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

# Function that takes a Timetable class and returns a 2D Array of strings
# Array entries are blank for free hours, and not blank for hours with classes
# array[2][13] refers to the class on at 1pm on Wednesday
def get_timetable_array(timetable):
    # Create a 2D array for the timetable
    timetablegrid = [[""] * 24] # one day
    for i in range(7): # Seven days in a week
        timetablegrid.append([""] * 24)
    
    # Fill the array
    for i in timetable.streams:
        # Go over each date/time combo in the stream
        for j in range(len(i.days)):
            for k in range(i.ends[j] - i.starts[j]):
                # Add course code and stream name to array
                timetablegrid[i.days[j]][i.starts[j] + k] \
                        += i.code + " " + i.name
    return timetablegrid


# Function that takes a Course class and removes streams from it
# Takes, as arguments, a Course class and a string of capital letters
# Letters in the string will have their streams removed from the Course
def remove_streams_from_course(course, streams):
    new = course
    for i in streams:
        if i.isupper():
            new.streams[ord(i) - ord("A")] = 0

# Function that takes a course name and removes streams from the course
# in the dictionary
def remove_streams_from_course_name(coursename, streams):
    course = returnDictionary()[coursename]
    remove_streams_from_course(course, streams)
