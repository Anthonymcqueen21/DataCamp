'''
Plotting the ECDF
100xp

You will now use your ecdf() function to compute the ECDF for the petal lengths of
Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf()
function returns two arrays so you will need to unpack them. An example of such unpacking
is x, y = foo(data), for some function foo().

Instructions
-Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
-Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' in addition to x_vers and y_vers as arguments inside plt.plot().
-Set the margins of the plot with plt.margins() so that no data points are cut off. Use a 2% margin.
-Label the axes. You can label the y-axis 'ECDF'.
-Show your plot.
'''
import numpy as np
import matplotlib.pyplot as plt

versicolor_petal_length = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1])
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('length')
_ = plt.ylabel('ECDF')


# Display the plot
plt.show()
