'''
Working with mixed datatypes (2)
100xp

You have just used np.genfromtxt() to import data containing mixed datatypes. There
is also another function np.recfromcsv() that behaves similarly to np.genfromtxt(),
except that its default dtype is None. In this exercise, you'll practice using this
to achieve the same result.

Instructions
-Import titanic.csv using the function np.recfromcsv() and assign it to the variable,
d. You'll only need to pass file to it because it has the defaults delimiter=',' and
names=True in addition to dtype=None!
-Run the remaining code to print the first three entries of the resulting array d.
'''
import numpy as np

# Assign the filename: file
file = '../_datasets/titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
