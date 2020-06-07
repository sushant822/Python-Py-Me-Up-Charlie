# Let us import the libraries that we'll use for this project
import os
import csv 

# Inform Python where source csv file is stored that will be used for our analysis
csvpath = os.path.join('Resources/employee_data.csv')

# First, we need to define the abbreviations for each state and store them in a variable as dictionary
states_us = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Let us declare empty lists where we will store the data
emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []

#opens csv file and reads in as ordered dictionary
#no need to skip header row because it serves as dict keys
#with open(csvpath, 'r') as csvfile:  
    #csvreader = csv.DictReader(csvfile)
with open(csvpath, newline='') as csvfile:
    
    # Since it is a csv file, the delimiter is set to ','
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
    for row in csvreader:
        # Append employee id which is stored in the first row to emp_id empty array which we created above
        emp_id.append(row[0])
        
        # Employee name is stored in single row in the csv file
        # but we need to split it in first name and last name
        # one way of doing this by storing the employee name in a variable and applying the .split function
        # This will split the first and last name in two rows.
        # First name will be stored in a temporary variable which we will call first_name_1
        # and last name will be stored in another temporary variable which we will call last_name_1
        emp_name = row[1]
        name_split = emp_name.split()
        first_name_1 = name_split[0]
        last_name_1 = name_split[1]
        
        # We can then append this to the first_name and last_name empty array that we created above
        first_name.append(first_name_1)
        last_name.append(last_name_1)
        
        # We can use the above mentioned method to split the date of birth, store it in temprory variables
        # and append it to the dob empty array we created above
        org_dob = row[2]
        dob_1 = org_dob.split("-")
        dob_year = dob_1[0]
        dob_month = dob_1[1]
        dob_day = dob_1[2]
        dob_all = dob_month + "/" + dob_day + "/" + dob_year
        dob.append(dob_all)
        
        # Social Securit Number's first 5 digits must be replaced with *'s
        # one way of doing this is splitting the data and joining the last row (which contains the last 4 digits)
        # with *'s and appending it to the ssn empty array we created above
        ssn_org = row[3]
        star_ssn = "***-**-" + ssn_org.split("-")[2]
        ssn.append(star_ssn)
        
        # States must be replaces with the abbreviations for the respective state
        # This can be achieved by using the get method for dictionaries
        # The get method will look at the current state name and
        # get its abbreviated name from the dictionary that we created above
        # we can then append this to the empty state array that we created above
        state_org = row[4]
        abbr_state = states_us.get(state_org)
        state.append(abbr_state)
        
# Now, we need to merge all the data. This can be done by using the zip function
merged_data = zip(emp_id, first_name, last_name, dob, ssn, state)

# Now we need to output our results to a text file
# We need to specify the file path where our results will be saved
output_file = os.path.join('analysis/employee_data.csv')

with open(output_file, 'w', newline='') as csvwrite:
    csvfile = csv.writer(csvwrite, delimiter = ",")
    csvfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    csvfile.writerows(merged_data)