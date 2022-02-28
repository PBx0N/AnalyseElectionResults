import os
import csv
import operator

#set csv path and text file output path
csvpath = os.path.join("Resources", "election_data.csv")
outputpath = os.path.join("Election Analysis.txt")

#Set empty dictionary
CandidateData = {}

#Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip header row
    next(csvreader)

    for row in csvreader:

        if row[2] in CandidateData.keys():
            CandidateData[row[2]] = CandidateData[row[2]] + 1
        else:
            CandidateData[row[2]] = 1

    TotalVoteOfEach = CandidateData.values()
    TotalVotes = sum(TotalVoteOfEach)
    EachCandidate = CandidateData.keys()
    
    #Find Percentage votes for each candidate
    EachVotesPercentage = [f'{(x/TotalVotes)*100:.3f}%' for x in CandidateData.values()]

    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(TotalVotes))
    print("-----------------------")

#Print data out to text    
with open(outputpath, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(TotalVotes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")

    #Iterate through the dictonary and list to print the candidate names, corresponding percentage vote and the amount of vote
    #Print data out to text 
    i = 0 
    for candidates, totalvotes in CandidateData.items():
            print(f" {candidates}: {EachVotesPercentage[i]} ({totalvotes}) ")
            txt_file.write(f" {candidates}: {EachVotesPercentage[i]} ({totalvotes}) ")
            txt_file.write("\n")
            i = i + 1 

    print("-----------------------")
    txt_file.write("-------------------------")
    txt_file.write("\n")

    #Find the candidate who has to most votes
    winner = max(CandidateData.items(), key=operator.itemgetter(1))[0]
    print("Winner: " + winner)
    txt_file.write("Winner: " + str(winner))
    print("-----------------------")
    txt_file.write("\n")
    txt_file.write("-------------------------")



    