import queue as Q
from classfile import *

class Node():
    def __init__(self, timetable, depth):
        self.timetable = timetable
        self.depth = depth
        self.weight = timetable.getHWeight()







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
q.append(emptyTimetable)

while len(q)>0:
    current = q.pop()
    
