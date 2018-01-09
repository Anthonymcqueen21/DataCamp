'''
Your First NumPy Array
100xp
In this chapter, we're going to dive into the world of baseball. Along the way, you'll get
comfortable with the basics of numpy, a powerful package to do data science.

A list baseball has already been defined in the Python script, representing the height of
some baseball players in centimeters. Can you add some code here and there to create a numpy
array from it?

Instructions
-Import the numpy package as np, so that you can refer to numpy with np.
-Use np.array() to create a numpy array from baseball. Name this array np_baseball.
-Print out the type of np_baseball to check that you got it right.
'''
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
