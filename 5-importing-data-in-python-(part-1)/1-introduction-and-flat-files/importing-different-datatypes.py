'''
Importing different datatypes
100xp

The file seaslug.txt

has a text header, consisting of strings
is tab-delimited.
These data consists of percentage of sea slug larvae that had metamorphosed in a
given time period. Read more here.

Due to the header, if you tried to import it as-is using np.loadtxt(), Python
would throw you a ValueError and tell you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).

Alternatively, you can skip the first row as we have seen before, using the skiprows
argument.

Instructions
-Complete the first call to np.loadtxt() by passing file as the first argument.
-Execute print(data[0]) to print the first element of data.
-Complete the second call to np.loadtxt(). The file you're importing is tab-delimited,
the datatype is float, and you want to skip the first row.
-Print the 10th element of data_float by completing the print() command. Be guided by
the previous print() call.
-Execute the rest of the code to visualize the data.
'''
import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = '../_datasets/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
