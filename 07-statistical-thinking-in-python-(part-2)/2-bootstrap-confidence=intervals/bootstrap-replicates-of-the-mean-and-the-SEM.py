'''
Bootstrap replicates of the mean and the SEM

In this exercise, you will compute a bootstrap estimate of the probability distribution function of the
mean annual rainfall at the Sheffield Weather Station. Remember, we are estimating the mean annual rainfall 
we would get if the Sheffield Weather Station could repeat all of the measurements from 1883 to 2015 over
and over again. This is a probabilistic estimate of the mean. You will plot the PDF as a histogram, and 
you will see that it is Normal.

In fact, it can be shown theoretically that under not-too-restrictive conditions, the value of the 
mean will always be Normally distributed. (This does not hold in general, just for the mean and a 
few other statistics.) The standard deviation of this distribution, called the standard error of the 
mean, or SEM, is given by the standard deviation of the data divided by the square root of the number 
of data points. I.e., for a data set, sem = np.std(data) / np.sqrt(len(data)). Using hacker statistics,
you get this same result without the need to derive it, but you will verify this result from your
bootstrap replicates.

The dataset has been pre-loaded for you into an array called rainfall.

INSTRUCTIONS
100XP
-Draw 10000 bootstrap replicates of the mean annual rainfall using your draw_bs_reps() function and the
rainfall array. Hint: Pass in np.mean for func to compute the mean.
-As a reminder, draw_bs_reps() accepts 3 arguments: data, func, and size.
-Compute and print the standard error of the mean of rainfall.
-The formula to compute this is np.std(data) / np.sqrt(len(data)).
-Compute and print the standard deviation of your bootstrap replicates bs_replicates.
-Make a histogram of the replicates using the normed=True keyword argument and 50 bins.
-Hit 'Submit Answer' to see the plot!
'''
import matplotlib.pyplot as plt
import numpy as np


def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates

# Take 10,000 bootstrap replicates of the mean: bs_replicates
bs_replicates = draw_bs_reps(rainfall, np.mean, size=10000)

# Compute and print SEM
sem = np.std(rainfall) / np.sqrt(len(rainfall))
print(sem)

# Compute and print standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('mean annual rainfall (mm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
