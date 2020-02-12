# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
election_csv = os.path.join(".." "Resources", "election_data.csv")
text = os.path.join(".." "Resources", "election_analysis.txt")

# Candidate
candidate = row[2]

# Total votes
total_votes = 0

# The winner
winning_vote_num = 0
winning candidate = ""

# The candidate option dictionaries
candidate_votes = {}
candidate_options = []

# Reading the csv and then creating the dictionary
with open(election_csv) as election_data:
    reader = csv.reader(election_data)

    for row in reader:

        # Add to total votes
        total_votes = total_votes + 1

        # Define candidate name for each row
        candidate_name = row[2]

        # If the candidate is not there
        if candidate_name not in candidate_options:

            # Add it to the candidate list and track
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Then add vote to counter
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(text_file, "text") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)

    # Save to text file
    txt_file.write(election_results)

    # Determine the winner
    for candidate in candidate_votes:

        # Vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Winning vote count and winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print results
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # Save to text file
        txt_file.write(voter_output)

    # Print winning candidate
    winning_candidate_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_results)

    # Save winning candidate's name to text file
    txt_file.write(winning_candidate_results)


