'''
Processing large amounts of Twitter data
100xp

Sometimes, the data we have to process reaches a size that is too much for a computer's
memory to handle. This is a common problem faced by data scientists. A solution to this
is to process an entire data source chunk by chunk, instead of a single go all at once.

In this exercise, you will do just that. You will process a large csv file of Twitter
data in the same way that you processed 'tweets.csv' in Bringing it all together
exercises of the prequel course, but this time, working on it in chunks of 10 entries
at a time.

If you are interested in learning how to access Twitter data so you can work with it on
your own system, refer to Part 2 of the DataCamp course on Importing Data in Python.

The pandas package has been imported as pd and the file 'tweets.csv' is in your curren
 directory for your use. Go for it!

Instructions
-Initialize an empty dictionary counts_dict for storing the results of processing the
Twitter data.
-Iterate over the 'tweets.csv' file by using a for loop. Use the loop variable chunk and
iterate over the call to pd.read_csv() with a chunksize of 10.
-In the inner loop, iterate over the column 'lang' in chunk by using a for loop. Use the
loop variable entry.
'''
# Import packages
import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('../_datasets/tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
