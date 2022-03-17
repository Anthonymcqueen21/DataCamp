'''
The power of SQL lies in relationships between tables: INNER JOIN
100xp

Here, you'll perform your first INNER JOIN! You'll be working with your favourite
SQLite database, Chinook.sqlite. For each record in the Album table, you'll extract
the Title along with the Name of the Artist. The latter will come from the Artist
table and so you will need to INNER JOIN these two tables on the ArtistID column of both.

Recall that to INNER JOIN the Orders and Customers tables from the Northwind database,
Hugo executed the following SQL query:

"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID =
    Customers.CustomerID"

The following code has already been executed to import the necessary packages and to
create the engine:

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

Instructions
-Assign to rs the results from the following query: select all the records, extracting
the Title of the record and Name of the artist of each record from the Album table and
the Artist table, respectively. To do so, INNER JOIN these two tables on the ArtistID
column of both.
-In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all
records in rs. Store them in the DataFrame df.
-Set the DataFrame's column names to the corresponding names of the table columns.
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
