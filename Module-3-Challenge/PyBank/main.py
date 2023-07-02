import os
import csv
import operator


# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', "budget_data.csv")

# Specify the file to write to
output_path = os.path.join("analysis", "final_result.csv")

# To read the csv file
with open(budget_data_csv, 'r') as budget_Data_File:

    # Split the data on commas
    budget_Data = csv.reader(budget_Data_File, delimiter=',')

    # skip the first line that contains headers
    header = next(budget_Data)

    # the budget file in list form
    budget_data_list = [row for row in budget_Data]

    # total month
    all_months = [row[0] for row in budget_data_list]
    total_month = len(all_months)

    # the list of all the profit/loss over the period
    profit_loss = [int(row[1]) for row in budget_data_list]

    # the net amount of profit/loss over the period
    net_total = sum(profit_loss)

    # creating a temporary holder for previous value
    prev = 0

    # a list of the changes in profit/loss over a duration
    changes_list = []

    lenght = len(profit_loss)
    i = 1

    while i < lenght:
        prev = profit_loss[i]-profit_loss[i-1]
        changes_list.append(prev)
        i = i+1

    # the average chnage over the entire period
    average_change = sum(changes_list)/len(changes_list)

    # searching for the greatest increase and greatest decrease in profit
    max_index, max_value = max(
        enumerate(changes_list), key=operator.itemgetter(1))
    min_index, min_value = min(
        enumerate(changes_list), key=operator.itemgetter(1))
    greatest_increase_date = all_months[max_index+1]
    greatest_decrease_date = all_months[min_index+1]
    greatest_increase_amount = max_value
    greatest_decrease_amount = min_value

    print('Financial Analysis')
    print('-----------------------------------------------')
    print(f'Total Months: {total_month}')
    print(f'Total: ${net_total}')
    print(f'Average change: ${round(average_change,2)}')
    print(
        f'Greatest Increase in profits: {greatest_increase_date} (${greatest_increase_amount})')
    print(
        f'Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease_amount})')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as resultfile:

    # Initialize csv.writer
    output_writer = csv.writer(resultfile, delimiter=',')

    output_writer.writerow(['Financial Analysis'])
    output_writer.writerow(['-----------------------------------------------'])
    output_writer.writerow([f'Total Months: {total_month}'])
    output_writer.writerow([f'Total: ${net_total}'])
    output_writer.writerow([f'Average change: ${round(average_change,2)}'])
    output_writer.writerow(
        [f'Greatest Increase in profits: {greatest_increase_date} (${greatest_increase_amount})'])
    output_writer.writerow(
        [f'Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease_amount})'])
