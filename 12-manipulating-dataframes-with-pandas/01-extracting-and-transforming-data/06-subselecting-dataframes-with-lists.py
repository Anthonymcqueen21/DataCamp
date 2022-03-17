'''
Subselecting DataFrames with lists

You can use lists to select specific row and column labels with the .loc[] accessor. In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.

INSTRUCTIONS
100XP
Create the list of row labels ['Philadelphia', 'Centre', 'Fulton'] and assign it to rows.
Create the list of column labels ['winner', 'Obama', 'Romney'] and assign it to cols.
Create a new DataFrame by selecting with rows and cols in .loc[] and assign it to three_counties.
Print the three_counties DataFrame. This has been done for you, so hit 'Submit Answer` to see your new DataFrame.
'''
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)
