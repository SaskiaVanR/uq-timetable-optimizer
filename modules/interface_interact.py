import sys
import os

from classfile import Course
from classfile import Stream
from classfile import Timetable
from data_interact import *

# Function that takes a list of courses and gets a dictionary from it
def get_dictionary(*coursecodes):
    courses = []
    Courses = {}
    for i in courses:
        course = get_course_info(i)
        courses.append(course)
        Courses[coursename] = course
    return Courses
