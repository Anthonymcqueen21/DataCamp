'''
Grouping on a function of the index

Groubpy operations can also be performed on transformations of the index values. In the case of a DateTimeIndex, we can extract portions of the datetime over which to group.

In this exercise you'll read in a set of sample sales data from February 2015 and assign the 'Date' column as the index. Your job is to group the sales data by the day of the week and aggregate the sum of the 'Units' column.

Is there a day of the week that is more popular for customers? To find out, you're going to use .strftime('%a') to transform the index datetime values to abbreviated days of the week.

The sales data CSV file is available to you as 'sales.csv'.

INSTRUCTIONS
70XP
Read 'sales.csv' into a DataFrame with index_col='Date' and parse_dates=True.
Create a groupby object with sales.index.strftime('%a') as input and assign it to by_day.
Aggregate the 'Units' column of by_day with the .sum() method. Save the result as units_sum.
Print units_sum. This has been done for you, so hit 'Submit Answer' to see the result.
'''
# Read file: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)
