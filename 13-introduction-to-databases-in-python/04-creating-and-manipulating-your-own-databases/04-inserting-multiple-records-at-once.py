'''
Inserting Multiple Records at Once

It's time to practice inserting multiple records at once!

As Jason showed you in the video, you'll want to first build a list of dictionaries that represents the data you want to insert. Then, in the .execute() method, you can pair this list of dictionaries with an insert statement, which will insert all the records in your list of dictionaries.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
Build an insert statement for the data table for a multiple insert, save it as stmt.
Execute stmt with the values_list via connection and store the results. Make sure values_list is the second argument to .execute().
Print the rowcount of the results.
'''
# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
