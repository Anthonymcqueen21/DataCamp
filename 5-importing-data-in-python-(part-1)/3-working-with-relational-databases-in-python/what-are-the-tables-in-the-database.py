'''
What are the tables in the database?
100xp

In this exercise, you'll once again create an engine to connect to 'Chinook.sqlite'.
Before you can get any data out of the database, however, you'll need to know what
tables it contains!

To this end, you'll save the table names to a list using the method table_names() on
the engine and then you will print the list.

Instructions
-Import the function create_engine from the module sqlalchemy.
-Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it
to engine.
-Using the method table_names() on the engine engine, assign the table names of
'Chinook.sqlite' to the variable table_names.
-Print the object table_names to the shell.
'''
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
