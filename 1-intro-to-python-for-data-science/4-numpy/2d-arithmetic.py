'''
2D Arithmetic
100xp
Remember how you calculated the Body Mass Index for all baseball players?
numpy was able to perform all calculations element-wise (i.e. element by element).
For 2D numpy arrays this isn't any different! You can combine matrices with single
numbers, with vectors, and with other matrices.

Execute the code below in the IPython shell and see if you understand:

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat
np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing
height, weight and age.

Instructions
-You managed to get hold of the changes in weight, height and age of all baseball players.
It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
-You want to convert the units of height and weight. As a first step, create a numpy array
with three values: 0.0254, 0.453592 and 1. Name this array conversion.
-Multiply np_baseball with conversion and print out the result.
'''
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1.0])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
