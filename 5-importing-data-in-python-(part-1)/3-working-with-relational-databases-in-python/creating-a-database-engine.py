'''
Creating a database engine
100xp
Here, you're going to fire up your very first SQL engine. You'll create an engine to
connect to the SQLite database 'Chinook.sqlite', which is in your working directory.
Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command

engine = create_engine('sqlite:///Northwind.sqlite')
Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database
Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database
contains information about a semi-fictional digital media store in which media data is
real and customer, employee and sales data has been manually created.

Why the name Chinook, you ask? According to their website,

The name of this sample database was based on the Northwind database. Chinooks are winds
in the interior West of North America, where the Canadian Prairies and Great Plains meet
various mountain ranges. Chinooks are most prevalent over southern Alberta in Canada.
Chinook is a good name choice for a database that intends to be an alternative to Northwind.

Instructions
-Import the function create_engine from the module sqlalchemy.
-Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
'''
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')
