import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

print(budget_data)
    
with open(budget_data, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    Profit = []
    Months = []

    for row in csvreader:
        Profit.append(int(row[1]))
        Months.append(row[0])

        revenue_change = []

    for x in range(len(Profit) - 1):
        revenue_change.append(Profit[x+1] - Profit[x])
        revenue_change_average = sum(revenue_change) / len(revenue_change)
        total_months = len(Months)

        greatest_increase = max(revenue_change)
        greatest_decrease = min(revenue_change)

print("Financial Analysis:")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: ${revenue_change_average:.2f}")
print(f"Greatest Increase in Profits: {Months[revenue_change.index(greatest_increase)]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {Months[revenue_change.index(greatest_decrease)]} (${greatest_decrease})")

output_file = os.path.join("Financial_Analysis.txt")

with open(output_file, "w") as file:
    file.write("Financial Analysis:\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${sum(Profit)}\n")
    file.write(f"Average Change: ${revenue_change_average:.2f}\n")
    file.write(f"Greatest Increase in Profits: {Months[revenue_change.index(greatest_increase)]} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {Months[revenue_change.index(greatest_decrease)]} (${greatest_decrease})\n")