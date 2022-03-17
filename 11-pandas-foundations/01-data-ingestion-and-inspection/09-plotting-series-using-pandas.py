'''
Plotting series using pandas

Data visualization is often a very effective first step in gaining a rough understanding of a data set to be analyzed. Pandas provides data visualization by both depending upon and interoperating with the matplotlib library. You will now explore some of the basic plotting mechanics with pandas as well as related matplotlib options. We have pre-loaded a pandas DataFrame df which contain the data you need. Your job is to use the DataFrame method df.plot() to visualize the data, and then explore the optional matplotlib input parameters that this .plot() method accepts.

The pandas .plot() method makes calls to matplotlib to construct the plots. This means that you can use the skills you've learned in previous visualization courses to customize the plot. In this exercise, you'll add a custom title and axis labels to the figure.

Before plotting, inspect the DataFrame in the IPython Shell using df.head(). Also, use type(df) and note that it is a single column DataFrame.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Create the plot with the DataFrame method df.plot(). Specify a color of 'red'.
    -Note: c and color are interchangeable as parameters here, but we ask you to be explicit and specify color.
-Use plt.title() to give the plot a title of 'Temperature in Austin'.
-Use plt.xlabel() to give the plot an x-axis label of 'Hours since midnight August 1, 2010'.
-Use plt.ylabel() to give the plot a y-axis label of 'Temperature (degrees F)'.
-Finally, display the plot using plt.show().
'''
# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

