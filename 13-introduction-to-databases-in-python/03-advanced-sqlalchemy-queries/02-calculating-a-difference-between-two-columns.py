'''
Calculating a Difference between Two Columns

Often, you'll need to perform math operations as part of a query, such as if you wanted to calculate the change in population from 2000 to 2008. For math operations on numbers, the operators in SQLAlchemy work the same way as they do in Python.

You can use these operators to perform addition (+), subtraction (-), multiplication (*), division (/), and modulus (%) operations. Note: They behave differently when used with non-numeric column types.

Let's now find the top 5 states by population growth between 2000 and 2008.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Define a select statement called stmt to return:
i) The state column of the census table (census.columns.state).
ii) The difference in population count between 2008 (census.columns.pop2008) and 2000 (census.columns.pop2000) labeled as 'pop_change'.
Group the statement by census.columns.state.
Order the statement by population change ('pop_change') in descending order. Do so by passing it desc('pop_change').
Use the .limit() method on the statement to return only 5 records.
Execute the statement and fetchall the records.
The print statement has already been written for you. Hit 'Submit Answer' to view the results!
'''
 # Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt
stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

# Return only 5 results: stmt
stmt = stmt.limit(5)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
