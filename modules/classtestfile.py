from classfile import * 

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
print (infs1200.getWeight())


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


t = Timetable(["INFS1200", "INFS2200"])

t.addStreams(lectures)
t.addStreams(tutorials)
t.addStreams(practicals)
t.addStreams(lecturesm)
t.addStreams(tutorialsm)
t.addStreams(practicalsm)

print(t.getWeight())
