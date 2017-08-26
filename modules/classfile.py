

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
        

class Stream():
    def __init__(self, code, name, starts, ends, days):
        self.code = code
        self.name = name
        self.starts = starts
        self.ends = ends
        self.days = days
        self.timeTotal = self.getTimeTotal()


    # get the total number of hours required for this class per week
    def getTimeTotal(self):
        i = 0
        time = 0
        while i < len(self.starts):
            time +=self.ends[i]-self.starts[i]
            i+=1
        return time


class Timetable():
    def __init__(self, codes):
        self.codes = codes
        self.streams = []
        self.Lassigned = [0]*len(self.codes)
        self.Tassigned = [0]*len(self.codes)
        self.Passigned = [0]*len(self.codes)
        self.Wassigned = [0]*len(self.codes)

    def addStream(self, stream):
        if "L"== stream.name[0]:
            self.Lassigned[self.getCodeIndex(stream.code)] = 1
        elif "T" == stream.name[0]:
            self.Tassigned[self.getCodeIndex(stream.code)] = 1
        elif "P" == stream.name[0]:
            self.Passigned[self.getCodeIndex(stream.code)] = 1
        elif "W" == stream.name[0]:
            self.Wassigned[self.getCodeIndex(stream.code)] = 1
        self.streams +=[stream]

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
        

    def getWeight(self):
        starts = [24, 24, 24, 24, 24]
        ends = [0, 0, 0, 0, 0,]
        for c in self.streams:
            print(c.days)
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
                
           
