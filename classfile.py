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
    def __init__(self, name, starts, ends, ctype, days):
        self.name = name
        self.starts = starts
        self.ends = ends
        self.ctype = ctype
        self.day = days
        self.timeTotal = self.getTimeTotal()


    # get the total number of hourse required for this class per week
    def getTimeTotal(self):
        i = 0
        time = 0
        while i < len(self.starts):
            time +=self.ends[i]-self.starts[i]
            i+=1
        return time


lectures = []
tutorials = []
practicals = []
workshops = []
lectures +=[Class("L01", [12, 13], [14, 14], "L", [4,5])]
tutorials +=[Class("T01", [15], [16], "T", [2])]
tutorials +=[Class("T02", [9], [10], "T", [5])]
tutorials +=[Class("T03", [10], [11], "T", [5])]

infs1200 = Course("INFS1200", lectures, tutorials, practicals, workshops)
print (infs1200.getWeight())           
           
