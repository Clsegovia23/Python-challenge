import os
import csv

# set path for file

csvpath = os.path.join("Resources", "election_data.csv")

# set variables
count = 0
candidates = []
vote_count = []
vote_perc = []
unique_candidates = []
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
vote_tally = [khan_vote, correy_vote, li_vote, otooley_vote]

# setup to read data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(csvreader)

    for row in csvreader:
        #The total number of votes cast
        count += 1
    # print(count)

        #A complete list of candidates who received votes
        candidates.append(row[2])
    # print(unique_candidates)

    #start elseif     
    for name in candidates:
        if name not in unique_candidates:
            unique_candidates.append(name)
        
        if name == "Khan":
            khan_vote += 1
        elif name == "Correy":
            correy_vote += 1
        elif name == "Li":
            li_vote += 1
        else:
            otooley_vote += 1

# The total number of votes each candidate won
# print(khan_vote)
# print(correy_vote)
# print(li_vote)
# print(otooley_vote)

# The percentage of votes each candidate won
# The winner of the election based on popular vote. 

winning_vote_count = max(vote_tally)
winner = unique_candidates[vote_tally.index(winning_vote_count)]
# print(winner)


# Write in terminal
print("------------------------------------")
print("Election Results")
print("------------------------------------")
print(f'Total Votes: {count}')
print("------------------------------------")
print(f'Khan: {round((khan_vote/count)*100,2)}% ({khan_vote})')
print(f'Correy: {round((correy_vote/count)*100,2)}% ({correy_vote})')
print(f'Li: {round((li_vote/count)*100,2)}% ({li_vote})')
print(f'OTooley: {round((otooley_vote/count)*100,2)}% ({otooley_vote})')
print("--------------------------------------")
print(f'Winner: {winner}')
print("--------------------------------------")


#Print in text file
# with open("analysis/Election Results", "w") as text:
#     text.write("------------------------------------\n")
#     text.write(f"Election Results\n")
#     text.write("------------------------------------\n")
#     text.write(f"Total Votes: " + str(count) + "\n")
#     text.write("------------------------------------\n")
#     text.write(f"Khan: " + str(round((khan_vote/count)*100,2)) + "% " + "(" + str((khan_vote)) + ")" + "\n")
#     text.write(f"Correy: " + str(round((correy_vote/count)*100,2)) + "% " + "(" + str((correy_vote)) + ")" + "\n")
#     text.write(f"Li: " + str(round((li_vote/count)*100,2)) + "% " + "(" + str((li_vote)) + ")" + "\n")
#     text.write(f"O'Tooley: " + str(round((otooley_vote/count)*100,2)) + "% " + "(" + str((otooley_vote)) + ")" + "\n")
#     text.write("------------------------------------\n")
#     text.write(f"Winner: " + str(winner) + "\n")
#     text.write("------------------------------------\n")


# print("------------------------------------")
# print("Election Results")
# print("------------------------------------")
# print(f'Total Votes: {count}')
# print("------------------------------------")
# print(f'Khan: {round((khan_vote/count)*100,2)}% ({khan_vote})')
# print(f'Correy: {round((correy_vote/count)*100,2)}% ({correy_vote})')
# print(f'Li: {round((li_vote/count)*100,2)}% ({li_vote})')
# print(f'OTooley: {round((otooley_vote/count)*100,2)}% ({otooley_vote})')
# print("--------------------------------------")
# print(f'Winner: {winner}')
# print("--------------------------------------")