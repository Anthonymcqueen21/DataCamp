'''
Indexing and column rearrangement

There are circumstances in which it's useful to modify the order of your DataFrame columns. We do that now by extracting just two columns from the Pennsylvania election results DataFrame.

Your job is to read the CSV file and set the index to 'county'. You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters']. The CSV file is provided to you in the variable filename.

INSTRUCTIONS
100XP
Import pandas as pd.
Read in filename using pd.read_csv() and set the index to 'county' by specifying the index_col parameter.
Create a separate DataFrame results with the columns ['winner', 'total', 'voters'].
Print the output using results.head(). This has been done for you, so hit 'Submit Answer' to see the new DataFrame!
'''
# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())
