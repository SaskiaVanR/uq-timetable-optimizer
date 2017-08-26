import json 
import os
import sys
from classfile import Course
from classfile import Stream

# Function that gets info on a course
# It opens the file for it and parses info from the json
# Return the data as a course class
def get_course_info(coursename):
    try:
        coursejson = json.loads(open("../scraper/data/" + coursename).read())
        # Initialise empty array
        streams = [] # Array of streams
        for i in range(len(coursejson['courses'][0]['activity_streams'])):
            streamname = str(coursejson['courses'][0]['activity_streams']\
                    [i]['name'])
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
                        ['end'].split("T", 1)[1].split(":", 1)[0]) + 1
                newtime =  str(newday) + " " + str(newstart) + " " + str(newend)
                if newtime not in times:
                    times.append(newtime)
                    days.append(newday)
                    starts.append(newstart)
                    ends.append(newend)
                if j == len(coursejson['courses'][0]['activity_streams']\
                        [i]['events']) - 1:
                    # At the last point in the iteration
                    stream = Stream(coursename, streamname, starts, ends, days)
                    streams.append(stream)
        course = Course(coursename,  streams)
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
