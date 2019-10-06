import os
import csv

csvpath = os.path.join("C:\\Users\\paula\\Desktop\\python_callenge\\PyBank\\budget_data.csv")

# Define Lists
profit = []
months = []
monthly_change = []

#Set variables
count = 0
total_profit = 0
initial_profit = 0
total_change_profit = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    

    for row in csvreader:
        count = count + 1
        months.append(row[0])
        profit.append(row[1])
        total_profit = total_profit +int(row[1])
        monthly_change_profit = total_profit - initial_profit
        monthly_change.append(monthly_change_profit)
        

print("Total Months: " + str(count))
print("Total Profits: " + str(total_profit))


with open('PyBank_Analysis.txt', 'w') as text:
    text.write("---------------------------------------------------------+\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("---------------------------------------------------------+\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
 
