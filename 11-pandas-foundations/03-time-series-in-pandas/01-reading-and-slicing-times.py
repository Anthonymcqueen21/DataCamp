'''
Reading and slicing times

For this exercise, we have read in the same data file using three different approaches:

df1 = pd.read_csv(filename)

df2 = pd.read_csv(filename, parse_dates=['Date'])

df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)

Use the .head() and .info() methods in the IPython Shell to inspect the DataFrames. Then, try to index each DataFrame with a datetime string. Which of the resulting DataFrames allows you to easily index and slice data by dates using, for example, df1.loc['2010-Aug-01']?

INSTRUCTIONS
50XP
Possible Answers
df1.
press 1

df1 and df2.
press 2

df2.
press 3

df2 and df3.
press 4

df3.
press 5
'''
df3