'''
Computing the covariance
100xp
The covariance may be computed using the Numpy function np.cov(). For example,
we have two sets of data x and y, np.cov(x, y) returns a 2D array where entries
[0,1] and [1,0] are the covariances. Entry [0,0] is the variance of the data in x,
and entry [1,1] is the variance of the data in y. This 2D output array is called
the covariance matrix, since it organizes the self- and covariance.

To remind you how the I. versicolor petal length and width are related, we include
the scatter plot you generated in a previous exercise.

Instructions
-Use np.cov() to compute the covariance matrix for the petal length
(versicolor_petal_length) and width (versicolor_petal_width) of I. versicolor.
-Print the covariance matrix.
-Extract the covariance from entry [0,1] of the covariance matrix. Note that by symmetry,
entry [1,0] is the same as entry [0,1].
-Print the covariance.
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

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0, 1]

# Print the length/width covariance
print(petal_cov)
