'''
Using NumPy to import flat files
100xp

In this exercise, you're now going to load the MNIST digit recognition dataset using
the numpy function loadtxt() and see just how easy it can be:

-The first argument will be the filename.
-The second will be the delimiter which, in this case, is a comma.

You can find more information about the MNIST dataset here on the webpage of Yann LeCun,
who is currently Director of AI Research at Facebook and Founding Director of the NYU
Center for Data Science, among many other things.

Instructions
-Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
-Fill in the argument of print() to print the type of the object digits. Use the function type().
-Execute the rest of the code to visualize one of the rows of the data.
'''

# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = '../_datasets/digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
