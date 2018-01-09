'''
Bringing it all together (1)
100xp

This is awesome! You have now learned how to write anonymous functions using lambda,
how to pass lambda functions as arguments to other functions such as map(), filter(),
and reduce(), as well as how to write errors and output custom error messages within
your functions. You will now put together these learnings to good use by working with
a Twitter dataset. Before practicing your new error handling skills,in this exercise,
you will write a lambda function and use filter() to select retweets, that is, tweets
that begin with the string 'RT'.

To help you accomplish this, the Twitter data has been imported into the DataFrame,
tweets_df. Go for it!

Instructions
-In the filter() call, pass a lambda function and the sequence of tweets as strings,
tweets_df['text']. The lambda function should check if the first 2 characters in a
tweet x are 'RT'. Assign the resulting filter object to result. To get the first 2
characters in a tweet x, use x[0:2]. To check equality, use a Boolean filter with ==.
-Convert result to a list and print out the list.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
