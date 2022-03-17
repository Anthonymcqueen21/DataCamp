'''
Using pandas to import flat files as DataFrames (2)
100xp

In the last exercise, you were able to import flat files into a pandas
DataFrame. As a bonus, it is then straightforward to retrieve the corresponding
numpy array using the attribute values. You'll now have a chance to do this using
the MNIST dataset, which is available as digits.csv.

Instructions
-Import the first 5 rows of the file into a DataFrame using the function pd.read_csv()
and assign the result to data. You'll need to use the arguments nrows and header
(there is no header in this file).
-Build a numpy array from the resulting DataFrame in data and assign to data_array.
-Execute print(type(data_array)) to print the datatype of data_array.
'''
import numpy as np
import pandas as pd

# Assign the filename: file
file = '../_datasets/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))
