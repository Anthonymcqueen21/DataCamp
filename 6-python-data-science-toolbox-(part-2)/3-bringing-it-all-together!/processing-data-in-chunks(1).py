'''
Processing data in chunks (1)
100xp

Sometimes, data sources can be so large in size that storing the entire dataset in memory
becomes too resource-intensive. In this exercise, you will process the first 1000 rows of
a file line by line, to create a dictionary of the counts of how many times each country
appears in a column in the dataset.

The csv file 'world_dev_ind.csv' is in your current directory for your use. To begin, you
need to open a connection to this file using what is known as a context manager. For example,
the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp
in the context manager. Here, the with statement is the context manager, and its purpose is to
ensure that resources are efficiently allocated when opening a connection to a file.

If you'd like to learn more about context managers, refer to the DataCamp course on Importing
Data in Python.

Instructions
-Use open() to bind the csv file 'world_dev_ind.csv' as file in the context manager.
-Complete the for loop so that it iterates 1000 times to perform the loop body and process only
the first 1000 rows of data of the file.
'''
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)
