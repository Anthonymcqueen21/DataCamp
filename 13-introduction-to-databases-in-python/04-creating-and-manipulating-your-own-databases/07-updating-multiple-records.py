'''
Updating Multiple Records

As Jason discussed in the video, by using a where clause that selects more records, you can update multiple records at once. It's time now to practice this!

For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), notes (Column), and census_region_name (Column).

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Build an update statement to update the notes column in the state_fact table to 'The Wild West'. Save it as stmt.
Use a where clause to filter for records that have 'West' in the census_region_name column of the state_fact table.
Execute stmt via the connection and save the output as results.
Hit 'Submit Answer' to print rowcount of the results.
'''
# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)
