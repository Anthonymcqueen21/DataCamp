'''
Importing Stata files
100xp

Here, you'll gain expertise in importing Stata files as DataFrames using
the pd.read_stata() function from pandas. The last exercise's file,
'disarea.dta', is still in your working directory.

Instructions
-Use pd.read_stata() to load the file 'disarea.dta' into the DataFrame df.
-Print the head of the DataFrame df.
-Visualize your results by plotting a histogram of the column disa10.
We’ve already provided this code for you, so just run it!
'''
import matplotlib.pyplot as plt

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('../_datasets/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()
