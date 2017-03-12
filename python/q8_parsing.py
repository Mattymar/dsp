# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

#open the file
with open('./football.csv', 'r') as f:
    # read the file into a list
    reader = list(csv.reader(f))

    # get the index of 'Goals' and 'Goals Allowed' stats
    goals = reader[0].index('Goals')
    goals_allowed = reader[0].index('Goals Allowed')

    # get the absolute value of the differences in goals/allowed for each team
    diffs = [abs(int(x[goals]) - int(x[goals_allowed])) for x in reader[1:]]

    # find the minimum difference and determine the index representing the team
    min_diff_index = diffs.index(min(diffs))

    # determine the team name and print it out
    print(reader[min_diff_index + 1][0])
