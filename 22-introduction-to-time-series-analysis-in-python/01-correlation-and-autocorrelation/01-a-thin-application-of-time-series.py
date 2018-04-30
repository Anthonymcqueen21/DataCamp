'''
A "Thin" Application of Time Series

Google Trends allows users to see how often a term is searched for. We downloaded a file from Google Trends containing the frequency over time for the search word "diet", which is pre-loaded in a DataFrame called diet. A first step when analyzing a time series is to visualize the data with a plot. You should be able to clearly see a gradual decrease in searches for "diet" throughout the calendar year, hitting a low around the December holidays, followed by a spike in searches around the new year as people make New Year's resolutions to lose weight.

Like many time series datasets you will be working with, the index of dates are strings and should be converted to a datetime index before plotting.

INSTRUCTIONS
100XP
Convert the date index to datetime using pd.to_datetime().
Use the .plot() method with slicing to plot data for only 2012.
Plot the entire time series and set the argument grid=True to better see the year-ends.
'''
# Import pandas and plotting modules
import pandas as pd
import matplotlib.pyplot as plt

# Convert the date index to datetime
diet.index = pd.to_datetime(diet.index)

# Plot 2012 data using slicing
diet['2012'].plot()
plt.show()

# Plot the entire time series diet and show gridlines
diet.plot(grid=True)
plt.show()