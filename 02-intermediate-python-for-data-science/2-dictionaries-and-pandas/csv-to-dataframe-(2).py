'''
CSV to DataFrame (2)
100xp
Your read_csv() call to import the CSV data didn't generate an error, but the
output is not entirely what we wanted. The row labels were imported as another
column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which
column in the CSV file should be used as a row label? Well, that's exactly what
you need here!

Python code that solves the previous exercise is already included; can you make
the appropriate changes to fix the data import?

Instructions
-Run the code with Submit Answer and assert that the first column should actually
be used as row labels.
-Specify the index_col argument inside pd.read_csv(): set it to 0, so that the
first column is used as row labels.
-Has the printout of cars improved now?
'''
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)
