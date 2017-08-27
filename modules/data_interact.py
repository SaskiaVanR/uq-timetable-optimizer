import json 
import os
import sys
from classfile import Course
from classfile import Stream

# Function that gets info on a course
# It opens the file for it and parses info from the json
# Return the data as a course class
def get_course_info(coursename):
    coursename = coursename.upper()
    try:
        coursejson = json.loads(open("../scraper/data/" \
                + coursename.upper()).read())
        # Initialise empty array
        streams = [] # Array of streams
        # Array showing how many streams there is for each type of class
        # This is to identify things like X01 in MATH1061 which only
        # happens once and probably isn't important
        streamoccurrences = [0] * 26
        #Iterate over the streams
        for i in range(len(coursejson['courses'][0]['activity_streams'])):
            # Get the name of the string (eg T01)
            streamname = str(coursejson['courses'][0]['activity_streams']\
                    [i]['name'])
            # Initialise empty arrays
            times = [] # array for testing, string
            days = [] # array of ints for each day, 0 = monday
            starts = [] # array of ints for each start time, 15 = 3:00pm
            ends = [] # array of ints for each end time, 15 = 3:00pm
            # Iterate over the events in the stream
            # (including repeats of weekly classes)
            for j in range(len(coursejson['courses'][0]['activity_streams']\
                    [i]['events'])):
                # Add to streamoccurrences
                streamoccurrences[ord(streamname[0]) - ord("A")] += 1
                newdaystring = str(coursejson['courses'][0]['activity_streams']\
                        [i]['events'][j]['day'])
                from helpers import day_to_int
                newday = day_to_int(newdaystring)
                if newday == None:
                    return None
                newstart = int(coursejson['courses'][0]['activity_streams'][i]\
                        ['events'][j]\
                        ['start'].split("T", 1)[1].split(":", 1)[0])
                newend = int(coursejson['courses'][0]['activity_streams'][i]\
                        ['events'][j]\
                        ['end'].split("T", 1)[1].split(":", 1)[0]) + 1
                newtime =  str(newday) + " " + str(newstart) + " " + str(newend)
                # Check if this has been seen before in an earlier week
                if newtime not in times:
                    times.append(newtime)
                    days.append(newday)
                    starts.append(newstart)
                    ends.append(newend)
                if j == len(coursejson['courses'][0]['activity_streams']\
                        [i]['events']) - 1:
                    # At the last point in the iteration
                    stream = Stream(coursename.upper(), \
                            streamname, starts, ends, days)
                    streams.append(stream)
        # Iterate over the letters and see what the counts are
        for i in range(26):
            if streamoccurrences[i] == 1:
                # There is something that only happens once
                # This probably shouldn't be counted
                for j in range(len(streams)):
                    if ord(streams[j].name[0]) - ord("A") == i:
                        del streams[j]
                        break
        course = Course(coursename,  streams)
        return course
    except: return None

# Function that tells you if all courses passed to it exist
# It will check if all courses given have been scraped
# and return true or false
def does_course_exist(*coursenames):
    for i in coursenames:
        if not os.path.exists("../scraper/data/" + i.upper()):
            return False
    return True
