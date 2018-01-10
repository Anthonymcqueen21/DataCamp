'''
Bachelor's degrees awarded to women

In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.

Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of the mean value of all 17 academic fields per year. To perform this step, you'll use the .mean() method with the keyword argument axis='columns'. This computes the mean across all columns per row.

The DataFrame has been pre-loaded for you as df with the index set to 'Year'.

INSTRUCTIONS
100XP
-Print the minimum value of the 'Engineering' column.
-Print the maximum value of the 'Engineering' column.
-Construct the mean percentage per year with .mean(axis='columns'). Assign the result to mean.
-Plot the average percentage per year. Since 'Year' is the index of df, it will appear on the x-axis of the plot. No keyword arguments are needed in your call to .plot().
'''
import pandas as pd

df = pd.read_csv('../_datasets/percent-bachelors-degrees-women-usa.csv')

# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()
df.plot()

# Display the plot
plt.show()

