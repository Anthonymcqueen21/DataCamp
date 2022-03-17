'''
Filtering columns using other columns

The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.

Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.

The DataFrame has been pre-loaded for you as election.

INSTRUCTIONS
100XP
Import numpy as np.
Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
Convert the entries in the 'winner' column where the result was too close to call to np.nan.
Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.
'''
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())