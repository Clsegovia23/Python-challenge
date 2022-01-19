import os
import csv

# set path for file

csvpath = os.path.join("Resources", "budget_data.csv")

# set variables
count = 0
months = 0
average = 0
total = 0
current = 0
total_chg = 0
great_inc_profit = 0
great_dec_profit = 0
profit_inc_dates = ""
loss_decr_dates = ""

monthly_chg = []
total_profit = 0
total_chg_profits = 0
profit = []
initial_profit = 0

# setup to read data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(csvreader)
    count = 0
    total = 0
    date = []
# The total number of months included in the dataset
    for row in csvreader:
        total += float(row[1])
        count += 1
        current = float(row[1])
        date.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])
        monthly_chg_profit = final_profit - initial_profit
        monthly_chg.append(monthly_chg_profit)
        total_chg_profits = total_chg_profits + monthly_chg_profit
        initial_profit = final_profit
        avg_chg_profits = (total_chg_profits/count)
        great_inc_profit = max(monthly_chg)
        great_dec_profit = min(monthly_chg)
        profit_inc_dates = date[monthly_chg.index(great_inc_profit)]
        loss_decr_dates = date[monthly_chg.index(great_dec_profit)]


# The net total amount of "Profit/Losses" over the entire period
# if(current >= 0): 
#         if(current > great_inc_profit):
#             #great_inc_profit = current
#             great_inc_profit = 
#             profit_inc_dates = str(row[0])
#         elif(current < 0):
#             if(current < great_dec_profit):
#                 #great_dec_profit = current

#                 loss_decr_dates = str(row[0])
# average = total / count

# print(count, total) 

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# with open("analysis/Fin_Analysis", 'w') as textfile:
#     textfile.write("Financial Analysis" + "\n")
#     textfile.write("--------------------------\n")
#     textfile.write("Total Months: " + str(count) + "\n")
#     textfile.write("Total Profits: " + str(total_profit) + "\n")
#     textfile.write("Average Change: " + "$" + str(avg_chg_profits) + "\n")
#     textfile.write("Greatest Increase in Profits: " + str(profit_inc_dates) + "($ "+ str(great_inc_profit) + ")\n")
#     textfile.write("Greatest Decrease in Profits: " + str(loss_decr_dates) + "($ " + str(great_dec_profit) + ")\n")

#printing summary:
print(f'Financial Analysis')
print(f'---------------------------------------------------')
print("Total Months: " + str(count))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(avg_chg_profits))
print("Greatest Increase in Profits: " + str(profit_inc_dates) + "($ "+ str(great_inc_profit) +")")
print("Greatest Decrease in Profits: " + str(loss_decr_dates) + "($ " + str(great_dec_profit)+")")