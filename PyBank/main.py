import os
import csv

# Store the file path associated with the file 
Bank_csv = os.path.join("budget_data.csv")

# Open the file in read
with open(Bank_csv) as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")


    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

# Define the function for toal months
def print_totals(Date)
    if january == "Jan"
        