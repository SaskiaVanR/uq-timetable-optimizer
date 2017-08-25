import sys
import requests
import getpass

# Function that gets the token cookie required for scraping the data
# It uses splinter, which uses a headless Firefox
# See https://splinter.readthedocs.io/ for more info
def get_token(username, password):
    from splinter import Browser
    import time
    browser = Browser()
    try:
        browser.visit("https://timetableplanner.app.uq.edu.au/")
        count = 0
        while browser.is_element_not_present_by_text("Sign in and get started!") and count < 10:
            time.sleep(1)
            count += 1
        if browser.is_element_present_by_text("Sign in and get started!"):
            browser.find_by_text("Sign in and get started!").click()
        else:
            return None
        count = 0
        while browser.is_element_not_present_by_id("username") and count < 10:
            time.sleep(1)
            count += 1
        if browser.is_element_present_by_id("username") and browser.is_element_present_by_id("password"):
            browser.fill('username', username)
            browser.fill('password', password)
        else:
            return None
        count = 0
        while browser.is_element_not_present_by_value("LOGIN") and count < 10:
            time.sleep(1)
            count += 1
        if browser.is_element_present_by_value("LOGIN"):
            browser.find_by_value("LOGIN").click()
        else:
            return None
        count = 0
        while "remember_token" not in browser.cookies and count < 10:
            time.sleep(1)
            count += 1
        if "remember_token" in browser.cookies:
            return browser.cookies['remember_token']
        else:
            return None
    finally:
        try: browser.quit() 
        except: print("Unable to close browser. Do it yourself!")

# Open the courses.txt text file and get an array of courses
try: courselistfile = open("courses.txt", "r")
except:
    sys.stderr.write("Please place a list of courses in courses.txt\n")
    sys.exit()
courselist = courselistfile.readlines()
for i in range(len(courselist)):
    # Strip trailing \n
    courselist[i] = str(courselist[i].rstrip())

# Open the headless browser and get the token
username = input("Enter your UQ username: ")
password = getpass.getpass()
token = get_token(username, password)
if token is None:
    sys.stderr.write("Unable to get token\n")
    sys.exit()
print("Token: " + token)

# Request timetables and save to file
for i in courselist:
    timetable = requests.get('https://timetableplanner.app.uq.edu.au/courses/search?semester_id=88&course_code=' + i, cookies={'remember_token': token})
    try: coursefile = open("data/" + i, "w+")
    except:
        sys.stderr.write("Unable to open file for writing")
        sys.exit()
    coursefile.write(timetable.text)
    print("Saved data for " + i)
