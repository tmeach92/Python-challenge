import os
import csv

#path to file we are using
Pybank_csv = os.path.join("Resources","PyBank_data.csv")

#assign variables
total_months = 0
profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
change_profit_loss = 0
total_profit_loss = 0
months = []
net_profit_loss = []
changes_in_profit_loss = []

#open csv
with open (Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
    
        #total number of months
        total_months = total_months + 1
        months.append(row[0])

        #net total of "profit/losses"
        net_profit_loss.append(row[1])
        profit_loss = profit_loss + int(row[1])

        #average of changes in "profit/losses"
        current_month_profit_loss = int(row[1])
        change_profit_loss = current_month_profit_loss - previous_month_profit_loss

        changes_in_profit_loss.append(change_profit_loss)

        total_profit_loss = total_profit_loss + change_profit_loss
        previous_month_profit_loss = current_month_profit_loss

        #changes_in_profit_loss
        average_change_profits = (total_profit_loss/total_months)

        #greatest increase in profits
        greatest_increase_profits = max(changes_in_profit_loss)
        greatest_decrease_profits = min(changes_in_profit_loss)

        increase_date = months[changes_in_profit_loss.index(greatest_increase_profits)]
        decrease_date = months[changes_in_profit_loss.index(greatest_decrease_profits)]

    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(profit_loss))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")



