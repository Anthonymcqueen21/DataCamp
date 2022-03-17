'''
Index ordering

In this exercise, the DataFrame election is provided for you. It contains the 2012 US election results for the state of Pennsylvania with county names as row indices. Your job is to select 'Bedford' county and the'winner' column. Which method is the preferred way?

Feel free to explore the DataFrame in the IPython Shell.

INSTRUCTIONS
50XP
Possible Answers
election['Bedford', 'winner']
press 1

election['Bedford']['winner']
press 2

election['eggs']['Bedford']
press 3

election.loc['Bedford', 'winner']
press 4

election.iloc['Bedford', 'winner']
press 
'''

# election.loc['Bedford', 'winner']
