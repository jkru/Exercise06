
filename = open("scores.txt")
restrating = {}

for line in filename:
    line = line.rstrip().split(":")
    restrating[line[0]] = line[1]

sorted_list = sorted(restrating)

for rest in sorted_list:
    print "the restaurant %s got a rating of %s " % (rest, restrating[rest])
