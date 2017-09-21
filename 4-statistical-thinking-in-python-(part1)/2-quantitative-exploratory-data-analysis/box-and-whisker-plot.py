'''
Box-and-whisker plot
100xp

Making a box plot for the petal lengths is unnecessary because the iris data set is
not too large and the bee swarm plot works fine. However, it is always good to get
some practice. Make a box plot of the iris petal lengths. You have a pandas DataFrame,
df, which contains the petal length data, in your namespace. Inspect the data frame df
in the IPython shell using df.head() to make sure you know what the pertinent columns are.

For your reference, the code used to produce the box plot in the video is provided below:

_ = sns.boxplot(x='east_west', y='dem_share', data=df_all_states)

_ = plt.xlabel('region')

_ = plt.ylabel('percent of vote for Obama')

In the IPython Shell, you can use sns.boxplot? or help(sns.boxplot) for more details on
how to make box plots using seaborn.

Instructions
-The set-up is exactly the same as for the bee swarm plot; you just call sns.boxplot()
with the same keyword arguments as you would sns.swarmplot(). The x-axis is 'species'
and y-axis is 'petal length (cm)'.
-Don't forget to label your axes!
-Display the figure using the normal call.
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/iris.csv')

# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
