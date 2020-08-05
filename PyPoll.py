import csv
import os

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to load the file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyse data here
    #print(election_data)
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    #print(headers)

    # Read each row in the CSV file
    for row in file_reader:
        #print(row)
        # 2. Add to the total vote count
        total_votes += 1

# 3. Print the total votes
print(total_votes)

# Close the file
#election_data.close()

# # Writing to Analysis text file
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write the file header
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("_________________________\n")
#     # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")
