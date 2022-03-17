'''
Re-assigning column names

After the initial step of reading in the data, the next step is to clean and tidy it so that it is easier to work with.

In this exercise, you will begin this cleaning process by re-assigning column names and dropping unnecessary columns.

pandas has been imported in the workspace as pd, and the file NOAA_QCLCD_2011_hourly_13904.txt has been parsed and loaded into a DataFrame df. The comma separated string of column names, column_labels, and list of columns to drop, list_to_drop, have also been loaded for you.

INSTRUCTIONS
100XP
-Convert the comma separated string column_labels to a list of strings using .split(','). Assign the result to column_labels_list.
-Reassign df.columns using the list of strings column_labels_list.
-Call df.drop() with list_to_drop and axis='columns'. Assign the result to df_dropped.
-Print df_dropped.head() to examine the result. This has already been done for you.
'''
# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop, axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())
