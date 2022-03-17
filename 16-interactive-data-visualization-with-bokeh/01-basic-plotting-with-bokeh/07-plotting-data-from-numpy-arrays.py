'''
Plotting data from NumPy arrays

In the previous exercises, you made plots using data stored in lists. You learned that Bokeh can plot both numbers and datetime objects.

In this exercise, you'll generate NumPy arrays using np.linspace() and np.cos() and plot them using the circle glyph.

np.linspace() is a function that returns an array of evenly spaced numbers over a specified interval. For example, np.linspace(0, 10, 5) returns an array of 5 evenly spaced samples calculated over the interval [0, 10]. np.cos(x) calculates the element-wise cosine of some array x.

For more information on NumPy functions, you can refer to the NumPy User Guide and NumPy Reference.

The figure p has been provided for you.

INSTRUCTIONS
100XP
Import numpy as np.
Create an array x using np.linspace() with 0, 5, and 100 as inputs.
Create an array y using np.cos() with x as input.
Add circles at x and y using p.circle().
'''
# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p.circle(x, y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)
