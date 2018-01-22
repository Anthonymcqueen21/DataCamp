'''
Updating individual records

The update statement is very similar to an insert statement, except that it also typically uses a where clause to help us determine what data to update. You'll be using the FIPS state code using here, which is appropriated by the U.S. government to identify U.S. states and certain other associated areas. Recall that you can update all wages in the employees table as follows:

stmt = update(employees).values(wage=100.00)
For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), name (Column), and fips_state (Column).

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Build a statement to select all columns from the state_fact table where the name column is New York. Call it select_stmt.
Print the results of executing the select_stmt and fetching all records.
Build an update statement to change the fips_state column code to 36, save it as stmt.
Use a where clause to filter for states with the name of 'New York' in the state_fact table.
Execute stmt via the connection and save the output as results.
Hit 'Submit Answer' to print the rowcount of the results and the results of executing select_stmt. This will verify the fips_state code is now 36.
'''
# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state=36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())
