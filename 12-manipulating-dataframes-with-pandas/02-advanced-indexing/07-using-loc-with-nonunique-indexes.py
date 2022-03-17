'''
Using .loc[] with nonunique indexes

As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.

As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.

INSTRUCTIONS
100XP
Set the index of sales to be the column 'state'.
Print the sales DataFrame to verify that indeed you have an index with state values.
Access the data from 'NY' and print it to verify that you obtain two rows.
'''
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])
