'''
Bringing it all together (1)
100xp

You've got your first taste of writing your own functions in the previous exercises.
You've learned how to add parameters to your own function definitions, return a value
or multiple values with tuples, and how to call the functions you've defined.

In this and the following exercise, you will bring together all these concepts and apply
them to a simple data science problem. You will load a dataset and develop functionalities
to extract simple insights from the data.

For this exercise, your goal is to recall how to load a dataset into a DataFrame.
The dataset contains Twitter data and you will iterate over entries in a column to
build a dictionary in which the keys are the names of languages and the values are
the number of tweets in the given language. The file tweets.csv is available in your
current directory.

Instructions
-Import the pandas package with the alias pd.
-Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
-Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
-Complete the bodies of the if-else statements in the for loop: if the key is in the
dictionary langs_count, add 1 to its current value, else add the key to langs_count
and set its value to 1. Use the loop variable entry in your code.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
