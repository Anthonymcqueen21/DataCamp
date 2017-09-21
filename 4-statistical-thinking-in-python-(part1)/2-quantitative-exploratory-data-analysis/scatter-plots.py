'''
Scatter plots
100xp

When you made bee swarm plots, box plots, and ECDF plots in previous exercises,
you compared the petal lengths of different species of iris. But what if you want
to compare two properties of a single species? This is exactly what we will do in
this exercise. We will make a scatter plot of the petal length and width measurements
of Anderson's Iris versicolor flowers. If the flower scales (that is, it preserves its
proportion as it grows), we would expect the length and width to be correlated.

For your reference, the code used to produce the scatter plot in the video is provided below:

_ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')

_ = plt.xlabel('total votes (thousands)')

_ = plt.ylabel('percent of vote for Obama')

Instructions
-Use plt.plot() with the appropriate keyword arguments to make a scatter plot of versicolor
petal length (x-axis) versus petal width (y-axis). The variables versicolor_petal_length and
versicolor_petal_width are already in your namespace. Do not forget to use the marker='.'
and linestyle='none' keyword arguments.
-Specify 2% margins so no data are cut off.
-Label the axes.
-Display the plot.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

versicolor_petal_length = np.array([4.7,  4.5,  4.9,  4.,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
                                    4.2,  4.,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4.,
                                    4.9,  4.7,  4.3,  4.4,  4.8,  5.,  4.5,  3.5,  3.8,  3.7,  3.9,
                                    5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4.,  4.4,  4.6,  4.,  3.3,
                                    4.2,  4.2,  4.2,  4.3,  3.,  4.1])

versicolor_petal_width = np.array([1.4,  1.5,  1.5,  1.3,  1.5,  1.3,  1.6,  1.,  1.3,  1.4,  1.,
                                   1.5,  1.,  1.4,  1.3,  1.4,  1.5,  1.,  1.5,  1.1,  1.8,  1.3,
                                   1.5,  1.2,  1.3,  1.4,  1.4,  1.7,  1.5,  1.,  1.1,  1.,  1.2,
                                   1.6,  1.5,  1.6,  1.5,  1.3,  1.3,  1.3,  1.2,  1.4,  1.2,  1.,
                                   1.3,  1.2,  1.3,  1.3,  1.1,  1.3])

# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width,
             marker='.', linestyle='none')


# Set margins
_ = plt.margins(0.02)

# Label the axes
_ = plt.xlabel('versicolor petal length')
_ = plt.ylabel('versicolor petal width')


# Show the result
plt.show()
