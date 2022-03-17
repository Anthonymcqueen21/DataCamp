'''
Positional and labeled indexing

Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.

Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!

To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.

INSTRUCTIONS
100XP
Explore the DataFrame in the IPython Shell using election.head().
Assign the row position of election.loc['Bedford'] to x.
Assign the column position of election['winner'] to y.
Hit 'Submit Answer' to print the boolean equivalence of the .loc and .iloc selections.
'''

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

