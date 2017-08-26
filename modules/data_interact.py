import json 
import os

# Function that gets info on a course
# It opens the file for it and parses info from the json
# It will eventually return the data as a Course class but for now it
# just prints stuff
def get_course_info(coursename):
    try: coursejson = json.loads(open("../scraper/data/" + coursename).read())
    except: return None
    for i in range(len(coursejson['courses'][0]['activity_streams'])):
        print(coursejson['courses'][0]['activity_streams'][i]['name'])
        # Initialise empty array
        times = []
        for j in range(len(coursejson['courses'][0]['activity_streams']\
                [i]['events'])):
            newtime = str(coursejson['courses'][0]['activity_streams'][i]\
                    ['events'][j]['day']) + ": " + \
                    str(coursejson['courses'][0]['activity_streams'][i]\
                    ['events'][j]['start'].split("T", 1)[1].split(":", 1)[0]) \
                    + " " \
                    + str(int(coursejson['courses'][0]['activity_streams'][i]\
                    ['events'][j]['end'].split("T", 1)[1].split(":", 1)[0]) + 1)
            if newtime not in times:
                times.append(newtime)
                print(times[len(times) - 1])
