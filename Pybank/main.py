#Importing csv budget file
import os
import csv
import statistics
#Variable for file path
csv_path = 'resources/budget_data.csv'
#Reading file
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    

    #Variable,list declaration
    months = 0
    total = 0
    profit = []
    greatest_increase = 0
    greatest_decrease = 0
    best_month = ""
    worst_month = ""
    
    #Looping through data
    for row in csv_reader:
        months += 1
        total += int(row[1])
        profloss = int(row[1])
        profit.append(profloss)
        
        if int(row[1]) > greatest_increase:
            best_month = row[0]
            greatest_increase = int(row[1])
        
        elif int(row[1]) < greatest_decrease:
            worst_month = row[0]
            greatest_decrease = int(row[1])


    #Difference
    profloss_change = []

    for i in range(len(profit) -1):
        monthly_change = (int(profit[i + 1]) - int(profit[i]))
        profloss_change.append(monthly_change)

    #Sum of profloss
    net_avg_change = statistics.mean(profloss_change)




    # #Printing results
    # print(f"""
    # Financial Analysis
    # --------------------
    # Total Months: {months}
    # Total: ${total}
    # Average Change: ${round(net_avg_change,2)}
    # Greatest Increase in Profits: {best_month} (${greatest_increase})
    # Greatest Decrease in Profits: {worst_month} (${greatest_decrease})""")

f = open("Pybank_analysis.txt", "w")
f.write(f"""
Financial Analysis
--------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(net_avg_change,2)}
Greatest Increase in Profits: {best_month} (${greatest_increase})
Greatest Decrease in Profits: {worst_month} (${greatest_decrease})""")