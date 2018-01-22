'''
Creating Tables with SQLAlchemy

Previously, you used the Table object to reflect a table from an existing database, but what if you wanted to create a new table? You'd still use the Table object; however, you'd need to replace the autoload and autoload_with parameters with Column objects.

The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints.

When defining the table, recall how in the video Jason passed in 255 as the maximum length of a String by using Column('name', String(255)). Checking out the slides from the video may help: you can dowload them by clicking on 'Slides' next to the IPython Shell.

After defining the table, you can create the table in the database by using the .create_all() method on metadata and supplying the engine as the only parameter. Go for it!

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
Create the table in the database by passing engine to metadata.create_all().
'''
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))
