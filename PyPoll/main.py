import os
import csv

# Store the file path associated with the file 
election_csv = os.path.join("PyPoll\Resources\election_data.csv")

# Open the file in read
with open(election_csv) as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")


    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")