'''
Customizing the Hello World of SQL Queries
100xp
Congratulations on executing your first SQL query! Now you're going to figure ou
how to customize your query in order to:

-Select specified columns from a table;
-Select a specified number of rows;
-Import column names from the database table.

Recall that Hugo performed a very similar query customization in the video:

engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()

Packages have already been imported as follows:

from sqlalchemy import create_engine
import pandas as pd
The engine has also already been created:

engine = create_engine('sqlite:///Chinook.sqlite')
The engine connection is already open with the statement

with engine.connect() as con:

All the code you need to complete is within this context.

Instructions
Execute the SQL query that selects the columns LastName and Title from the Employee
table. Store the results in the variable rs.
Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them
in the DataFrame df.
Using the rs object, set the DataFrame's column names to the corresponding names of
the table columns.
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
