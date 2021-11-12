# Election_Analysis

## Overview of Election Audit

The purpose of this project is to use Python to automate certifying election results for a congressional precinct in Colorado.  Certifying this election using this method means this same method may be used to certify other elections for congressional, senatorial and local elections.  In addition to providing the breakdown of the votes by candidate, we need to provide a breakdown by county.

## Election-Audit Results

- The total number of votes cast in this congressional election is 369,711.
- The breakdown of votes and percentage of total vote per county is as follows:
  - Jefferson:  38,855 votes were cast, which is 10.5% of the total vote.
  - Denver:  306,055 votes were cast, which is 82.8% of the total vote.
  - Arapahoe:  24,801 votes were cast, which is 6.7% of the total vote.
- Denver County had the largest number of votes, and by an overwhelming majority.
- The breakdown of votes and percentage of total vote per candidate is as follows:
  - Charles Casper Stockham received 85,213 votes, which is 23.0% of the total vote.
  - Diana DeGette received 272,892 votes, which is 73.8% of the total vote.
  - Raymon Anthony Doane received 11,606 votes, which is 3.1% of the total vote.
- Diana DeGette clearly won the election with 272,892 votes and 73.8% of the total vote.

Below are the results provided by the python program that was written.

![Election Results](https://github.com/mshideler/Election_Analysis/blob/main/Resources/ElectionResults.PNG)

Here is the code used to read the data file with the votes:
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_turnout_name = ""
county_turnout_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```

Here is the code used to analyze what was read and output the results to both the terminal and a text file.
```
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        covotes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        covote_percent = float(covotes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f'{county_name}: {covote_percent:.1f}% ({covotes:,})\n')
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if covotes > county_turnout_votes:
            county_turnout_name = county_name
            county_turnout_votes = covotes

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f'-------------------------\n'
        f'Largest County Turnout: {county_turnout_name}\n'
        f'-------------------------\n')
    print(largest_county_turnout)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```

## Election-Audit Summary

Considering the success of the python program certifying the election results, we propose the election commission use this script for all elections going forward.  If approved, the code would need to be modified slightly to account for the different types of elections.  Here are a couple of suggestions:

1. Update the terminology in the code so it properly reflects where the votes are coming from, such as precincts, judicial districts, etc.  This information can be provided by the person running the program by adding prompts for input to the code.  Then, after adding a little more code, program could then update the variables and output with the correct terminology.

2. Often times, elections include asking the people if they agree a provision should be passed, such as adding a new tax or a construction project should be approved.  The code would need to be modified to take into account yes/no votes.