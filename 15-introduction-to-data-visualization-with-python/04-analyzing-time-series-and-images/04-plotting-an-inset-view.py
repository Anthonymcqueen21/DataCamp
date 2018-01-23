'''
Plotting an inset view

Remember, rather than comparing plots with subplots or overlayed plots, you can generate an inset view directly using plt.axes(). In this exercise, you'll reproduce two of the time series plots from the preceding two exercises. Your figure will contain an inset plot to highlight the dramatic changes in AAPL stock price between November 2007 and April 2008 (as compared to the 11 years from 2001 to 2011).

INSTRUCTIONS
100XP
Extract a slice of series aapl from November 2007 to April 2008 inclusive. This has been done for you.
Plot the entire series aapl.
Create a set of axes with lower left corner (0.25, 0.5), width 0.35, and height 0.35. Pass these coordinates to plt.axes() as a list (all in units relative to the figure dimensions).
Plot the sliced view in the current axes in 'red'.
'''
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series 
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# Specify the axes
plt.axes([0.25,0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()
