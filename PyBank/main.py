# Let us import the libraries that we'll use for this project
import os
import csv

# Let us declare the global variables that we'll use in this project
total_months = 0
total_amount = 0
monthly_change = []
month_count = []
max_increase = 0
max_increase_month = 0
max_decrease = 0
max_decrease_month = 0

# Inform Python where source csv file is stored that will be used for our analysis
csvpath = os.path.join('Resources/budget_data.csv')

# Let us open the csv file. newline='' would get rid of the blank line that will be added after every row
with open(csvpath, newline='') as csvfile:
    # Since it is a csv file, the delimiter is set to ','
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Since our csv file has headers, we need to skip them
    # otherwise they will be included in our calculations and would result in errors
    # Since headers contains text/string and Profit/Loss contains numbers
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Now let us calculate total number of months, net total amount of "Profit/Losses" 
    # Set Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    max_increase = int(row[1])
    max_increase_month = row[0]
    
    for row in csvreader:
        # Now let us calculate total number of months
        total_months += 1
        
        # now we will calculate net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])

        # In order to calculate average change of profit/loss
        # we need to calculate change from current month to the previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Now we need to calculate maximum increase
        # One way of doing this is by setting a temperary variable to 0 and comparing it to every cell
        # if found greater, storing that value in a variable
        if int(row[1]) > max_increase:
            max_increase = int(row[1])
            max_increase_month = row[0]
            
        # in order to calculate maximum decrease, we can use the same principal that we used above
        if int(row[1]) < max_decrease:
            max_decrease = int(row[1])
            max_decrease_month = row[0]  
        
    # Now, in order to calculate average change, all we need to do is add all the values stored in monthly change
    # and divide it by the number of values stored in that same list
    average_change = sum(monthly_change)/ len(monthly_change)
    
    # Highest and lowest values in monthly change can be calculated by using the max and min function
    highest = max(monthly_change)
    lowest = min(monthly_change)

    # Now let us print our results
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {max_increase_month} (${highest})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${lowest})")

# Now we need to output our results to a text file
# We need to specify the file path where our results will be saved
output_file = os.path.join('analysis/budget_data.txt')

with open(output_file, 'w',) as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_amount}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_month} (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${lowest})")