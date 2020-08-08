# Election_Analysis

## Project Overview
The Election Commission has provided us with a file of the election data, and asked us to report the results of the election.  

To this end, we will  analyze and summarize the data in the file and provide the following:

- The total number of votes cast.
- A list of all the counties and the percentage and total number of votes cast in each county
- The name of the county with the largest turnout
- The percentage and total votes for each candidate
- The winning candidate and the total votes and percentage cast for them

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.47.3

## Election Results
The analysis of the election data shows that:
- There were <b>369,711</b> votes cast in the election.
- <b>Turnout by County:</b>
  - Jefferson county had 10.5% or 38,855 votes
  - Denver county had 82.8% or 306,055 votes
  - Arapahoe county had 6.7% or 24,801 votes
 - <b>Denver</b> county had the largest turnout
 
  - <b>Candidate Results:</b>
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
    
  - <b>Overall Results:</b>
    - Election Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%

  ## Analysis of Methodology
The data was provided in a flat csv (comma delimited) file.  
In order to read and analyze the data, We imported 2 Python modules: <b>csv</b> and <b>os</b>.  
The csv module makes reading and writing files possible. 
Here is an example of how we were able to read the file:

The os module facilitates working with the local file systems.
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

  ## Summary
