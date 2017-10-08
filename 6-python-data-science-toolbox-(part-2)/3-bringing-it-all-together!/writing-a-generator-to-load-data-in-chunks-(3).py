'''
Writing a generator to load data in chunks (3)
100xp

Great! You've just created a generator function that you can use to help you process large files.

Now let's use your generator function to process the World Bank dataset like you did previously.
You will process the file line by line, to create a dictionary of the counts of how many times each
country appears in a column in the dataset. For this exercise, however, you won't process just 1000
rows of data, you'll process the entire dataset!

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and
ready for your use. Go for it!

Instructions
-Bind the file 'world_dev_ind.csv' to file in the context manager with open().
-Complete the for loop so that it iterates over the generator from the call to read_large_file()
to process all the rows of the file.
'''
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)
