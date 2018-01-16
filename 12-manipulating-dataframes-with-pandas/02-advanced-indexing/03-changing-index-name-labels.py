'''
Changing index name labels

Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.

Similarly, if all the columns are related in some way, you can provide a label for the set of columns.

To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).

INSTRUCTIONS
100XP
Assign the string 'MONTHS' to sales.index.name to create a name for the index.
Print the sales dataframe to see the index name you just created.
Now assign the string 'PRODUCTS' to sales.columns.name to give a name to the set of columns.
Print the sales dataframe again to see the columns name you just created.
'''
# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)
