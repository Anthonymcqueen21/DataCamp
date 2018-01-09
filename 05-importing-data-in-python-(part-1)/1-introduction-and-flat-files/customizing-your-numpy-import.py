'''
Customizing your NumPy import
100xp

What if there are rows, such as a header, that you don't want to import? What if
your file has a delimiter other than a comma? What if you only wish to import
particular columns?

There are a number of arguments that np.loadtxt() takes that you'll find useful:
delimiter changes the delimiter that loadtxt() is expecting, for example, you can
use ',' and '\t' for comma-delimited and tab-delimited respectively; skiprows allows
you to specify how many rows (not indices) you wish to skip; usecols takes a list of
the indices of the columns you wish to keep.

The file that you'll be importing, digits_header.txt,
-has a header
-is tab-delimited.

Instructions
-Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited,
you want to skip the first row and you only want to import the first and third columns.
-Complete the argument of the print() call in order to print the entire array that you
just imported.
'''
# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)
