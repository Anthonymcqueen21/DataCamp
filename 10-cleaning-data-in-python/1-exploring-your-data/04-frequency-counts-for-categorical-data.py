'''
Frequency counts for categorical data

As you've seen, .describe() can only be used on numeric columns. So how can you diagnose
data issues when you have categorical data? One way is by using the .value_counts() method,
which returns the frequency counts for each unique value in a column!

This method also has an optional parameter called dropna which is True by default. What this
means is if you have missing data in a column, it will not give a frequency count of them. You want to set the dropna column to False so if there are missing values in a column, it will give you the frequency counts.

In this exercise, you're going to look at the 'Borough', 'State', and 'Site Fill' columns
to make sure all the values in there are valid. When looking at the output, do a sanity
check: Are all values in the 'State' column from NY, for example? Since the dataset consists
of applications filed in NY, you would expect this to be the case.

INSTRUCTIONS
100XP
Print the value counts for:
-The 'Borough' column.
-The 'State' column.
-The 'Site Fill' column.
'''
import pandas as pd

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))
