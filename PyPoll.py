# The Data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes. 
# 3. Total number of votes each candidate recieved. 
# 4. Precentage of votes each candidate won. 
# 5. The winner of the election based on popular vote.  

import csv 

file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
     print(election_data)

import os
dir(os)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")


# Add dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Creating new list for candidate options. 
candidate_options = []

#Declare candidate dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row.
    headers = next(file_reader)

     # Print each row in the CSV file.
    for row in file_reader:
            # Add to the total vote count.
        total_votes += 1
         # Print Candidate Names 
        candidate_name = row[2]

        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
         # Add name to list
            candidate_options.append(candidate_name)
        # Tracking vote count 
            candidate_votes[candidate_name] = 0
        # Add vote count
        candidate_votes[candidate_name] += 1
# Determine percentage of votes for each candidate. 
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)
print(total_votes)
print(candidate_options)
print(candidate_votes)