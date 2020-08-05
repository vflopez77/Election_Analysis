# Read votes file, calculate votes and percentage of votes by candidate, and declare winner

# importing necessary modules for manipulating files
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to load the file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize canditate list
candidate_options = []

# Declare an empty candidate votes dictionary
candidate_votes = {}

# Declare winning candidate and winning count tracker variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row and skip
    headers = next(file_reader)

    # Read each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Read the candidate name from each row
        candidate_name = row[2]

        # Check if candidate is in the candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
       f"\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total_votes:,}\n"
       f"-------------------------\n")
    print(election_results, end="")
    # Save tthe final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve a vote count for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote and candidate
        # Determine if the votes are greater than the winning count
        if votes > winning_count and vote_percentage > winning_percentage:
            # If true set the winning count to votes and the winning percentage to vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate equal to the candidate's name
            winning_candidate = candidate_name 

        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    # Print out winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)