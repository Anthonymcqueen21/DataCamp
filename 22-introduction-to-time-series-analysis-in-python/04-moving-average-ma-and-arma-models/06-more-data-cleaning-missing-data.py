'''
More Data Cleaning: Missing Data

When you print out the length of the DataFrame intraday, you will notice that a few rows are missing. There will be missing data if there are no trades in a particular one-minute interval. One way to see which rows are missing is to take the difference of two sets: the full set of every minute and the set of the DataFrame index which contains missing rows. You can fill in the missing rows with the .reindex() method, convert the index to time of day, and then plot the data.

Stocks trade at discrete one-cent increments (although a small percentage of trades occur in between the one-cent increments) rather than at continuous prices, and when you plot the data you should observe that there are long periods when the stock bounces back and forth over a one cent range. This is sometimes referred to as "bid/ask bounce".

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Print out the length of intraday using len().
Find the missing rows by making range(391) into a set and subtracting the set of the intraday index, intraday.index.
Fill in the missing rows using the .reindex() method, setting the index equal to the full range(391) and forward filling the missing data by passing the argument method='ffill'.
Change the index to times using pandas function date_range(), starting with '2017-08-28 9:30' and ending with '2017-08-28 16:00' and passing the argument freq='1min'.
Plot the data and include gridlines.
'''
# Notice that some rows are missing
print("The length of the DataFrame is: ",len(intraday))

# Find the missing rows
print("Missing rows: ", set(range(391)) - set(intraday.index))

# Fill in the missing rows
intraday = intraday.reindex(range(391), method='ffill')

# Change the index to the intraday times
intraday.index = pd.date_range(start='2017-08-28 9:30', end='2017-08-28 16:00', freq='1min')

# Plot the intraday time series
intraday.plot(grid=True)
plt.show()
