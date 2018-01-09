'''
Bringing it all together (1)
100xp
Recall the Bringing it all together exercise in the previous chapter where you did a
simple Twitter analysis by developing a function that counts how many tweets are in
certain languages. The output of your function was a dictionary that had the language
as the keys and the counts of tweets in that language as the value.

In this exercise, we will generalize the Twitter language analysis that you did in the
previous chapter. You will do that by including a default argument that takes a column name.

For your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported
into the DataFrame tweets_df. Parts of the code from your previous work are also provided.

Instructions
-Complete the function header by supplying the parameter for a DataFrame df and the parameter
col_name with a default value of 'lang' for the DataFrame column name.
-Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'.
Assign the result to result1. Note that since 'lang' is the default value of the col_name
parameter, you don't have to specify it here.
-Call count_entries() by passing the tweets_df DataFrame and the column name 'source'.
Assign the result to result2.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

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
result1 = count_entries(tweets_df, col_name='lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')

# Print result1 and result2
print(result1)
print(result2)
