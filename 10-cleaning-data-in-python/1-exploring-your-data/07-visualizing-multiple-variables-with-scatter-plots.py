'''
Visualizing multiple variables with scatter plots

Boxplots are great when you have a numeric column that you want to compare across different
categories. When you want to visualize two numeric columns, scatter plots are ideal.

In this exercise, your job is to make a scatter plot with 'initial_cost' on the x-axis and
the 'total_est_fee' on the y-axis. You can do this by using the DataFrame .plot() method with
kind='scatter'. You'll notice right away that there are 2 major outliers shown in the plots.

Since these outliers dominate the plot, an additional DataFrame, df_subset, has been provided,
in which some of the extreme values have been removed. After making a scatter plot using this,
you'll find some interesting patterns here that would not have been seen by looking at summary
statistics or 1 variable plots.

When you're done, you can cycle between the two plots by clicking the 'Previous Plot' and
'Next Plot' buttons below the plot.

INSTRUCTIONS
100XP
-Using df, create a scatter plot (kind='scatter') with 'initial_cost' on the x-axis and the
'total_est_fee' on the y-axis. Rotate the x-axis labels by 70 degrees.
-Create another scatter plot exactly as above, substituting df_subset in place of df.
'''
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
