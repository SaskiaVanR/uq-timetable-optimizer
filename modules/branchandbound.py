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


def getChildren(node, maxTime):
    children = []
    currentDepth = node.adjDepth
    if node.timetable.assigned[currentDepth][node.cindex]==0:
        for stream in \
            Courses[node.timetable.codes[node.cindex]].streams[currentDepth]:
            t = node.timetable.makeCopy()
            if t.canAdd(stream, maxTime):
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

def daysBranchAndBound(optCourses, maxTime):
    q = []
    get_dictionary(*optCourses)
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
        if nodes > 1000000:
            break
        if current.timetable.getHDays()>bestVal:
            
            cut+=1
        if current.adjDepth == 26:
            if current.timetable.getDays()<bestVal:
                bestVal = current.timetable.getDays()
                best = [current]
                mostRecent = nodes
                print("New best at " + str(bestVal))
            elif current.timetable.getDays()==bestVal:
                best += [current]
                mostRecent = nodes
            continue
        children = getChildren(current, maxTime)
        for c in children:
            q.append(c)
    return best
        

def mainBranchAndBound(optCourses, maxTime):
    q = []
    get_dictionary(*optCourses)
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
        if nodes > 1000000:
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
        children = getChildren(current, maxTime)
        for c in children:
            q.append(c)
    return best


def reduceDays(best):

    THEBEST = []
    BestDays = 10

    for b in best:
        days = [0, 0, 0, 0, 0, 0, 0]
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


def reduceWeight(best):

    THEBEST = []
    bestWeight = 100

    for b in best:
        w = b.timetable.getWeight()
        if w<bestWeight:
            bestWeight = w
            THEBEST = [b]
        elif w == bestWeight:
            THEBEST += [b]

    return THEBEST

def reduceEarlyMornings(best):
    THEBEST = []
    earliest = 0
    n = 100

    for b in best:
        e, num = b.timetable.getEarlyMornings()
        if e>earliest or (e==earliest and num<n):
            earliest = e
            THEBEST = [b]
            n = num
        elif e == earliest and num==n:
            THEBEST +=[b]

    return THEBEST
    

def optimize(courses, maxTime=24):
    print("--------- Weight, then Days ----------")
    b = mainBranchAndBound(courses, maxTime)
    print(len(b))
    better = reduceDays(b)
    print(len(better))
    
    best = reduceEarlyMornings(better)
    print(len(best))
    if len(best)!=0:
        t = best[0].timetable
        print("Weight: "+str(t.getWeight()) + " Days: " + str(t.getDays()))
        for s in t.streams:
            print (s.code +" + " + s.name)
    return best

def optimizeDays(courses, maxTime=24):
    print("--------- Days, then Weight ----------")
    b = daysBranchAndBound(courses, maxTime)
    print(len(b))
    
    better = reduceWeight(b)
    print(len(better))
    best = reduceEarlyMornings(better)
    print(len(best))
    if len(best)!=0:
        t = best[0].timetable
        print("Weight: "+str(t.getWeight()) + " Days: " + str(t.getDays()))
        for s in t.streams:
            print (s.code +" + " + s.name)
    return best

##lectures = []
##tutorials = []
##practicals = []
##workshops = []
##lectures +=[Stream("INFS1200", "L01", [12, 13], [14, 14],[3,4])]
##tutorials +=[Stream("INFS1200", "T01", [15], [16], [1])]
##tutorials +=[Stream("INFS1200", "T02", [9], [10], [4])]
##tutorials +=[Stream("INFS1200", "T03", [10], [11], [4])]
##practicals +=[Stream("INFS1200", "P01", [9], [10], [3])]
##practicals +=[Stream("INFS1200", "P02", [10], [11], [3])]
##
##
##infs1 = lectures+tutorials+practicals+workshops
##
##
##infs1200 = Course("INFS1200", infs1)
##
##
##lecturesm = []
##tutorialsm = []
##practicalsm = []
##workshopsm = []
##lecturesm +=[Stream("INFS2200", "L01", [12, 13], [14, 14], [1,2])]
##tutorialsm +=[Stream("INFS2200", "T01", [15], [16], [3])]
##tutorialsm +=[Stream("INFS2200", "T02", [9], [10], [4])]
##tutorialsm +=[Stream("INFS2200", "T03", [10], [11], [3])]
##practicalsm +=[Stream("INFS2200", "P01", [9], [10], [2])]
##practicalsm +=[Stream("INFS2200", "P02", [10], [11], [2])]
##
##infs2 = lecturesm+ tutorialsm+ practicalsm+workshopsm
##
##infs2200 = Course("INFS2200", infs2)




##q = Q.PriorityQueue()
##q.put((10, 'ten'))
##q.put((1, 'one'))
##q.put((5, 'five'))
##while not q.empty():
##    print(q.get(),)
##
##for a, b in enumerate([0,3,4]):
##    print(a,b)
##
##
####print("----TIME----")
####print("Fulltime: "+str(fulltime)+", Main: "+str(maintime)+\
####      ", Part: "+str(parttime))
####print("----BandB----")
####print("q: "+str(len(q))+" nodes: " + str(nodes) + " cuts " + str(cut))
##
#clist = ["INFS1200"]
#a = optimize(clist, 4)
#d = optimizeDays(clist)

