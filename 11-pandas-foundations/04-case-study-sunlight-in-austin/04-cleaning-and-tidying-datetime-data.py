'''
Cleaning and tidying datetime data

In order to use the full power of pandas time series, you must construct a DatetimeIndex. To do so, it is necessary to clean and transform the date and time columns.

The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.

Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.

INSTRUCTIONS
70XP
INSTRUCTIONS
70XP
Convert the 'date' column to a string with .astype(str) and assign to df_dropped['date'].
Add leading zeros to the 'Time' column. This has been done for you.
Concatenate the new 'date' and 'Time' columns together. Assign to date_string.
Convert the date_string Series to datetime values with pd.to_datetime(). Specify the format parameter.
Set the index of the df_dropped DataFrame to to be date_times. Assign the result to df_clean.
'''
# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date'] + df_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())