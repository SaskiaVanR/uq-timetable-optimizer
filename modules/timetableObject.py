from classfile import *

lectures = []
tutorials = []
practicals = []
lectures +=[Stream("INFS1200", "L01", [12, 13], [14, 14],[3,4])]
tutorials +=[Stream("INFS1200", "T01", [15], [16], [1])]

practicals +=[Stream("INFS1200", "P01", [9], [10], [3])]


infs1 = lectures + tutorials + practicals + workshops

infs1200 = Course("INFS1200", infs1)
#print (infs1200.getWeight())


lecturesm = []
tutorialsm = []
practicalsm = []
lecturesm +=[Stream("INFS2200", "L01", [12, 13], [14, 14], [1,2])]
tutorialsm +=[Stream("INFS2200", "T03", [10], [11], [3])]
practicalsm +=[Stream("INFS2200", "P02", [10], [11], [2])]

infs2 = lecturesm + tutorialsm + practicalsm + workshopsm

infs2200 = Course("INFS2200", infs2)
Courses = {"INFS1200": infs1200, "INFS2200": infs2200}

t = Timetable(["INFS1200", "INFS2200"])
streams = infs1 + infs2
t.addStreams(streams)
