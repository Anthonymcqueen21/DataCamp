'''
Deleting all the records from a table

Often, you'll need to empty a table of all of its records so you can reload the data. You can do this with a delete statement with just the table as an argument. For example, in the video, Jason deleted the table extra_employees by executing as follows:

delete_stmt = delete(census)
result_proxy = connection.execute(delete_stmt)
Do be careful, though, as deleting cannot be undone!

INSTRUCTIONS
100XP
Import delete and select from sqlalchemy.
Build a delete statement to remove all the data from the census table. Save it as stmt.
Execute stmt via the connection and save the results.
Hit 'Submit Answer' to select all remaining rows from the census table and print the result to confirm that the table is now empty!
'''
# Import delete, select
from sqlalchemy import delete, select

# Build a statement to empty the census table: stmt
stmt = delete(census)

# Execute the statement: results
results = connection.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table
stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(stmt).fetchall())
