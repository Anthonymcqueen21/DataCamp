'''
Visualizing single variables with histograms

Up until now, you've been looking at descriptive statistics of your data. One of the best
ways to confirm what the numbers are telling you is to plot and visualize the data.

You'll start by visualizing single variables using a histogram for numeric values. The column
you will work on in this exercise is 'Existing Zoning Sqft'.

The .plot() method allows you to create a plot of each column of a DataFrame. The kind parameter
allows you to specify the type of plot to use - kind='hist', for example, plots a histogram.

In the IPython Shell, begin by computing summary statistics for the 'Existing Zoning Sqft'
column using the .describe() method. You'll notice that there are extremely large differences
between the min and max values, and the plot will need to be adjusted accordingly. In such cases,
it's good to look at the plot on a log scale. The keyword arguments logx=True or logy=True can be
passed in to .plot() depending on which axis you want to rescale.

Finally, note that Python will render a plot such that the axis will hold all the information.
That is, if you end up with large amounts of whitespace in your plot, it indicates counts or
values too small to render.

INSTRUCTIONS
100XP
-Import matplotlib.pyplot as plt.
-Create a histogram of the 'Existing Zoning Sqft' column. Rotate the axis labels by 70 degrees
and use a log scale for both axes.
-Display the histogram using plt.show().
'''
import pandas as pd

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()





