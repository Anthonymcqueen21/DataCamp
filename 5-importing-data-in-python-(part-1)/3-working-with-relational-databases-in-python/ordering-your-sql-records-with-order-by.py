'''
Ordering your SQL records with ORDER BY
100xp

You can also order your SQL query results. For example, if you wanted to get
all records from the Customer table of the Chinook database and order them in
increasing order by the column SupportRepId, you could do so with the following query:

"SELECT * FROM Customer ORDER BY SupportRepId"

In fact, you can order any SELECT statement by any column.

In this interactive exercise, you'll select all records of the Employee table and order them in increasing order by the column BirthDate.

Packages are already imported as follows:

import pandas as pd
from sqlalchemy import create_engine

Get querying!

Instructions
-Using the function create_engine(), create an engine for the SQLite database
Chinook.sqlite and assign it to the variable engine.
-In the context manager, execute the query that selects all records from the
Employee table and orders them in increasing order by the column BirthDate.
Assign the result to rs.
-In a call to pd.DataFrame(), apply the method fetchall() to rs in order to
fetch all records in rs. Store them in the DataFrame df.
-Set the DataFrame's column names to the corresponding names of the table columns.
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
