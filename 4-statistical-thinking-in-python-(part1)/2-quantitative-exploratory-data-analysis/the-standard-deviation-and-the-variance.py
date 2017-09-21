'''
The standard deviation and the variance
100xp

As mentioned in the video, the standard deviation is the square root of the variance.
You will see this for yourself by computing the standard deviation using np.std() and
comparing it to what you get by computing the variance with np.var() and then computing
the square root.

Instructions
-Compute the variance of the data in the versicolor_petal_length array using np.var().
-Print the square root of this value.
-Compute the standard deviation of the data in the versicolor_petal_length array using
np.std() and print the result.
'''
import numpy as np

versicolor_petal_length = np.array([4.7,  4.5,  4.9,  4.,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
                                    4.2,  4.,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4.,
                                    4.9,  4.7,  4.3,  4.4,  4.8,  5.,  4.5,  3.5,  3.8,  3.7,  3.9,
                                    5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4.,  4.4,  4.6,  4.,  3.3,
                                    4.2,  4.2,  4.2,  4.3,  3.,  4.1])

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))
