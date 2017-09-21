'''
Working with mixed datatypes (1)
50xp

Much of the time you will need to import datasets which have different datatypes
in different columns; one column may contain strings and another floats, for example.
The function np.loadtxt() will freak at this. There is another function, np.genfromtxt(),
which can handle such structures. If we pass dtype=None to it, it will figure out what
types each column should be.

Import 'titanic.csv' using the function np.genfromtxt() as follows:

data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

Here, the first argument is the filename, the second specifies the delimiter , and the
third argument names tells us there is a header. Because the data are of different types,
data is an object called a structured array. Because numpy arrays have to contain elements
that are all the same type, the structured array solves this by being a 1D array, where
each element of the array is a row of the flat file imported. You can test this by checking
out the array's shape in the shell by executing np.shape(data).

Acccessing rows and columns of structured arrays is super-intuitive: to get the ith row,
merely execute data[i] and to get the column with name 'Fare', execute data['Fare'].

Print the entire column with name Survived to the shell. What are the last 4 values of this column?

Possible Answers
-1,0,0,1
-1,2,0,0
-1,0,1,0
-0,1,0
'''
import numpy as np

data = np.genfromtxt('../_datasets/titanic.csv', delimiter=',', names=True, dtype=None)

print(np.shape(data))

print(data['Survived'])

# 1,0,1,0
