# #import csv
# import os
# import csv

# total_months = []

# filepath = os.path.join("resources","budget_data.csv")

# print(filepath)

# with open(filepath) as file:
    
#     csvFile = csv.reader(file)

#     header = next(csvFile)
#     print(header)
#     print("\n")

#     for row in csvFile:
#         print(row)
#         total_months.append(row[0])
#  # Track the total
#         total_months += 1
#         total_net += int(row[1])   
# # Track various financial parameters
# total_months = total_net = 0            

# # How many months:
import os
import csv
total_months = 0
total_net = 0
month_of_change = []
net_change_list = []
#REVIEW THIS
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

filepath = os.path.join("resources","budget_data.csv")
file_to_output = os.path.join("resources", "budget_analysis.txt")
print(filepath)
with open(filepath) as file:
    csvFile = csv.reader(file)
    header =next(csvFile)
    first_row=next(csvFile)
    total_months +=1 
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvFile:
        # Track the total months
        total_months +=1
        # Track the total net
        total_net += int(row[1])
       
        #Net Change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change+=[row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#total number of months
print(total_months)
#net total amount of "Profit/Losses"
print(total_net)
#Net Change
net_monthly_avg=(sum(net_change_list) / len(net_change_list)) #formula for net change

# greatest increase in profits (date and amount)
print(greatest_increase)
# greatest decrease in profits (date and amount)
print(greatest_decrease)

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)