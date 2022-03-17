'''
Subsetting 2D NumPy Arrays
100xp
If your 2D numpy array has a regular structure, i.e. each row and column has a
fixed number of values, complicated ways of subsetting become very easy.
Have a look at the code below where the elements "a" and "c" are extracted
from a list of lists.

# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]

For regular Python lists, this is a real pain. For 2D numpy arrays, however,
it's pretty intuitive! The indexes before the comma refer to the rows, while
those after the comma refer to the columns. The : is for slicing; in this example,
it tells Python to include all rows.

The code that converts the pre-loaded baseball list to a 2D numpy array is already
in the script. The first column contains the players' height in inches and the second
column holds player weight, in pounds. Add some lines to make the correct selections.
Remember that in Python, the first element is at index 0!

Instructions
-Print out the 50th row of np_baseball.
-Make a new variable, np_weight, containing the entire second column of np_baseball.
-Select the height (first column) of the 124th baseball player in np_baseball and print it out.
'''
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])