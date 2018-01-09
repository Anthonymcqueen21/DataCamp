'''
Comparing percentiles to ECDF
100xp
To see how the percentiles relate to the ECDF, you will plot the percentiles of
Iris versicolor petal lengths you calculated in the last exercise on the ECDF plot
you generated in chapter 1. The percentile variables from the previous exercise are
available in the workspace as ptiles_vers and percentiles.

Note that to ensure the Y-axis of the ECDF plot remains between 0 and 1, you will need
to rescale the percentiles array accordingly - in this case, dividing it by 100.

Instructions
-Plot the percentiles as red diamonds on the ECDF. Pass the x and y co-ordinates - ptiles_vers
and percentiles/100 - as positional arguments and specify the marker='D', color='red' and
linestyle='none' keyword arguments. The argument for the y-axis - percentiles/100 has been
specified for you.
-Display the plot.
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ptiles_vers = np.array([3.3, 4., 4.35, 4.6, 4.9775])

x_vers = np.array([3.,  3.3,  3.3,  3.5,  3.5,  3.6,  3.7,  3.8,  3.9,  3.9,  3.9,
                   4.,  4.,  4.,  4.,  4.,  4.1,  4.1,  4.1,  4.2,  4.2,  4.2,
                   4.2,  4.3,  4.3,  4.4,  4.4,  4.4,  4.4,  4.5,  4.5,  4.5,  4.5,
                   4.5,  4.5,  4.5,  4.6,  4.6,  4.6,  4.7,  4.7,  4.7,  4.7,  4.7,
                   4.8,  4.8,  4.9,  4.9,  5.,  5.1])

y_vers = np.array([0.02,  0.04,  0.06,  0.08,  0.1,  0.12,  0.14,  0.16,  0.18,
                   0.2,  0.22,  0.24,  0.26,  0.28,  0.3,  0.32,  0.34,  0.36,
                   0.38,  0.4,  0.42,  0.44,  0.46,  0.48,  0.5,  0.52,  0.54,
                   0.56,  0.58,  0.6,  0.62,  0.64,  0.66,  0.68,  0.7,  0.72,
                   0.74,  0.76,  0.78,  0.8,  0.82,  0.84,  0.86,  0.88,  0.9,
                   0.92,  0.94,  0.96,  0.98,  1.])

percentiles = np.array([2.5,  25.,  50.,  75.,  97.5])

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles / 100, marker='D', color='red',
             linestyle='none')

# Show the plot
plt.show()
