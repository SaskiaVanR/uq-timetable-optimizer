import queue as Q
from classfile import *
import time


#Depths
#Lectures = 0
#A = 1
#B = 2
#C = 3
# etc


class Node():
    def __init__(self, timetable, depth, adjDepth, cindex):
        self.timetable = timetable
        self.depth = depth
        self.adjDepth = adjDepth
        self.weight = timetable.getHWeight()
        self.cindex=cindex


def getChildren(node):
    children = []
    currentDepth = node.adjDepth
    if node.timetable.assigned[currentDepth][node.cindex]==0:
        for stream in \
            Courses[node.timetable.codes[node.cindex]].streams[currentDepth]:
            t = node.timetable.makeCopy()
            if t.canAdd(stream):
                t.addStream(stream)
                adj = getAdjDepth(t)
                n = Node(t, node.depth+1, adj[0], adj[1])
                children +=[n]
    return children            
    

def getAdjDepth(timetable):
    #If there are missing lectures(index 11), depth is 0
    for i in range(26):
        for j, item in enumerate(timetable.assigned[i]):
            if item==0:
                return i,j
    return 26, 0

def printTimeTable(node):
    t = node.timetable
    for s in t.streams:
        print (s.code +" + " + s.name)
        

def mainBranchAndBound(optCourses):
    get_dictionary("COMP7308", "STAT1201", "COMP7500", "MATH1050", "MATH4202", \
               "INFS1200", "MATH1061", "MATH1052")
    Courses = returnDictionary()
    emptyTimetable = Timetable(optCourses)
    adj = getAdjDepth(emptyTimetable) 
    emptyNode = Node(emptyTimetable, 0, adj[0],adj[1])
    q.append(emptyNode)
    best = []
    bestVal = 1000
    mostRecent = 0
    nodes = 0
    cut = 0
    while len(q)>0:
        current = q.pop()
        nodes +=1
        
        
        if nodes%5000==0:
            print("q: "+str(len(q))+" nodes: " + str(nodes) + " cuts " + str(cut))
        if nodes-mostRecent >=50000:
            break
        if nodes > 100000:
            break
        if current.timetable.getHWeight()>bestVal:
            
            cut+=1
            continue
        if current.adjDepth == 26:
            if current.timetable.getWeight()<bestVal:
                bestVal = current.timetable.getWeight()
                best = [current]
                mostRecent = nodes
                print("New best at " + str(bestVal))
            elif current.timetable.getWeight()==bestVal:
                best += [current]
                mostRecent = nodes
            continue
        children = getChildren(current)
        for c in children:
            q.append(c)
    return best


def reduceDays(best):

    THEBEST = []
    BestDays = 10

    for b in best:
        days = [0, 0, 0, 0, 0]
        t = b.timetable
        for s in t.streams:
            for d in s.days:
                days[d]+=1
        total = 0
        for d in days:
            if d!=0:
                total+=1
        if total<BestDays:
            THEBEST = [b]
            BestDays = total
        elif total==BestDays:
            THEBEST+=[b]

    return THEBEST


def optimize(courses):
    b = mainBranchAndBound(courses)
    best = reduceDays(b)
    if len(best)!=0:
        t = best[0].timetable
        for s in t.streams:
            print (s.code +" + " + s.name)
    return best

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


infs1 = lectures+tutorials+practicals+workshops


infs1200 = Course("INFS1200", infs1)


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

infs2 = lecturesm+ tutorialsm+ practicalsm+workshopsm

infs2200 = Course("INFS2200", infs2)




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

optcourses = ["INFS1200", "MATH1061"]
get_dictionary("COMP7308", "STAT1201", "COMP7500", "MATH1050", "MATH4202", \
               "INFS1200", "MATH1061", "MATH1052")
Courses = returnDictionary()
##emptyTimetable = Timetable(optcourses)
##adj = getAdjDepth(emptyTimetable) 
##emptyNode = Node(emptyTimetable, 0, adj[0],adj[1])
##q.append(emptyNode)
##best = []
##bestVal = 1000
##mostRecent = 0
##nodes = 0
##cut = 0
##starttime = time.time()
##while len(q)>0:
##    current = q.pop()
##    nodes +=1
##    
##    
##    if nodes%5000==0:
##        print("q: "+str(len(q))+" nodes: " + str(nodes) + " cuts " + str(cut))
##    if nodes-mostRecent >=50000:
##        break
##    if nodes > 100000:
##        break
##    if current.timetable.getHWeight()>bestVal:
##        
##        cut+=1
##        continue
##    if current.adjDepth == 26:
##        if current.timetable.getWeight()<bestVal:
##            bestVal = current.timetable.getWeight()
##            best = [current]
##            mostRecent = nodes
##            print("New best at " + str(bestVal))
##        elif current.timetable.getWeight()==bestVal:
##            best += [current]
##            mostRecent = nodes
##        continue
##    children = getChildren(current)
##    for c in children:
##        q.append(c)
##
##maintime = time.time() - starttime
##
##THEBESTS = []
##BestDays = 10
##
##for b in best:
##    days = [0, 0, 0, 0, 0]
##    t = b.timetable
##    for s in t.streams:
##        for d in s.days:
##            days[d]+=1
##    total = 0
##    for d in days:
##        if d!=0:
##            total+=1
##    if total<BestDays:
##        THEBEST = [b]
##        BestDays = total
##    elif total==BestDays:
##        THEBEST+=[b]
##
##fulltime = time.time()-starttime
##
##parttime = fulltime - maintime
##
##b = mainBranchAndBound(optcourses)
##best = reduceDays(b)
##if len(best)!=0:
##    t = best[0].timetable
##    for s in t.streams:
##        print (s.code +" + " + s.name)

##print("----TIME----")
##print("Fulltime: "+str(fulltime)+", Main: "+str(maintime)+\
##      ", Part: "+str(parttime))
##print("----BandB----")
##print("q: "+str(len(q))+" nodes: " + str(nodes) + " cuts " + str(cut))
      

a = optimize(["INFS1200", "MATH1061"])
