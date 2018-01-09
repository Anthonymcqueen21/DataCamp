'''
Computing the variance
100xp

It is important to have some understanding of what commonly-used functions are doing
under the hood. Though you may already know how to compute variances, this is a beginner
course that does not assume so. In this exercise, we will explicitly compute the variance
of the petal length of Iris veriscolor using the equations discussed in the videos. We will
then use np.var() to compute it.

Instructions
-Create an array called differences that is the difference between the petal lengths
(versicolor_petal_length) and the mean petal length. The variable versicolor_petal_length
is already in your namespace as a NumPy array so you can take advantage of NumPy's vectorized operations.
-Square each element in this array. For example, x**2 squares each element in the array x.
Store the result as diff_sq.
-Compute the mean of the elements in diff_sq using np.mean(). Store the result as variance_explicit.
-Compute the variance of versicolor_petal_length using np.var(). Store the result as variance_np.
-Print both variance_explicit and variance_np in one print call to make sure they are consistent.
'''
import numpy as np

versicolor_petal_length = np.array([4.7,  4.5,  4.9,  4.,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
                                    4.2,  4.,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4.,
                                    4.9,  4.7,  4.3,  4.4,  4.8,  5.,  4.5,  3.5,  3.8,  3.7,  3.9,
                                    5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4.,  4.4,  4.6,  4.,  3.3,
                                    4.2,  4.2,  4.2,  4.3,  3.,  4.1])

# Array of differences to mean: differences
differences = np.array(versicolor_petal_length -
                       np.mean(versicolor_petal_length))

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)
