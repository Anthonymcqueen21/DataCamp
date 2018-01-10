'''
Method chaining and filtering

We've seen that pandas supports method chaining. This technique can be very powerful when cleaning and filtering data.

In this exercise, a DataFrame containing flight departure data for a single airline and a single airport for the month of July 2015 has been pre-loaded. Your job is to use .str() filtering and method chaining to generate summary statistics on flight delays each day to Dallas.

INSTRUCTIONS
100XP
Use .str.strip() to strip extra whitespace from df.columns. Assign the result back to df.columns.
In the 'Destination Airport' column, extract all entries where Dallas ('DAL') is the destination airport. Use .str.contains('DAL') for this and store the result in dallas.
Resample dallas such that you get the total number of departures each day. Store the result in daily_departures.
Generate summary statistics for daily Dallas departures using .describe(). Store the result in stats.
'''
import pandas as pd

df = pd.read_csv('../_datasets/austin_airport_departure_data_2015_july.csv')

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip(' ')

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

