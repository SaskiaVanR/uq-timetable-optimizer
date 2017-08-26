import queue as Q

q = Q.PriorityQueue()
q.put((10, 'ten'))
q.put((1, 'one'))
q.put((5, 'five'))
while not q.empty():
    print(q.get(),)

for a, b in enumerate([0,3,4]):
    print(a,b)
