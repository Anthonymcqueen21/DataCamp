'''
Multiple time series on common axes

For this exercise, you will construct a plot showing four time series stocks on the same axes. The time series in question are represented in the session using the identifiers aapl, ibm, csco, and msft. You'll generate a single plot showing all the time series on common axes with a legend.

INSTRUCTIONS
100XP
Plot the aapl time series in blue with a label of 'AAPL'.
Plot the ibm time series in green with a label of 'IBM'.
Plot the csco time series in red with a label of 'CSCO'.
Plot the msft time series in magenta with a label of 'MSFT'.
Specify a rotation of 60 for the xticks with plt.xticks().
Add a legend in the 'upper left' corner of the plot.
'''
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the aapl time series in blue
plt.plot(aapl, color='blue', label='AAPL')

# Plot the ibm time series in green
plt.plot(ibm, color='green', label='IBM')

# Plot the csco time series in red
plt.plot(csco, color='red', label='CSCO')

# Plot the msft time series in magenta
plt.plot(msft, color='magenta', label='MSFT')

# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')

# Specify the orientation of the xticks
plt.xticks(rotation=60)

# Display the plot
plt.show()
