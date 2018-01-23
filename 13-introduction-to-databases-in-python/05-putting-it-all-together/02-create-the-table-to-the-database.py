'''
Create the Table to the Database

Having setup the engine and initialized the metadata, you will now define the census table object and then create it in the database using using the metadata and engine from the previous exercise. To create it in the database, you will have to use the .create_all() method on the metadata with engine as the argument.

It may help to refer back to the Chapter 4 exercise in which you learned how to create a table.

INSTRUCTIONS
100XP
Import Table, Column, String, and Integer from sqlalchemy.
Define a census table with the following columns:
'state' - String - length of 30
'sex' - String - length of 1
'age' - Integer
'pop2000' - Integer
'pop2008' - Integer
Create the table in the database using the metadata and engine.
'''
# Import Table, Column, String, and Integer
from sqlalchemy import (Table, Column, String, Integer)

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)
