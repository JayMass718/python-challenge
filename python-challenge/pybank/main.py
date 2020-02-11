import os
import csv

# Paths to collect data and push data
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
text = os.path.join('..', 'Resources', 'budget_analysis.txt')

# Define various financial dicts/trackers
total_months = 0
total_net = 0
net_change_dict = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999]



# Reading CSV and then creating the dictionary
with open(budget_csv) as budget_data
   reader = csv.reader(budget_data)
   
# Skip first row
   header = next(reader)
   first_row = next(reader)
   total_net = total_net + int(first_row[1])
   prev_net = int(first_row[1])
   
   for row in reader:
      # Tracking totals
         total_months = total_months + 1
         total_net = total_net + int(row[1])
      # Tracking the Net Change
         prev_net = int(row[1])
         net_change = int(row[1]) - prev_net
         net_change_dict = net_change_dict + [net_change]
      # Tracking the profit increase and decrease
         if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

         if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average calculation
monthly_avg = sum(net_change_dict) / len(net_change_dict)

# Print out the budget financial analysis
output = {
   (f"\nFinancial Analysis\n")
   (f"-----------------------------\n")
   (f"Total Months: {total_months}\n")
   (f"Total: ${total_net}\n")
   (f"Average Change: ${monthly_avg)}\n")
   (f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
   (f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")}
print(output)

# Export to the text file
with open(text, "text") as txt_file:
   txt_file.write(output)
