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
        if len(self.lectures)!=0:
            time += self.lectures[0].timeTotal
        if len(self.tutorials)!=0:
            time += self.tutorials[0].timeTotal
        if len(self.practicals)!=0:
            time += self.practicals[0].timeTotal
        if len(self.workshops)!=0:
            time += self.workshops[0].timeTotal
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


class Timetable():
    def __init__(self, codes):
        self.codes = []
        self.classes = []

    def addClass(self, myClass):
        self.classes +=[myClass]

    def getWeight(self):
        starts = [24, 24, 24, 24, 24]
        ends = [0, 0, 0, 0, 0,]
        for c in self.classes:
            for index, day in c.days:
                if starts[day] > c.starts[index]:
                    starts[day] = c.starts[index]
                if ends[day] < c.ends[index]:
                    ends[day] = c.ends[index]
        weight = 0
        for i in range(5):
            starts[i] = starts[i]%24
            weight += ends[i] = starts[i]
        
                
           
