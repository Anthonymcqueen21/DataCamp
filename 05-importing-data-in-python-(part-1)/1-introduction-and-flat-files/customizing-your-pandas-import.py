'''
Customizing your pandas import
100xp

The pandas package is also great at dealing with many of the issues you will
encounter when importing data as a data scientist, such as comments occurring
in flat files, empty lines and missing values. Note that missing values are also
commonly referred to as NA or NaN. To wrap up this chapter, you're now going to
import a slightly corrupted copy of the Titanic dataset titanic_corrupt.txt, which

-contains comments after the character '#'
-is tab-delimited.

Instructions
-Complete the sep (the pandas version of delim), comment and na_values arguments of
pd.read_csv(). comment takes characters that comments occur after in the file, which
in this case is '#'. na_values takes a list of strings to recognize as NA/NaN, in
this case the string 'Nothing'.
-Execute the rest of the code to print the head of the resulting DataFrame and plot
the histogram of the 'Age' of passengers aboard the Titanic.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = '../_datasets/titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
