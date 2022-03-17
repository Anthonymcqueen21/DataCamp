'''
Baseball data in 2D form
100xp
You have another look at the MLB data and realize that it makes more sense to
restructure all this information in a 2D numpy array. This array should have
1015 rows, corresponding to the 1015 baseball players you have information on, 
nd 2 columns (for height and weight).

The MLB was, again, very helpful and passed you the data in a different structure,
a Python list of lists. In this list of lists, each sublist represents the height
and weight of a single baseball player. The name of this embedded list is baseball.

Can you store the data as a 2D array to unlock numpy's extra functionality?

Instructions
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the shape attribute of np_baseball.
'''
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
