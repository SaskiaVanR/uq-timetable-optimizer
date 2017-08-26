# Global variables
# Dictionary storing course names and associating them with course classes
Courses = {}
# alpha = ["A", "B", "C", "D", "E", "F", "G", "H" "I", "J" ,"K", "L", "M",\
         # "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Class that stores information on a course
# It contains the course code, and a bunch of streams
# course.streams is a 26 dimensional array, with one entry for each letter.
# of the alphabet. If there are lectures ("L"), they will be stored in a list
# at course.streams[ord("L") - ord("A")]. If there are not any streams with
# The corresponding letter, the value will be 0
class Course():
    def __init__(self, code, streams):
        #course code
        self.code = code
        #list of classes, with index 0 (A) corresponding to all A class types
        self.streams = [0]*26
        self.weight = self.getWeight()
        self.sortStreams(streams)

    #sorts the given list of streams into the correct index in self.streams
    def sortStreams(self, streams):
        for s in streams:
            if (self.streams[ord(s.name[0])-ord("A")])==0:
                self.streams[ord(s.name[0])-ord("A")] = []
            self.streams[ord(s.name[0])-ord("A")] += [s]

    # gets the total number of hours required for the course per week
    def getWeight(self):
        time = 0
        for i in self.streams:
            if i!=0:
                time += i[0].timeTotal
        return time

# Class that stores information on a stream.
# Streams at UQ are basically classes that you can enrol in
# Sometimes, you can enrol into a stream that gives you a certain list of
# different classes, so each stream can contain more than one class.
# The stream class contains the course code at stream.code, and the name
# of the stream at stream.name. It also includes three arrays of integers,
# days, starts, and ends. These integers contain information on class times
class Stream():
    def __init__(self, code, name, starts, ends, days):
        self.code = code
        self.name = name
        # Starts and ends are integers representing start and end times
        # They represent the hour in 24-hour time
        # Classes always start on the hour
        self.starts = starts
        self.ends = ends
        # days are integers representing the days classes are on
        # They are integers, with 0 representing Monday and 6, Sunday
        self.days = days
        #total number of hours for this stream
        self.timeTotal = self.getTimeTotal()

    # get the total number of hours required for this class per week
    def getTimeTotal(self):
        i = 0
        time = 0
        while i < len(self.starts):
            time +=self.ends[i]-self.starts[i]
            i+=1
        return time

# Class that stores information on a timetable.
# It contains a bunch of arrays
# Most important are timetable.codes (Course codes),
# timetable.streams (an array of streams representing the ones chosen)
class Timetable():
    def __init__(self, codes):
        self.codes = codes
        self.streams = []
        self.assigned = self.makeAssignArray()
        self.needToAssign()
        
    def makeAssignArray(self):
        numCodes = len(self.codes)
        array = [0]*26
        for i in range(26):
            array[i] = [0]*numCodes
        return array

    def addStream(self, stream):
        index = ord(stream.name[0]) - ord("A")
        codeIndex = self.getCodeIndex(stream.code)
        self.assigned[index][codeIndex] = 1
        self.streams +=[stream]

    # Assigns -1 to the letters that do not need to be assigned for each course
    # Stays 0 when it needs to be assigned
    # Becomes 1 when assigned
    def needToAssign(self):
        for index, code in enumerate(self.codes):
            c = Courses[code]
            for i in range(26):
                if c.streams[i]==0:
                    self.assigned[i][index] = -1

    def makeCopy(self):
        t = Timetable(self.codes)
        for s in self.streams:
            t.addStream(s)
        return t

    def addStreams(self, streams):
        for i in streams:
            self.addStream(i)

    def getCodeIndex(self, code):
        i = 0
        while i< len(self.codes):
            if self.codes[i] == code:
                return i
            i+=1
        print("not a valid course code: " + code + " in " + str(self.codes))
        return False

    def canAdd(self, stream):
        hours = self.getHours()
        for i in range(len(stream.starts)):
            for hour in range(stream.starts[i],stream.ends[i]):
                if hour in hours[stream.days[i]]:
                    return False
        return True
        

    def getHours(self):
        hours = [[],[],[],[],[]]
        for s in self.streams:
            for i in range(len(s.starts)):
                for time in range(s.starts[i],s.ends[i]):
                    hours[s.days[i]]+=[time]
        return hours

    def getWeight(self):
        starts = [24, 24, 24, 24, 24]
        ends = [0, 0, 0, 0, 0,]
        for c in self.streams:
            for index, day in enumerate(c.days):
                if starts[day] > c.starts[index]:
                    starts[day] = c.starts[index]
                if ends[day] < c.ends[index]:
                    ends[day] = c.ends[index]
        weight = 0
        for i in range(5):
            starts[i] = starts[i]%24
            weight += ends[i] - starts[i]
        return weight

    def getHWeight(self):
        starts = [24, 24, 24, 24, 24]
        ends = [0, 0, 0, 0, 0,]
        for c in self.streams:
            for index, day in enumerate(c.days):
                if starts[day] > c.starts[index]:
                    starts[day] = c.starts[index]
                if ends[day] < c.ends[index]:
                    ends[day] = c.ends[index]
        weight = 0
        for i in range(5):
            starts[i] = starts[i]%24
            weight += ends[i] - starts[i]

        #lectures
        for c in self.codes:
            course = Courses[c]
            for letter in range(26):
                if course.streams[letter]!=0:
                    for i in course.streams[letter]:
                        if self.isWithinTime(i):
                            break
                    else:
                        weight += course.streams[letter][0].timeTotal              
        return weight
                
    def isWithinTime(self, stream):
        starts = [24, 24, 24, 24, 24]
        ends = [0, 0, 0, 0, 0,]
        for c in self.streams:
            for index, day in enumerate(c.days):
                if starts[day] > c.starts[index]:
                    starts[day] = c.starts[index]
                if ends[day] < c.ends[index]:
                    ends[day] = c.ends[index]
        for i in range(5):
            starts[i] = starts[i]%24

        for i in range(len(stream.starts)):
            if not(stream.starts[i]>=starts[stream.days[i]] and\
                stream.ends[i]<=ends[stream.days[i]]):
                return False
        else:
            return True


# def getTestTimetable():
    # lectures = []
    # tutorials = []
    # practicals = []
    # lectures +=[Stream("INFS1200", "L01", [12, 13], [14, 14],[3,4])]
    # tutorials +=[Stream("INFS1200", "T01", [15], [16], [1])]
    # practicals +=[Stream("INFS1200", "P01", [9], [10], [3])]
    # infs1 = lectures + tutorials + practicals
    # infs1200 = Course("INFS1200", infs1)
    # #print (infs1200.getWeight())
    # lecturesm = []
    # tutorialsm = []
    # practicalsm = []
    # lecturesm +=[Stream("INFS2200", "L01", [12, 13], [14, 14], [1,2])]
    # tutorialsm +=[Stream("INFS2200", "T03", [10], [11], [3])]
    # practicalsm +=[Stream("INFS2200", "P02", [10], [11], [2])]
    # infs2 = lecturesm + tutorialsm + practicalsm
    # infs2200 = Course("INFS2200", infs2)
    # Courses = {"INFS1200": infs1200, "INFS2200": infs2200}
    # t = Timetable(["INFS1200", "INFS2200"])
    # streams = infs1 + infs2
    # t.addStreams(streams)
    # return t

# Function that takes a list of courses and gets a dictionary from it
def get_dictionary(*coursecodes):
    courses = []
    for i in coursecodes:
        from data_interact import get_course_info
        course = get_course_info(i)
        courses.append(course)
        print (course, i)
        Courses[i] = course

def returnDictionary():
    return Courses

# Gets a test timetable
def get_test_timetable():
    get_dictionary("INFS1200")
    timetable = Timetable(["INFS1200"])
    streams = [Courses['INFS1200'].streams[ord("L") - ord("A")][0], \
            Courses["INFS1200"].streams[ord("T") - ord("A")][0], \
            Courses["INFS1200"].streams[ord("P") - ord("A")][0]]
    timetable.addStreams(streams)
    return timetable

lectures = []
tutorials = []
practicals = []
workshops = []
lectures +=[Stream("INFS1200", "L01", [12, 13], [14, 14],[3,4])]
tutorials +=[Stream("INFS1200", "T01", [15], [16], [1])]
tutorials +=[Stream("INFS1200", "T02", [9], [10], [4])]
tutorials +=[Stream("INFS1200", "T03", [10], [11], [4])]
practicals +=[Stream("INFS1200", "P01", [9], [10], [3])]
practicals +=[Stream("INFS1200", "P02", [10], [11], [3])]

infs1 = lectures + tutorials + practicals + workshops

infs1200 = Course("INFS1200", infs1)
#print (infs1200.getWeight())


lecturesm = []
tutorialsm = []
practicalsm = []
workshopsm = []
lecturesm +=[Stream("INFS2200", "L01", [12, 13], [14, 14], [1,2])]
tutorialsm +=[Stream("INFS2200", "T01", [15], [16], [3])]
tutorialsm +=[Stream("INFS2200", "T02", [9], [10], [4])]
tutorialsm +=[Stream("INFS2200", "T03", [10], [11], [3])]
practicalsm +=[Stream("INFS2200", "P01", [9], [10], [2])]
practicalsm +=[Stream("INFS2200", "P02", [10], [11], [2])]

infs2 = lecturesm + tutorialsm + practicalsm + workshopsm

infs2200 = Course("INFS2200", infs2)
Courses = {"INFS1200": infs1200, "INFS2200": infs2200}
##
##t = Timetable(["INFS1200", "INFS2200"])
##
###print(t.getWeight())
##t.addStreams(lectures)
##t.addStreams(tutorials)
##t.addStreams(practicals)
##
###print(t.getWeight())
##
##sss = []
##sss += tutorials
##sss += practicals
##sss += lectures
##infs1200.sortStreams(sss)
