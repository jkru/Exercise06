# Your job is to write a program named 'sorted_data.py' that
# reads the file, then spits out the ratings in 
# alphabetical order by restaurant.

in_file = open("scores.txt","r")

ratings = {}

for line in in_file:
    data = line.rstrip().split(":")
    name, score = data
    ratings[name] = score

sorted_names = sorted(ratings)

for name in sorted_names:
     print "Restaurant %s is rated at %s." % (name, ratings[name]) 
