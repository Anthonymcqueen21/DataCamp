'''
The Normal PDF
100xp

In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF
of a known distribution using hacker statistics. Specifically, you will plot a Normal
PDF for various values of the variance.

Instructions
-Draw 100,000 samples from a Normal distribution that has a mean of 20 and a standard
deviation of 1. Do the same for Normal distributions with standard deviations of 3 and
10, each still with a mean of 20. Assign the results to samples_std1, samples_std3 and
samples_std10, respectively.
-Plot a histograms of each of the samples; for each, use 100 bins, also using the keyword
arguments normed=True and histtype='step'. The latter keyword argument makes the plot look
much like the smooth theoretical PDF. You will need to make 3 plt.hist() calls.
-Hit 'Submit Answer' to make a legend, showing which standard deviations you used, and show
your plot! There is no need to label the axes because we have not defined what is being
described by the Normal distribution; we are just looking at shapes of PDFs.
'''
import numpy as np
import matplotlib.pyplot as plt

# Seed random number generator
np.random.seed(42)

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3,
#   samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Make histograms
_ = plt.hist(samples_std1, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
