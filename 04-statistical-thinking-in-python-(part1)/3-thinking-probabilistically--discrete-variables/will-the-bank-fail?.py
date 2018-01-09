'''
Will the bank fail?
100xp
Plot the number of defaults you got from the previous exercise, in your namespace
as n_defaults, as a CDF. The ecdf() function you wrote in the first chapter is available.

If interest rates are such that the bank will lose money if 10 or more of its loans are
defaulted upon, what is the probability that the bank will lose money?

Instructions
-Compute the x and y values for the ECDF of n_defaults.
-Plot the ECDF, making sure to label the axes. Remember to include marker = '.' and
linestyle = 'none' in addition to x and y in your call plt.plot().
-Show the plot.
-Compute the total number of entries in your n_defaults array that were greater than or
equal to 10. To do so, compute a boolean array that tells you whether a given entry of
n_defaults is >= 10. Then sum all the entries in this array using np.sum(). For example,
np.sum(n_defaults <= 5) would compute the number of defaults with 5 or fewer defaults.
-The probability that the bank loses money is the fraction of n_defaults that are greater
than or equal to 10. Print this result by hitting 'Submit Answer'!
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


n_defaults = np.array([6,  5,  7,  8,  5,  5,  3,  2,  7,  6,  7,  3,  8,  3,  8,  5,  2,
                       6,  4,  5,  3,  2,  9,  5,  5,  3,  8,  7,  7,  5,  4,  3,  4,  5,
                       6,  1,  8,  4,  2,  9,  6,  5,  2,  6,  3,  6,  2,  6,  4,  4,  6,
                       4,  5,  4,  3,  4,  6,  3,  4,  8,  2,  4,  1,  6,  6,  6,  2,  2,
                       3,  8,  7,  2,  6,  6,  3,  6,  3, 10,  7,  6,  4,  5,  8,  4,  6,
                       4,  6,  1, 10,  4,  4,  4,  5,  4,  5,  2,  8,  7,  3,  7,  9,  6,
                       8,  2,  5,  4,  3,  6,  2,  6,  9,  5,  6,  6,  4,  4,  7,  6,  6,
                       7,  1,  5,  4,  1,  4,  6,  3,  2,  3,  8,  8,  6,  7,  6,  4,  4,
                       7,  2,  4,  7,  5,  4,  6,  6,  8,  4,  2,  5,  6,  3,  7,  6,  5,
                       10,  4,  4,  5,  7,  7,  6,  6,  4,  6,  9,  4,  4,  7,  4,  8,  5,
                       4,  3,  3,  6,  6,  1,  5,  7,  3,  7,  3,  4,  4,  3,  2,  2,  0,
                       7,  3,  7,  7,  3,  8,  6,  4,  3,  4,  4,  5,  2,  4,  4,  3,  7,
                       3,  6,  4,  2,  6,  6,  6,  7,  6,  4,  6,  6,  7,  8,  7,  3,  3,
                       3,  4,  7,  6,  5,  3,  6,  4,  2,  3,  2,  4,  6,  3,  4,  5,  1,
                       3,  6,  3,  6,  1,  6,  6,  7,  4,  7,  7,  4,  2,  8,  6,  3,  7,
                       3,  4,  4,  5,  1,  7,  1,  5,  3,  4,  8,  9,  3,  9,  8,  4,  0,
                       11,  7,  6,  7,  6,  7,  4,  5,  4,  5,  3,  6,  3,  3,  2,  5,  4,
                       6,  4,  3, 14,  5,  8,  1,  1,  4,  4,  4,  6,  4,  5,  3,  5,  6,
                       4,  5,  6,  3,  3,  8,  4,  1,  8,  5,  7,  5,  3,  2,  8,  4,  5,
                       4,  5,  8,  4,  2,  4,  3,  2,  9,  5,  6,  6,  3,  5,  8,  6,  4,
                       5,  1,  5,  8,  6,  5,  5, 10,  1,  0,  2,  3,  6, 10,  1,  6,  7,
                       5,  6, 13,  6,  4,  3,  3,  6,  3,  6,  3,  8,  4,  4,  6,  3,  5,
                       5,  1,  5,  7,  8,  9,  5,  7,  7,  6,  5,  7,  6,  2,  6,  4,  5,
                       6,  6,  2, 15,  8,  3,  5,  5,  6,  4,  4,  4,  2,  6,  7,  5,  3,
                       6,  7,  4,  2,  4,  7,  4,  5,  3,  8,  5,  3,  2,  8,  2,  4,  6,
                       3,  5,  1,  2,  5,  5,  4,  5,  5,  4,  7,  7,  4,  7,  6,  5,  6,
                       8,  5,  5,  4,  4,  1,  4,  3,  2,  4,  2,  6,  4,  6,  1,  6,  5,
                       5,  8,  7,  6,  3,  7,  6,  9,  5,  6,  1,  6,  6,  5,  6,  6,  5,
                       6,  2,  7,  4,  3, 13,  6,  7,  3,  4,  2,  8,  6,  5,  6,  4,  3,
                       7,  6,  4,  6,  6,  6,  6,  3,  7,  3,  7,  6,  2,  4,  4,  8,  6,
                       8,  4,  4,  5,  6,  7,  2,  8,  1,  6,  3,  9,  7,  1,  2,  7,  5,
                       4,  5, 11,  4,  3,  4,  7,  5,  7,  9,  4,  7,  7,  4,  7,  8,  4,
                       2,  7,  5,  3, 10,  3,  4,  4,  2,  2,  7,  3,  6,  7,  6,  6,  2,
                       2,  5,  7,  7,  6,  5,  3, 10,  6,  4,  4,  4,  4,  2,  6,  5,  7,
                       4,  5,  3,  8,  4,  2, 15,  3,  7,  9,  6,  3,  3,  3,  2,  3,  8,
                       8,  3,  8,  7,  3,  2,  8,  3,  5,  7,  1,  6,  5,  2,  4,  5,  2,
                       4,  4,  2,  5,  0,  6,  8,  5,  6,  3,  6,  5,  7,  3,  3,  4,  5,
                       7,  1,  6,  5,  7,  6,  6,  7,  2,  6,  3,  6,  4,  5,  5,  5,  7,
                       8,  3,  5,  4,  3,  8,  7,  3,  6,  4,  7,  4,  5,  4,  6,  1,  2,
                       2,  6,  3,  4,  7,  1,  7,  5,  6,  3,  7,  2, 10,  5,  3,  9,  7,
                       8,  2,  4,  5,  6,  5,  6,  5,  3,  4,  6,  8, 10,  7,  2,  3,  4,
                       5,  2,  5,  6,  6, 11,  4,  8,  4,  2,  4,  7,  3,  5,  1,  6,  4,
                       2,  5,  3,  3,  3,  3,  4,  3,  6,  6,  7,  6,  5,  6,  6,  9,  1,
                       2,  4,  4,  6,  8,  6,  4,  5,  5,  6,  6,  9,  4,  6,  3,  3,  6,
                       3,  2,  4,  6,  3,  6,  5,  6,  8,  5,  2,  4,  6,  7,  7,  9,  8,
                       4,  5,  3,  1,  4,  6,  1,  6,  2,  3,  5,  5,  3,  4,  6,  4,  5,
                       4,  7,  6,  3,  2,  4,  7,  6,  3,  4,  2,  5,  6,  7,  4,  8,  3,
                       3, 10,  3,  2,  5,  4,  5,  6,  6,  5,  2,  5,  2,  4,  6,  8,  4,
                       3,  6,  2,  1,  6,  3,  5,  9,  6,  2,  9,  4,  4,  6,  4,  5,  7,
                       5,  7,  4,  8,  4,  4,  4,  4,  7,  3,  7,  8,  2,  6,  2,  7,  7,
                       4,  3,  7,  9,  5,  5,  7,  4,  5,  3,  7,  7,  4,  3,  3,  3,  6,
                       5,  6,  8,  2,  9,  9,  4,  7,  8,  3,  4,  4,  7,  4,  2,  6,  8,
                       5,  6,  5,  3,  6,  9,  3,  1,  6,  4,  4,  3,  5,  5,  5, 12,  5,
                       10, 11,  3,  9,  3,  7,  5,  5,  5,  4,  5,  8,  9,  6,  6,  4,  6,
                       4,  6,  3,  6,  7,  5,  4,  2,  4,  6,  2,  3,  4,  6,  6,  1,  3,
                       7,  3,  7,  3,  1,  5,  5,  1,  8,  6,  8,  5,  5,  8,  6,  3,  2,
                       6,  4,  9,  6,  4,  8,  3,  8,  4,  3,  3,  4,  4,  3,  4,  5,  2,
                       4,  4, 10,  9,  7,  2,  9,  5,  4,  3,  5,  4,  5,  4,  4,  4,  4,
                       3,  4,  5,  7,  3,  5,  3,  2,  2,  5,  5,  7,  7,  2])

# Compute ECDF: x, y
x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')

# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))
