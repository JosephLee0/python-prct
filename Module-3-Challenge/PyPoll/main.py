import os
import csv
import operator

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', "election_data.csv")

# Specify the file to write to
output_path = os.path.join("analysis", "final_result.csv")


# Read in the CSV file
with open(election_data_csv, 'r') as electionfile:

    # Split the data on commas
    data_file = csv.reader(electionfile, delimiter=',')

    # skip the first line that contains headers
    header = next(data_file)

    # temporary  list to collect candidates
    election_list_file = [row[2] for row in data_file]

    # total number of voters
    total_votes = len(election_list_file)

    # list of all the candidates that partake in the election
    candidates_list = list(set(election_list_file))

    # percentage of each voters
    candidates_info = []

    # function to calculate the percentage of any candidate
    def percentage(vote_secured, total):
        return round(((vote_secured/total))*100, 3)

    # looping through the list to get each candidate data
    for candidate in candidates_list:
        vote_secured = election_list_file.count(candidate)
        total_vote = len(election_list_file)

        # storing each candidate info as a dictionary in a list
        candidates_info.append({
            "Name": candidate,
            "Vote_secured": vote_secured,
            "Percetage_secured": percentage(vote_secured, total_vote)
        })

    # searching for the winner
    examine_list = [row['Percetage_secured'] for row in candidates_info]
    index, value = max(enumerate(examine_list), key=operator.itemgetter(1))
    election_winner = candidates_list[index]

    # Printing the result
    print('Election Results')
    print('---------------------------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------------------------------------------')

    # Printing each candidate with loop
    for candidate in candidates_info:
        print(
            f'{candidate["Name"]}: {candidate["Percetage_secured"]}% ({candidate["Vote_secured"]})\n')

    print('----------------------------------------------------------')
    print(f'Winner: {election_winner}')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as resultfile:

    # Initialize csv.writer
    output_writer = csv.writer(resultfile, delimiter=',')

    output_writer.writerow(['Election Results'])
    output_writer.writerow(
        ['---------------------------------------------------------'])
    output_writer.writerow([f'Total Votes: {total_votes}'])
    output_writer.writerow(
        ['---------------------------------------------------------'])

    # Printing each candidate with loop
    for candidate in candidates_info:
        output_writer.writerow(
            [f'{candidate["Name"]}: {candidate["Percetage_secured"]}% ({candidate["Vote_secured"]})'])

    output_writer.writerow(
        ['----------------------------------------------------------'])
    output_writer.writerow([f'Winner: {election_winner}'])
