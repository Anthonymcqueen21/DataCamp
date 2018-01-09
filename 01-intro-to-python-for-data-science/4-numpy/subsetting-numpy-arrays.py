'''
Subsetting NumPy Arrays
100xp
You've seen it with your own eyes: Python lists and numpy arrays sometimes behave differently.
Luckily, there are still certainties in this world. For example, subsetting (using the square
bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the
following lines of code in the IPython Shell:

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]
The script on the right already contains code that imports numpy as np, and stores both the
height and weight of the MLB players as numpy arrays.

Instructions
-Subset np_weight: print out the element at index 50.
-Print out a sub-array of np_height: It contains the elements at index 100 up to and including
index 110
'''
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])