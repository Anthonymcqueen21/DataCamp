'''
Separate and plot

Population filtering can be used alongside plotting to quickly determine differences in distributions between the sub-populations. You'll work with the Titanic dataset.

There were three passenger classes on the Titanic, and passengers in each class paid a different fare price. In this exercise, you'll investigate the differences in these fare prices.

Your job is to use Boolean filtering and generate box plots of the fare prices for each of the three passenger classes. The fare prices are contained in the 'fare' column and passenger class information is contained in the 'pclass' column.

When you're done, notice the portions of the box plots that differ and those that are similar.

The DataFrame has been pre-loaded for you as titanic.

INSTRUCTIONS
100XP
-Inside plt.subplots(), specify the nrows and ncols parameters so that there are 3 rows and 1 column.
-Filter the rows where the 'pclass' column has the values 1 and generate a box plot of the 'fare' column.
-Filter the rows where the 'pclass' column has the values 2 and generate a box plot of the 'fare' column.
-Filter the rows where the 'pclass' column has the values 3 and generate a box plot of the 'fare' column.
'''
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('../_datasets/titanic.csv')

# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()
