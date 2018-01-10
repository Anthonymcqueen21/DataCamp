'''
Median vs mean

In many data sets, there can be large differences in the mean and median value due to the presence of outliers.

In this exercise, you'll investigate the mean, median, and max fare prices paid by passengers on the Titanic and generate a box plot of the fare prices. This data set was obtained from Vanderbilt University.

All necessary modules have been imported and the DataFrame is available in the workspace as df.

INSTRUCTIONS
100XP
Print summary statistics of the 'fare' column of df with .describe() and print(). Note: df.fare and df['fare'] are equivalent.
Generate a box plot of the 'fare' column.
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/titanic.csv')

# Print summary statistics of the fare column with .describe()
print(df['fare'].describe())

# Generate a box plot of the fare column
df['fare'].plot(kind='box')

# Show the plot
plt.show()

