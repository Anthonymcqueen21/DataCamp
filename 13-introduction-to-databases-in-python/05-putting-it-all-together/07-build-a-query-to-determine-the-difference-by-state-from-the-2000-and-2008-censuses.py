'''
Build a Query to Determine the Difference by State from the 2000 and 2008 Censuses

In this final exercise, you will write a query to calculate the states that changed the most in population. You will limit your query to display only the top 10 states.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Build a statement to:
Select state.
Calculate the difference in population between 2008 (pop2008) and 2000 (pop2000).
Group the query by census.columns.state using the .group_by() method on stmt.
Order by 'pop_change' in descending order using the .order_by() method with the desc() function on 'pop_change'.
Limit the query to the top 10 states using the .limit() method.
Execute the query and store it as results.
Print the state and the population change for each result. This has been done for you, so hit 'Submit Answer' to see the result!
'''
# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
