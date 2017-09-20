'''
Bringing it all together (3)
100xp

In the previous exercise, you built on your function count_entries() to add a try-except block.
This was so that users would get helpful messages when calling your count_entries() function
and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise
a ValueError in the case that the user provides a column name that isn't in the DataFrame.

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has
been imported into the DatFrame tweets_df. Parts of the code from your previous work are
also provided.

Instructions
-If col_name is NOT a column in the DataFrame df, raise a ValueError 'The DataFrame does not
have a ' + col_name + ' column.'.
-Call your new function count_entries() to analyze the 'lang' column of tweets_df. Store the
result in result1.
-Print result1. This has been done for you, so hit 'Submit Answer' to check out the result.
In the next exercise, you'll see that it raises the necessary ValueErrors.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)