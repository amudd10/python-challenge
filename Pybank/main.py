#Importing csv budget file
import csv

#Variable for file path
csv_path = 'resources/budget_data.csv'

#Reading file
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        print(row[0])

#Variable,list declaration
months = []
profit = []
total_months = 0
net_amount_change = []

#Looping through data, filling lists
for row in csv_reader:
    months = row[0]
    months.append(months)
    profloss = int(row[1])
    profit.append(profloss)

#Total months
total_months = len(months)
net_total_months = len(months) - 1

#Difference
profloss_change = []

for i in range(len(profloss) -1):
    profloss_change.append(int(profloss[i + 1]) - int(profloss[i]))
    new_total = sum(profloss_change)

#Sum of profloss
net_avg_change = new_total / net_total_months

#greatest increase & greatest decrease 
max_profit = profit[profit.index(max(profit))] - profit[profit.index(max(profit))-1]
min_profit = profit[profit.index(min(profit))] - profit[profit.index(min(profit))-1]


#Printing results
print(f"""Financial Analysis
--------------------
Total Months: {total_months}
Total: ${net_total_months}
Average Change: ${round(net_avg_change,2)}
Greatest Increase in Profits: {months[profit.index(max(profit))]} (${max_profit})
Greatest Decrease in Profits: {months[profit.index(min(profit))]} (${min_profit})""")

# define the file name
file_name = "financial_analysis.txt"

# open the file in write mode
with open(file_name, 'w') as file:
    # write the results to the file
    file.write(f"Financial Analysis\n")
    file.write("--------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total_months}\n")
    file.write(f"Average Change: ${round(net_avg_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {months[profit.index(max(profit))]} (${max_profit})\n")
    file.write(f"Greatest Decrease in Profits: {months[profit.index(min(profit))]} (${min_profit})\n")
