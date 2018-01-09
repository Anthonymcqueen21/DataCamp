'''
Loading and viewing your data

In this chapter, you're going to look at a subset of the Department of Buildings Job Application
Filings dataset from the NYC Open Data portal. This dataset consists of job applications filed on
January 22, 2017.

Your first task is to load this dataset into a DataFrame and then inspect it using the .head()
and .tail()
methods. However, you'll find out very quickly that the printed results don't allow you to see
everything you need, since there are too many columns. Therefore, you need to look at the data
in another way.

The .shape and .columns attributes let you see the shape of the DataFrame and obtain a list of
its columns. From here, you can see which columns are relevant to the questions you'd like to ask
of the data. To this end, a new DataFrame, df_subset, consisting only of these relevant columns,
has been pre-loaded. This is the DataFrame you'll work with in the rest of the chapter.

Get acquainted with the dataset now by exploring it with pandas! This initial exploratory analysis
is a crucial first step of data cleaning.

INSTRUCTIONS
50XP
Import pandas as pd.
-Read 'dob_job_application_filings_subset.csv' into a DataFrame called df.
-Print the head and tail of df.
-Print the shape of df and its columns. Note: .shape and .columns are attributes, not methods,
so you don't need to follow these with parentheses ().
-Hit 'Submit Answer' to view the results! Notice the suspicious number of 0 values. Perhaps these
represent missing data.
'''

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())
