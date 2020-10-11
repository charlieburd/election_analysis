'''
#Pseudocode -- Data retrieval steps.
#1. The total number of votes cast
#2. A complete list of canidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candiadate won
#5. The winner of the election based on populare vote


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.
print(election_data)
# Close the file.
election_data.close()


#open the election results and read the file.
with open(file_to_load) as election_data:
#To do: perform analysis
    print(election_data)



import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)    

import csv
import os

#3.4.3
#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
#using the open() function with the 'w' mode we will write data to the file
outfile = open(file_to_save,'w')
#write some data to the file.
outfile.write("Hello World")
#close the file
outfile.close()


import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the with statement open the file as a text file
with open (file_to_save, 'w') as txt_file:
    txt_file.write("Counties in the election\n-------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson ")


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #print each row in the CSV file.
    for row in file_reader:
        print(row)

'''

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0
#candidate options and candidate votes
candidate_options = []
candidate_votes = {}
#trancking the winning candidate, vote count, and percentgage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #read and analyze the data here.
    file_reader = csv.reader(election_data)
    #read the header row in the CSV file.
    headers = next(file_reader)
    #pring each row in the csv file
    for row in file_reader:
        #add to the total vote count.
        total_votes += 1
        #get the candidate name from each row
        candidate_name = row[2]
        #if the candidate does not match and existing candidate addit to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #add begin tracking that candidates voter count.
            candidate_votes[candidate_name] = 0
        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1

#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count and candidate results to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #save the final vote count to text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        #retrieve vote count and percantage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        #print each candidate, their voter count, and percentage to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidates, their voter count, and percentage to the terminal
        print(candidate_results)
        #save the final candidate results to the text file
        txt_file.write(candidate_results)

        #determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    #print the winning candidates results to the terminal
    winning_candidate_summary = (
        f" ------------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    #save the winning candidates results to the text file
    txt_file.write(winning_candidate_summary)

'''
with open(file_to_load) as election_data:
    #read and analyze the data here.
    file_reader = csv.reader(election_data)
    #read the header row in the CSV file.
    headers = next(file_reader)
    #pring each row in the csv file
    for row in file_reader:
        #add to the total vote count.
        total_votes += 1
        #get the candidate name from each row
        candidate_name = row[2]
        #if the candidate does not match and existing candidate addit to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #add begin tracking that candidates voter count.
            candidate_votes[candidate_name] = 0
    #add a vote to that candidates count
    candidate_votes[candidate_name] += 1
'''