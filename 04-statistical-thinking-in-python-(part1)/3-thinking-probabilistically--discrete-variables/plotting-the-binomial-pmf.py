'''
Plotting the Binomial PMF
100xp

As mentioned in the video, plotting a nice looking PMF requires a bit of matplotlib
trickery that we will not go into here. Instead, we will plot the PMF of the Binomial
distribution as a histogram with skills you have already learned. The trick is setting
up the edges of the bins to pass to plt.hist() via the bins keyword argument. We want
the bins centered on the integers. So, the edges of the bins should be -0.5, 0.5, 1.5,
2.5, ... up to max(n_defaults) + 1.5. You can generate an array like this using np.arange()
and then subtracting 0.5 from the array.

You have already sampled out of the Binomial distribution during your exercises on loan
defaults, and the resulting samples are in the NumPy array n_defaults.

Instructions
-Using np.arange(), compute the bin edges such that the bins are centered on the integers.
Store the resulting array in the variable bins.
-Use plt.hist() to plot the histogram of n_defaults with the normed=True and bins=bins
keyword arguments.
-Leave a 2% margin and label your axes.
-Show the plot.
'''
import numpy as np
import matplotlib.pyplot as plt


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y


# Seed random number generator
np.random.seed(42)

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n=100, p=0.05, size=10000)

# Compute bin edges: bins
bins = np.arange(min(n_defaults), max(n_defaults) + 1.5) - 0.5

# Generate histogram
_ = plt.hist(n_defaults, normed=True, bins=bins)

# Set margins
_ = plt.margins(0.02)

# Label axes
_ = plt.xlabel('x')
_ = plt.ylabel('y')

# Show the plot
plt.show()
