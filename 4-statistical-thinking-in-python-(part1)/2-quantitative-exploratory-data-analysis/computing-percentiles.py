'''
Computing percentiles
100xp
In this exercise, you will compute the percentiles of petal length of Iris versicolor.

Instructions
-Create percentiles, a NumPy array of percentiles you want to compute. These are the 2.5th,
25th, 50th, 75th, and 97.5th. You can do so by creating a list containing these ints/floats
and convert the list to a NumPy array using np.array(). For example, np.array([30, 50]) would
create an array consisting of the 30th and 50th percentiles.
-Use np.percentile() to compute the percentiles of the petal lengths from the Iris versicolor
samples. The variable versicolor_petal_length is in your namespace.
-Print the percentiles.
'''

import numpy as np
import seaborn as sns

versicolor_petal_length = np.array([4.7,  4.5,  4.9,  4.,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
                                    4.2,  4.,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4.,
                                    4.9,  4.7,  4.3,  4.4,  4.8,  5.,  4.5,  3.5,  3.8,  3.7,  3.9,
                                    5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4.,  4.4,  4.6,  4.,  3.3,
                                    4.2,  4.2,  4.2,  4.3,  3.,  4.1])

# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)
