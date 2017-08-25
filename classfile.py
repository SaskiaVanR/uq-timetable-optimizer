class Course():
    def __init__(self, code, lectures, tutorials, practicals, workshops):
        self.code = code
        self.lectures = lectures
        self.tutorials = tutorials
        self.practicals = practicals
        self.workshops = workshops
        self.weight = self.getWeight()

    # gets the total number of hours required for the course per week
    def getWeight(self):
        time = 0
        if len(lectures)!=0:
            time += lectures[0].timeTotal
        if len(tutorials)!=0:
            time += tutorials[0].timeTotal
        if len(practicals)!=0:
            time += practicals[0].timeTotal
        if len(workshops)!=0:
            time += workshops[0].timeTotal
        return time
        

class Class():
    def __init__(self, name, starts, ends, ctype, day):
        self.name = name
        self.starts = starts
        self.ends = ends
        self.ctype = ctype
        self.day = day
        self.timeTotal = this.getTimeTotal()


    # get the total number of hourse required for this class per week
    def getTimeTotal(self):
        i = 0
        time = 0
        while i < len(starts):
            time +=ends[0]-starts[0]
        return time
