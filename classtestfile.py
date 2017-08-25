lectures = []
tutorials = []
practicals = []
workshops = []
lectures +=[Class("L01", [12, 13], [14, 14], "L", [4,5])]
tutorials +=[Class("T01", [15], [16], "T", [2])]
tutorials +=[Class("T02", [9], [10], "T", [5])]
tutorials +=[Class("T03", [10], [11], "T", [5])]

infs1200 = Course("INFS1200", lectures, tutorials, practicals, workshops)
print (infs1200.getWeight())
