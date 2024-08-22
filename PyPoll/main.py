import os
import csv

election_data = os.path.join("Resources","election_data.csv")

print(election_data)

total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0
    
with open(election_data, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
    
        if candidate == "Charles Casper Stockham":
            stockham_votes +=1
        elif candidate == "Diana DeGette":
            degette_votes +=1
        elif candidate == "Raymon Anthony Doane":
            doane_votes +=1
    
candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

dict_candidates = dict(zip(candidate, votes))
winner = candidate[votes.index(max(votes))]

percentage_stockham = (stockham_votes / total_votes) * 100
percentage_degette = (degette_votes / total_votes) * 100
percentage_doane = (doane_votes / total_votes) * 100

print("Election Results:")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate[0]}: {percentage_stockham:.3f}% ({stockham_votes})\n")
print(f"{candidate[1]}: {percentage_degette:.3f}% ({degette_votes})\n")
print(f"{candidate[2]}: {percentage_doane:.3f}% ({doane_votes})\n")
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------")

output_file = os.path.join("Election_Results.txt")

with open(output_file, "w") as file:
    file.write("Election Results:\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"{candidate[0]}: {percentage_stockham:.3f}% ({stockham_votes})\n")
    file.write(f"{candidate[1]}: {percentage_degette:.3f}% ({degette_votes})\n")
    file.write(f"{candidate[2]}: {percentage_doane:.3f}% ({doane_votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")