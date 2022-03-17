'''
The Normal CDF
100xp
Now that you have a feel for how the Normal PDF looks, let's consider its CDF. Using the
samples you generated in the last exercise (in your namespace as samples_std1, samples_std3,
and samples_std10), generate and plot the CDFs.

Instructions
-Use your ecdf() function to generate x and y values for CDFs: x_std1, y_std1, x_std3, y_std3
and x_std10, y_std10, respectively.
-Plot all three CDFs as dots (do not forget the marker and linestyle keyword arguments!).
-Make a 2% margin in your plot.
-Hit submit to make a legend, showing which standard deviations you used, and to show your plot.
There is no need to label the axes because we have not defined what is being described by the Normal distribution; we are just looking at shapes of CDFs.
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
    y = np.arange(1, n+1) / n

    return x, y

# Seed random number generator
np.random.seed(42)

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3,
#   samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
_ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
_ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')

# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
