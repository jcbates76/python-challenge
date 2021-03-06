# Import functions
import os
import csv

# Declare variables
total_votes = 0
candidate_list = []
candidate_vote_total = []
candidate = str
candidate_winner = str
winner_total = 0

# Define the path of the CSV input file
csvpath = os.path.join("Resources", "election_data.csv")

# Define the path of the TXT output file
output_path = os.path.join("Analysis", "election_resuts.txt")

# Perform loop for all records within the CSV dataset
with open(csvpath, "r", encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row into a variable
    csv_header = next(csvreader) 

    # Iterate through all rows of the dataset
    for row in csvreader:
        
        # Accumulate total number of votes cast
        total_votes = total_votes + 1

        # Determine if candidate is accounted for in list of candidates
        # Pull the candidate name from the row of data
        candidate = row[2]

        # Check to see if the candidate is in the candidiate list, if not, add then add the candidat and append the vote total list at the same time
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote_total.append(0)
        
        # Increment the vote total for that candidate
        # Determine the candidate index 
        candidate_index = candidate_list.index(candidate)

        # Incremenet the candidate vote total for that candidate using the index for that candidate
        candidate_vote_total[candidate_index] = candidate_vote_total[candidate_index] + 1

# Determine the overall winner of the election looping through the candidates and comparing their totals
for candidate in candidate_list:
   if winner_total < candidate_vote_total[candidate_list.index(candidate)]:
        winning_candidate = candidate
        winner_total = candidate_vote_total[candidate_list.index(candidate)] 

# Print the output into the election_results.txt file
with open(output_path, "w", newline="") as f:
    f.write("Election Results\n")
    f.write("--------------------------------------------------------\n")
    f.write("Total Votes:  " + "{:,}\n".format(total_votes))
    f.write("--------------------------------------------------------\n")
    # Print the individual candidates and their sub-totals
    for candidate in candidate_list:
        f.write(candidate + ": " + str("{:.3%}".format(candidate_vote_total[candidate_list.index(candidate)]/total_votes)) + "   (" + str("{:,}".format(candidate_vote_total[candidate_list.index(candidate)])) + ")\n")
    f.write("--------------------------------------------------------\n")
    f.write("Winner:  " + winning_candidate + "\n")
    f.write("--------------------------------------------------------\n")

# Print the output of the election in the terminal
print("Election Results")
print("--------------------------------------------------------")
print("Total Votes:  " + "{:,}".format(total_votes))
print("--------------------------------------------------------")
# Print the individual candidates and their sub-totals
for candidate in candidate_list:
    print(candidate + ": " + str("{:.3%}".format(candidate_vote_total[candidate_list.index(candidate)]/total_votes)) + "   (" + str("{:,}".format(candidate_vote_total[candidate_list.index(candidate)])) + ")")
print("--------------------------------------------------------")
print("Winner:  " + winning_candidate)
print("--------------------------------------------------------")