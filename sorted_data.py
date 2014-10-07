# Your job is to write a program named 'sorted_data.py' that
# reads the file, then spits out the ratings in 
# alphabetical order by restaurant.


def read_file_make_dict(filename):
    in_file = open(filename,"r")
    ratings = {}        # Creates an empty dictionary that will store restaurants with their scores

    for line in in_file:    # Read file line by line
        clean_line = line.strip()
        word_list = clean_line.split(":")  # Assign first column to name and second to score
        name = word_list[0].strip()
        score = word_list[1].strip()       
        ratings[name] = int(score)       # Create dictionary entry for each restaurant name
    
    return ratings

def print_ratings(d):
# Iterate through key, value in sorted dictionary and print

    def second_item(x):
        return x[1]

    ratings = sorted(d.items())       # Creates list of tuples (name,score) - > sorted alphabetically 
    sorted_ratings = sorted(ratings, key = second_item, reverse = True)     # Sorts list by highest score
    
    for item in sorted_ratings:
        print "Restaurant %s is rated at %s." % (item[0], item[1])

    # Version 2
    
    # result = []
    # rest_names = d.keys()
    # for restaurant in rest_names:
    #     result.append((d[restaurant], restaurant,))
    
    # result.sort()
    # for pair in result:
    #     print "Restaurant %s is rated at %d." % (pair[1],pair[0])


def main():
    rest_ratings = read_file_make_dict('scores.txt')
    print_ratings(rest_ratings)

if __name__ == "__main__":
    main()