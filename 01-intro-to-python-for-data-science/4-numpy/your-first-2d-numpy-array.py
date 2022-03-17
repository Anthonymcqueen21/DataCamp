'''
Before working on the actual MLB data, let's try to create a 2D numpy array from a small
 list of lists.

In this exercise, baseball is a list of lists. The main list contains 4 elements.
Each of these elements is a list containing the height and the weight of 4 baseball
players, in this order. baseball is already coded for you in the script.

Instructions
-Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
-Print out the type of np_baseball.
-Print out the shape attribute of np_baseball. Use np_baseball.shape.
'''
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
