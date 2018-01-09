'''
Conditional list comprehesions for time-stamped data
100xp

Great, you've successfully extracted the data of interest, the time, from a pandas DataFrame!
Let's tweak your work further by adding a conditional that further specifies which entries to select.

In this exercise, you will be using a list comprehension to extract the time from time-stamped
Twitter data. You will add a conditional expression to the list comprehension so that you only
select the times in which entry[17:19] is equal to '19'. The pandas package has been imported as
pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.

Instructions

Extract the column 'created_at' from df and assign the result to tweet_time.
Create a list comprehension that extracts the time from each row in tweet_time. Each row is a
string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use entry as the iterator variable and assign the result to tweet_clock_time. Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.
'''
# Import packages
import pandas as pd

df = pd.read_csv('../_datasets/tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
