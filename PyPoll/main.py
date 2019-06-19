import os
import csv

#Path to collect data from the Resources folder
Election_csv = os.path.join ("Election_data.csv")
    
#Creates dictionary to be used for candidate name and vote count.
election = {}    
    
#Set iniital variables and blank lists    
total_votes = 0

# Read through CSV
with open(Election_csv, newline="") as csvfile:
    
    #Split the data on commmas
    csvreader = csv.reader(csvfile, delimiter=",")
   
    #Strip the header
    next(csvreader)
     
    #Keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1

#Create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#Candidates and num_votes
for key, value in election.items():
    candidates.append(key)
    num_votes.append(value)

#Create vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 3))
    
# Zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#Creates winner_list to put winners
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# Makes winner_list a str with the first entry
winner = winner_list[0]

# Output of election results
print(f'Election Results \n---------------------------- \nTotal Votes: ' +str(total_votes) + '\n----------------------------')
for item in clean_data:
    print(item[0] + f': '+str(item[2]) + '% (' +str(item[1]) + ')')
print(f'---------------------------- \nWinner: ' + winner +'\n----------------------------')

#Print results to text file

with open("PyPoll.txt", 'w') as txtfile:
    txtfile.writelines(f'Election Results \n---------------------------- \nTotal Votes: ' +str(total_votes) + '\n----------------------------\n')
    for item in clean_data:
        txtfile.writelines(item[0] + f': '+str(item[2]) + '% (' +str(item[1]) + ')\n')
    txtfile.writelines(f'---------------------------- \nWinner: ' + winner +'\n----------------------------')

