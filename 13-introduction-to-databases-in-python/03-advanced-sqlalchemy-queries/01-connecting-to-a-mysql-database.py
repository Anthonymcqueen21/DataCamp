'''
Connecting to a MySQL Database

Before you jump into the calculation exercises, let's begin by connecting to our database. Recall that in the last chapter you connected to a PostgreSQL database. Now, you'll connect to a MySQL database, for which many prefer to use the pymysql database driver, which, like psycopg2 for PostgreSQL, you have to install prior to use.

This connection string is going to start with 'mysql+pymysql://', indicating which dialect and driver you're using to establish the connection. The dialect block is followed by the 'username:password' combo. Next, you specify the host and port with the following '@host:port/'. Finally, you wrap up the connection string with the 'database_name'.

Now you'll practice connecting to a MySQL database: it will be the same census database that you have already been working with. One of the great things about SQLAlchemy is that, after connecting, it abstracts over the type of database it has connected to and you can write the same SQLAlchemy code, regardless!

INSTRUCTIONS
100XP
Import the create_engine function from the sqlalchemy library.
Create an engine to the census database by concatenating the following strings and passing them to create_engine():
'mysql+pymysql://' (the dialect and driver).
'student:datacamp' (the username and password).
'@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/' (the host and port).
'census' (the database name).
Use the .table_names() method on engine to print the table names.
'''
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Print the table names
print(engine.table_names())
