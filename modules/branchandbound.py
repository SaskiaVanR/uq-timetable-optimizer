import queue as Q
from classfile import *


#Depths
#Lectures = 0
#Tutorials = 1
#Practicals = 2
#Workshops = 3


class Node():
    def __init__(self, timetable, depth, adjDepth):
        self.timetable = timetable
        self.depth = depth
        self.adjDepth = adjDepth
        self.weight = timetable.getHWeight()



def getChildren(node):
    children = []
    if node.adjDepth == 0:
        for index, l in enumerate(node.timetable.Lassigned):
            if l==0:
                for stream in Courses[node.timetable.codes[index]].lectures:
                    t = node.timetable.makeCopy()
                    if t.canAdd(stream):
                        t.addStream(stream)
                        n = Node(t, node.depth+1, isDone(t))
                        children +=[n]

    if node.adjDepth == 1:
        for index, l in enumerate(node.timetable.Tassigned):
            if l==0:
                for stream in Courses[node.timetable.codes[index]].tutorials:
                    t = node.timetable.makeCopy()
                    if t.canAdd(stream):
                        t.addStream(stream)
                        n = Node(t, node.depth+1, isDone(t))
                        children +=[n]
    if node.adjDepth == 2:
        for index, l in enumerate(node.timetable.Passigned):
            if l==0:
                for stream in Courses[node.timetable.codes[index]].practicals:
                    t = node.timetable.makeCopy()
                    if t.canAdd(stream):
                        t.addStream(stream)
                        n = Node(t, node.depth+1, isDone(t))
                        children +=[n]
    if node.adjDepth == 3:
        for index, l in enumerate(node.timetable.Wassigned):
            if l==0:
                for stream in Courses[node.timetable.codes[index]].workshops:
                    t = node.timetable.makeCopy()
                    if t.canAdd(stream):
                        t.addStream(stream)
                        n = Node(t, node.depth+1, isDone(t))
                        children +=[n]
    return children            
    

def isDone(timetable):
    for i in timetable.Lassigned:
        if i ==0:
            return 0
    for i in timetable.Tassigned:
        if i ==0:
            return 1
    for i in timetable.Passigned:
        if i ==0:
            return 2
    for i in timetable.Wassigned:
        if i ==0:
            return 3
    return 4

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

infs1200 = Course("INFS1200", lectures, tutorials, practicals, workshops)


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

infs2200 = Course("INFS2200", lecturesm, tutorialsm, practicalsm, workshopsm)
Courses = {"INFS1200": infs1200, "INFS2200": infs2200}



q = Q.PriorityQueue()
q.put((10, 'ten'))
q.put((1, 'one'))
q.put((5, 'five'))
while not q.empty():
    print(q.get(),)

for a, b in enumerate([0,3,4]):
    print(a,b)


#q = Q.PriorityQueue()
q = []

emptyTimetable = Timetable(["INFS1200", "INFS2200"])
emptyNode = Node(emptyTimetable, 0, 0)
q.append(emptyNode)
best = False
bestVal = 1000

nodes = 0
while len(q)>0:
    current = q.pop()
    nodes +=1

    if current.adjDepth == 4:
        if current.timetable.getWeight()<bestVal:
            bestVal = current.timetable.getWeight()
            best = current
        continue
    children = getChildren(current)
    for c in children:
        q.append(c)



t = best.timetable

for s in t.streams:
    print (s.code +" + " + s.name)
    
    
