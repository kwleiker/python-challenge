# #     IMPORT DEPENDENCIES AND DATA FILE 
import os 
import csv 
file = 'PyPoll_data.csv' 

# #     DEFINE 
candidates = [] 
votes = [] 
votescast = 0 
with open(file, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",") 
    print(csvreader) 

    # #     PRINT HEADER ROW 
    csv_header = next(csvfile) 

# #     COUNT VOTES CAST 
    for row in csvreader: 
        votescast = votescast + 1 

        if candidates.count(row[2]) < 1: 
            candidates.append(row[2]) 

        votes.append(row[2]) 

# #     SCHLOCKY ATTEMPT AT SELF-DEPRECATING HUMOR TO GLOSS OVER 
# #     DESPITE DOING i THROUGH k MONKEY-TYPEWRITER ITERATIONS 
# #     i COULDN'T GET THIS TO DO WHAT I WANTED 
print(" --------------------------- ")
print("  .  ") 
print("Diebold Election Systems is pleased to announced the following election results: ")

# #     COUNT VOTES CAST 
print("  .  ") 
print("Total Votes Cast:  " + str(votescast)) 
print("  .  ") 
print(" --------------------------- ")


# #     PRINT VOTE TOTALS 
print("The c-th candidate got the r-th number and percent of the vote.")

for c in candidates: 
    print(str(candidates) + " received " + str(votes.count(c)) + " votes or " + str(round(((votes.count(c)/votescast)*100), 1)) + "% of the total votes cast.)")
print("  .  ") 
print(" --------------------------- ")
print("  .  ") 
print("The winner is: " + candidates[0])
print("  .  ") 
print(" --------------------------- ")

