'''
Handling a ResultSet

Recall the differences between a ResultProxy and a ResultSet:

ResultProxy: The object returned by the .execute() method. It can be used in a variety of ways to get the data returned by the query.
ResultSet: The actual data asked for in the query when using a fetch method such as .fetchall() on a ResultProxy.
This separation between the ResultSet and ResultProxy allows us to fetch as much or as little data as we desire.

Once we have a ResultSet, we can use Python to access all the data within it by column name and by list style indexes. For example, you can get the first row of the results by using results[0]. With that first row then assigned to a variable first_row, you can get data from the first column by either using first_row[0] or by column name such as first_row['column_name']. You'll now practice exactly this using the ResultSet you obtained from the census table in the previous exercise. It is stored in the variable results. Enjoy!

INSTRUCTIONS
100XP
Extract the first row of results and assign it to the variable first_row.
Print the value of the first column in first_row.
Print the value of the 'state' column in first_row.
'''
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the row by using an index
print(first_row[0])

# Print the state column of the row by using its name
print(first_row['state'])
