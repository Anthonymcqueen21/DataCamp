'''
Sampling out of the Binomial distribution
100xp

Compute the probability mass function for the number of defaults we would expect
for 100 loans as in the last section, but instead of simulating all of the Bernoulli
trials, perform the sampling using np.random.binomial(). This is identical to the
calculation you did in the last set of exercises using your custom-written
perform_bernoulli_trials() function, but far more computationally efficient. Given
this extra efficiency, we will take 10,000 samples instead of 1000. After taking the
samples, plot the CDF as last time. This CDF that you are plotting is that of the
Binomial distribution.

Note: For this exercise and all going forward, the random number generator is pre-seeded
for you (with np.random.seed(42)) to save you typing that each time.

Instructions
-Draw samples out of the Binomial distribution using np.random.binomial(). You should use
parameters n = 100 and p = 0.05, and set the size keyword argument to 10000.
-Compute the CDF using your previously-written ecdf() function.
-Plot the CDF with axis labels. The x-axis here is the number of defaults out of 100 loans,
while the y-axis is the CDF.
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

# Compute CDF: x, y

x, y = ecdf(n_defaults)

# Plot the CDF with axis labels
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Defaults out of 100')
_ = plt.ylabel('CDF')

# Show the plot
plt.show()
