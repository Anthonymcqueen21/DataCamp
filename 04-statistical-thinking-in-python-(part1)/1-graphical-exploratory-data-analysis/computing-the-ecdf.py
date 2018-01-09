'''
Computing the ECDF
100xp

In this exercise, you will write a function that takes as input a 1D array of
data and then returns the x and y values of the ECDF. You will use this function
over and over again throughout this course and its sequel. ECDFs are among the most
important plots in statistical analysis. You can write your own function, foo(x,y)
according to the following skeleton:

def foo(a,b):
    """State what function does here"""
    # Computation performed here
    return x, y

The function foo() above takes two arguments a and b and returns two values x and y.
The function header def foo(a,b): contains the function signature foo(a,b), which
consists of the function name, along with its parameters. For more on writing your
own functions, see DataCamp's course Python Data Science Toolbox (Part 1) here!

Instructions
-Define a function with the signature ecdf(data). Within the function definition,
    -Compute the number of data points, n, using the len() function.
    -The x-values are the sorted data. Use the np.sort() function to perform the sorting.
    -The y data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct 
        this using np.arange(). Remember, however, that the end value in np.arange() is not 
        inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n.
    -The function returns the values x and y.
'''
import numpy as np

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
