'''
Setup the Engine and MetaData

In this exercise, your job is to create an engine to the database that will be used in this chapter. Then, you need to initialize its metadata.

Recall how you did this in Chapter 1 by leveraging create_engine() and MetaData.

INSTRUCTIONS
100XP
Import create_engine and MetaData from sqlalchemy.
Create an engine to the chapter 5 database by using 'sqlite:///chapter5.sqlite' as the connection string.
Create a MetaData object as metadata.
'''
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()
