import json 
import os
import sys
from classfile import Course
from classfile import Stream

# Function that gets info on a course
# It opens the file for it and parses info from the json
# It will eventually return the data as a Course class but for now it
# just prints stuff
def get_course_info(coursename):
    try:
        coursejson = json.loads(open("../scraper/data/" + coursename).read())
        # Initialise empty arrays
        lectures = [] # Array of streams
        tutorials = []
        practicals = []
        workshops = []
        for i in range(len(coursejson['courses'][0]['activity_streams'])):
            streamname = str(coursejson['courses'][0]['activity_streams']\
                    [i]['name'])
            #print(streamname) # For debugging, TODO remove
            # Initialise empty arrays
            times = [] # array for testing, string
            days = [] # array of ints for each day, 0 = monday
            starts = [] # array of ints for each start time, 15 = 3:00pm
            ends = [] # array of ints for each end time, 15 = 3:00pm
            for j in range(len(coursejson['courses'][0]['activity_streams']\
                    [i]['events'])):
                newdaystring = str(coursejson['courses'][0]['activity_streams']\
                        [i]['events'][j]['day'])
                from helpers import day_to_int
                newday = day_to_int(newdaystring)
                newstart = int(coursejson['courses'][0]['activity_streams'][i]\
                        ['events'][j]\
                        ['start'].split("T", 1)[1].split(":", 1)[0])
                newend = int(coursejson['courses'][0]['activity_streams'][i]\
                        ['events'][j]\
                        ['end'].split("T", 1)[1].split(":", 1)[0])
                newtime =  str(newday) + " " + str(newstart) + " " + str(newend)
                if newtime not in times:
                    times.append(newtime)
                    #print(times[len(times) - 1]) # For debugging, TODO remove
                    days.append(newday)
                    starts.append(newstart)
                    ends.append(newend)
                if j == len(coursejson['courses'][0]['activity_streams']\
                        [i]['events']) - 1:
                    # At the last point in the iteration
                    stream = Stream(coursename, streamname, starts, ends, days)
                    if streamname[0] == "L":
                        lectures.append(stream)
                    elif streamname[0] == "T":
                        tutorials.append(stream)
                    elif streamname[0] == "P":
                        practicals.append(stream)
                    elif streamname[0] == "W":
                        practicals.append(stream)
                    else:
                        sys.stderr.write("Error: " + streamname \
                                + " is not a lecture, tute, prac, or workshop")
                        return None
        course = Course(coursename, 
                lectures, tutorials, practicals, workshops)
        return course
    except: return None

# Function that tells you if a course exists
# It will check if it has been scraped
# and return true or false
def does_course_exist(coursename):
    if os.path.exists("../scraper/data/" + coursename):
        return True
    else:
        return False
