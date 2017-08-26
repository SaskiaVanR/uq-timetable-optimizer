from classfile import * 

lectures = []
tutorials = []
practicals = []
workshops = []
lectures +=[Class("L01", [12, 13], [14, 14], "L", [3,4])]
tutorials +=[Class("T01", [15], [16], "T", [1])]
tutorials +=[Class("T02", [9], [10], "T", [4])]
tutorials +=[Class("T03", [10], [11], "T", [4])]
practicals +=[Class("P01", [9], [10], "T", [3])]
practicals +=[Class("P02", [10], [11], "T", [3])]

infs1200 = Course("INFS1200", lectures, tutorials, practicals, workshops)
print (infs1200.getWeight())
