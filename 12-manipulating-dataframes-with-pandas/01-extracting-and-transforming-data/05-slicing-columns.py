'''
Slicing columns

Similar to row slicing, columns can be sliced by value. In this exercise, your job is to slice column names from the Pennsylvania election results DataFrame using .loc[].

It has been pre-loaded for you as election, with the index set to 'county'.

INSTRUCTIONS
100XP
Slice the columns from the starting column to 'Obama' and assign the result to left_columns
Slice the columns from 'Obama' to 'winner' and assign the result to middle_columns
Slice the columns from 'Romney' to the end and assign the result to right_columns
The code to print the first 5 rows of left_columns, middle_columns, and right_columns has been written, so hit 'Submit Answer' to see the results!
'''
# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())
