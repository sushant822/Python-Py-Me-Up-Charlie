# Let us import the libraries that we'll use for this project
import os
import csv

# Let us declare the global variables that we'll use in this project
total_vote = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

# Inform Python where source csv file is stored that will be used for our analysis
csvpath = os.path.join('Resources/election_data.csv')

# Let us open the csv file. newline='' would get rid of the blank line that will be added after every row
with open(csvpath, newline='') as csvfile:

    # Since it is a csv file, the delimiter is set to ','
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Since our csv file has headers, we need to skip them
    # otherwise they will be included in our calculations and would result in errors
    # Since headers contains text/string and Profit/Loss contains numbers
    csv_header = next(csvfile)

    for row in csvreader:
        
        # Now let us calculate total votes casted
        total_vote += 1
        
        # now we need to calculate total number of votes casted for each candidate
        # this can be achieved by using the if statement
        # we will set the first row to the first candidate and if found true, then we can add 1 to our count
        # we can do the same for rest of the candidates
        if (row[2] == "Khan"):
            khan_vote += 1
        elif (row[2] == "Correy"):
            correy_vote += 1
        elif (row[2] == "Li"):
            li_vote += 1
        else:
            otooley_vote += 1
            
    # In order to calculate percentage of votes each candidate won,
    # we can simply divide total votes casted for each candidate by total number of votes casted overall
    # we can then store this in a variable
    khan_percent = khan_vote / total_vote
    correy_percent = correy_vote / total_vote
    li_percent = li_vote / total_vote
    otooley_percent = otooley_vote / total_vote
    
    # maximum votes can be found by using the max function on the total number of votes each candidate won   
    max_vote = max(khan_vote, correy_vote, li_vote, otooley_vote)
    
    # winning candidate can be determined by using the if and elif function
    # since in the above step, we have the maximum number of votes, we can compare them to each candidate
    # and with whomesoever they match, will be our winner.
    # we will also store the name of the winner in a variable
    if max_vote == khan_vote:
        winner = "Khan"
    elif max_vote == correy_vote:
        winner = "Correy"
    elif max_vote == li_vote:
        winner = "Li"
    else:
        winner = "O'Tooley"
        

# Now we can print our results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_vote}")
print("---------------------------")
print(f"Kahn: {round((khan_percent*100), 3)}% ({khan_vote})")
print(f"Correy: {round((correy_percent*100), 3)}% ({correy_vote})")
print(f"Li: {round((li_percent*100), 3)}% ({li_vote})")
print(f"O'Tooley: {round((otooley_percent*100), 3)}% ({otooley_vote})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Now we need to output our results to a text file
# We need to specify the file path where our results will be saved
output_file = os.path.join('analysis/election_data.txt')

with open(output_file, 'w',) as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {total_vote}\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Kahn: {round((khan_percent*100), 3)} ({khan_vote})\n")
    txtfile.write(f"Correy: {round((correy_percent*100), 3)} ({correy_vote})\n")
    txtfile.write(f"Li: {round((li_percent*100), 3)} ({li_vote})\n")
    txtfile.write(f"O'Tooley: {round((otooley_percent*100), 3)} ({otooley_vote})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------")