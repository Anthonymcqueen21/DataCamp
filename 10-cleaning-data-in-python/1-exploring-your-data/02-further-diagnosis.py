'''
Further diagnosis

In the previous exercise, you identified some potentially unclean or missing data. Now, you'll
continue to diagnose your data with the very useful .info() method.

The .info() method provides important information about a DataFrame, such as the number of rows,
number of columns, number of non-missing values in each column, and the data type stored in each
column. This is the kind of information that will allow you to confirm whether the 'Initial Cost'
and 'Total Est. Fee' columns are numeric or strings. From the results, you'll also be able to see
whether or not all columns have complete data in them.

The full DataFrame df and the subset DataFrame df_subset have been pre-loaded. Your task is to use
the .info() method on these and analyze the results.

INSTRUCTIONS
50XP
-Print the info of df.
-Print the info of the subset dataframe, df_subset.
'''
# Print the info of df
print(df.info)

# Print the info of df_subset
print(df_subset.info)
