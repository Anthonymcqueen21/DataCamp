'''
Pandas for more complex querying
100xp

Here, you'll become more familiar with the pandas function read_sql_query() by
using it to execute a more complex query: a SELECT statement followed by both a
WHERE clause AND an ORDER BY clause.

You'll build a DataFrame that contains the rows of the Employee table for which
the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.

Instructions
-Using the function create_engine(), create an engine for the SQLite database
Chinook.sqlite and assign it to the variable engine.
-Use the pandas function read_sql_query() to assign to the variable df the
DataFrame of results from the following query: select all records from the
Employee table where the EmployeeId is greater than or equal to 6 and ordered by
BirthDate (make sure to use WHERE and ORDER BY in this precise order).
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    'SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())
