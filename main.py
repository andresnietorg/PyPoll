# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

import csv
import os

# File paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
print("Processing votes:", end=" ")
with open(file_to_load, 'r') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header row

    # Process each vote
    for row in reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

        # Print progress
        if total_votes % 10000 == 0:
            print(".", end="", flush=True)

print(f"\nTotal votes processed: {total_votes}")

# Calculate results and find winner
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Prepare the analysis results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{chr(10).join(results)}
-------------------------
Winner: {winner["name"]}
-------------------------
"""

# Print the results
print(output)

# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

print(f"Results exported to {file_to_output}")