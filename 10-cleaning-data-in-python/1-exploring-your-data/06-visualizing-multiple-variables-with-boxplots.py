'''
Visualizing multiple variables with boxplots

Histograms are great ways of visualizing single variables. To visualize multiple variables,
boxplots are useful, especially when one of the variables is categorical.

In this exercise, your job is to use a boxplot to compare the 'initial_cost' across the
different values of the 'Borough' column. The pandas .boxplot() method is a quick way to do
this, in which you have to specify the column and by parameters. Here, you want to visualize
how 'initial_cost' varies by 'Borough'.

pandas and matplotlib.pyplot have been imported for you as pd and plt, respectively, and the
DataFrame has been pre-loaded as df.

INSTRUCTIONS
100XP
-Using the .boxplot() method of df, create a boxplot of 'initial_cost' across the different
values of 'Borough'.
-Display the plot.
'''
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()
