'''
Setting & sorting a MultiIndex

In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself! With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.

To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.

INSTRUCTIONS
100XP
Create a MultiIndex by setting the index to be the columns ['state', 'month'].
Sort the MultiIndex using the .sort_index() method.
Print the sales DataFrame. This has been done for you, so hit 'Submit Answer' to verify that indeed you have an index with the fields state and month!
'''
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state','month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)
