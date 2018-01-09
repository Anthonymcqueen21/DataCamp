'''
Computing the Pearson correlation coefficient
100xp
As mentioned in the video, the Pearson correlation coefficient, also called the
Pearson r, is often easier to interpret than the covariance. It is computed using
the np.corrcoef() function. Like np.cov(), it takes two arrays as arguments and
returns a 2D array. Entries [0,0] and [1,1] are necessarily equal to 1 (can you
think about why?), and the value we are after is entry [0,1].

In this exercise, you will write a function, pearson_r(x, y) that takes in two
arrays and returns the Pearson correlation coefficient. You will then use this
function to compute it for the petal lengths and widths of I. versicolor.

Again, we include the scatter plot you generated in a previous exercise to remind
you how the petal width and length are related.

Instructions
-Define a function with signature pearson_r(x, y).
    -Use np.corrcoef() to compute the correlation matrix of x and y (pass them to
    np.corrcoef() in that order).
    -The function returns entry [0,1] of the correlation matrix.
-Compute the Pearson correlation between the data in the arrays versicolor_petal_length
and versicolor_petal_width. Assign the result to r.
-Print the result.
'''
import numpy as np

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


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0, 1]


# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
