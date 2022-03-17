'''
Using pandas to import flat files as DataFrames (1)
100xp

In the last exercise, you were able to import flat files containing columns with
different datatypes as numpy arrays. However, the DataFrame object in pandas is a
more appropriate structure in which to store such data and, thankfully, we can easily
import files of mixed data types as DataFrames using the pandas functions read_csv()
and read_table().

Instructions
-Import the pandas package using the alias pd.
-Read titanic.csv into a DataFrame called df. The file name is already stored in
the file object.
-In a print() call, view the head of the DataFrame.
'''
# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = '../_datasets/titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
