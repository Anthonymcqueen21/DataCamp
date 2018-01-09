'''
Bringing it all together (2)
100xp

Great job! You've now defined the functionality for iterating over entries in a column and
building a dictionary with keys the names of languages and values the number of tweets in
the given language.

In this exercise, you will define a function with the functionality you developed in the
previous exercise, return the resulting dictionary from within the function, and call the
function with the appropriate arguments.

For your convenience, the pandas package has been imported as pd and the 'tweets.csv' file
has been imported into the tweets_df variable.

Instructions
-Define the function count_entries(), which has two parameters. The first parameter is df
for the DataFrame and the second is col_name for the column name.
-Complete the bodies of the if-else statements in the for loop: if the key is in the
dictionary langs_count, add 1 to its current value, else add the key to langs_count and set
its value to 1. Use the loop variable entry in your code.
-Return the langs_count dictionary from inside the count_entries() function.
-Call the count_entries() function by passing to it tweets_df and the name of the column,
'lang'. Assign the result of the call to the variable result.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)
