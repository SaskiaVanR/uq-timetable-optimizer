import queue as Q
from classfile import *


#Depths
#Lectures = 0
#A = 1
#B = 2
#C = 3
# etc


class Node():
    def __init__(self, timetable, depth, adjDepth):
        self.timetable = timetable
        self.depth = depth
        self.adjDepth = adjDepth
        self.weight = timetable.getHWeight()


def getChildren(node):
    children = []
    currentDepth = node.adjDepth
    for courseIndex in range(len(node.timetable.codes)):
        if node.timetable.assigned[currentDepth][courseIndex]==0:
            for stream in or stream in \
                Courses[node.timetable.codes[index]].streams[currentDepth]:
                t = node.timetable.makeCopy()
                if t.canAdd(stream):
                    t.addStream(stream)
                    n = Node(t, node.depth+1, getAdjDepth(timetable))
                    children +=[n]



##    if node.adjDepth == 3:
##        for index, l in enumerate(node.timetable.Wassigned):
##            if l==0:
##                for stream in Courses[node.timetable.codes[index]].workshops:
##                    t = node.timetable.makeCopy()
##                    if t.canAdd(stream):
##                        t.addStream(stream)
##                        n = Node(t, node.depth+1, isDone(t))
##                        children +=[n]
    return children            
    

def getAdjDepth(timetable):
    #If there are missing lectures(index 11), depth is 0
    if timetable.assigned[11] !=0 and timetable.assigned:
        continue



    
    for i in range(26):
        
        

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
    
    
