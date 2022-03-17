'''
Bee swarm plot
100xp
Make a bee swarm plot of the iris petal lengths. Your x-axis should contain each of the
three species, and the y-axis the petal lengths. A data frame containing the data is in
your namespace as df.

For your reference, the code Justin used to create the bee swarm plot in the video is
provided below:

_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')
plt.show()
In the IPython Shell, you can use sns.swarmplot? or help(sns.swarmplot) for more details
on how to make bee swarm plots using seaborn.

Instructions
-In the IPython Shell, inspect the DataFrame df using df.head(). This will let you identify
which column names you need to pass as the x and y keyword arguments in your call to sns.swarmplot().
-Use sns.swarmplot() to make a bee swarm plot from the DataFrame containing the Fisher iris
data set, df. The x-axis should contain each of the three species, and the y-axis should contain
the petal lengths.
-Label the axes.
-Show your plot.
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/iris.csv')

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
