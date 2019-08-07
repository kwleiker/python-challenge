import os
import csv

#   GET DATA FILE 
file = 'PyPoll_data.csv'
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    print(csvreader)

#   PRINT HEADER ROW
    csv_header = next(csvfile)
    print ("  .  ")
    print(f"Header: {csv_header}")

#   PRINT FIRST 20 ROWS 
    print ("  .  ")
    head = [next(csvfile) for x in range(20)]
    print(head)

#   COUNT VOTES CAST
    votescast = 0
    for row in csvreader:
        votescast = votescast + 1 
    print ("  .  ")
    print ("Total Votes Cast:  " + str(votescast))
    print ("  .  ")






    #   NOTHING BELOW HERE HAS WORKED WORK, JUST PLAYING WITH DIFFERENT IDEAS
    #   KEEP IN MIND, THIS IS NOT ANYWHERE NEAR A COMPLETE LIST.
    #   A colleague once said to me, "There is a right way and a wrong way to do things." 
    #   I corrected him.  "There is more than one wrong way to do thngs."
    #   "And there isn't always a right way."


    ## counter
    # count = csvfile.count("Khan")
    # print("Khan got " + str(count) + " votes")




# Tally occurrences of words in a list
cnt = Counter()
for Khan in [PyPoll_data.csv]:
    cnt["Khan"] += 1
cnt





import re
words = re.findall(r'\w+', open('Pypoll_data.csv').read().lower())
Counter(words).most_common(10)


    #   COUNT VOTES CAST KHAN

    Khanvotes = 0
    for row in csvreader:
        if row['2'] is "Khan":
            Khanvotes = Khanvotes + 1

    print ("  .  ")
    print ("Khan Votes Cast:  " + str(Khanvotes))
    print ("  .  ")





    # import csv 
    # count = sum(1 for row in (open(file)) if row['2'] == ['Khan'])
    # print(count)






    import csv
    my_reader = csv.reader(open('PyPoll_data.csv'))
    ctr = 0
    for record in my_reader:
        if record[2] == 'Khan':
            ctr += 1
    print(ctr)