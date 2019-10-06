import os
import csv

csvpath = os.path.join("C:\\Users\\paula\\Desktop\\python_callenge\\PyPoll\\election_data.csv")
 
# Define Lists
votes = []
candidates = []     #List of candidates
candidate_vote = {} #Dictionary containing candidate votes

#Set variables
count = 0
winning_candidate = ""
winning_count = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    for row in csvreader:
        count = count + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_vote[row[2]]=1
        else:
            candidate_vote[row[2]]=candidate_vote[row[2]] +1

    for vote in candidate_vote:
        candidate = candidate_vote.get(vote)  
        candidate_percentage = float(candidate) / float(count) * 100 
            
        if candidate > winning_count:
            winning_count = candidate
            winning_candidate = vote

print("Election Results")
print("Total Votes: " + str(count))
print(f"{candidate_vote}")
print("Winner: " + (winning_candidate))
