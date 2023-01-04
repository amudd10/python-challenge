# Dependencies
import os 
import csv
# lists, count
counter  = 0
candidate_li = []
diff_cand = []
vote_count = []
vote_perc = []

#open csv
csv_path = os.path.join("Resources", "election_data.csv")
with open(csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)

    for i in csv_reader:
        counter = counter + 1
        candidate_li.append(i[2])
    
    for x in set(candidate_li):
        diff_cand.append(x)
        total_votes = candidate_li.count(x)
        vote_count.append(total_votes)

        #percent of total votes
        total_perc = (total_votes/counter)*100
        vote_perc.append(total_perc)

    winner_count = max(vote_count)
    winner = diff_cand[vote_count.index(winner_count)]



# print(winner_count)

#Printing results
# print(f"""Election Results
# --------------------
# Total Votes: {total_votes}
# --------------------
# """)
# for j in range(len(diff_cand)):
#     print(diff_cand[j] + ": " + str(vote_perc[j]) + "% (" + str(vote_count[j]) + ")")

# print(f"""
# --------------------
# The winner is: {winner}
# --------------------""")

#Printing results to text file
with open('PyPoll_analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------\n")
    text.write(f'Total Vote: {total_votes}\n')
    text.write("--------------------\n")
    for j in range(len(diff_cand)):
        text.write(f"{diff_cand[j]} : {(vote_perc[j]):.3f}% Vote Count: {(vote_count[j])}\n")
    text.write("--------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("--------------------\n")

