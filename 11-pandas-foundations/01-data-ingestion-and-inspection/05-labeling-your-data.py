'''
Labeling your data

You can use the DataFrame attribute df.columns to view and assign new string labels to columns in a pandas DataFrame.

In this exercise, we have imported pandas as pd and defined a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia). Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. Your job is to use the df.columns attribute to re-assign descriptive column labels.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Create a list of new column labels with 'year', 'artist', 'song', 'chart weeks', and assign it to list_labels.
-Assign your list of labels to df.columns.
'''
# Build a list of labels: list_labels
list_labels = ['year','artist','song','chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels
