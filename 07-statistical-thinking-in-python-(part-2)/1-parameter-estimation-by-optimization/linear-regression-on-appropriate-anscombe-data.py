'''
Linear regression on appropriate Anscombe data

For practice, perform a linear regression on the data set from Anscombe's quartet that is most reasonably 
interpreted with linear regression.

INSTRUCTIONS
100XP
-Compute the parameters for the slope and intercept using np.polyfit(). The Anscombe data are stored 
in the arrays x and y.
-Print the slope a and intercept b.
-Generate theoretical x and y data from the linear regression. Your x array, which you can create with 
np.array(), should consist of 3 and 15. To generate the y data, multiply the slope by x_theor and add 
the intercept.
-Plot the Anscombe data as a scatter plot and then plot the theoretical line. Remember to include the 
marker='.' and linestyle='none' keyword arguments in addition to x and y when to plot the Anscombe data 
as a scatter plot. You do not need these arguments when plotting the theoretical line.
-Hit 'Submit Answer' to see the plot!
'''
# Perform linear regression: a, b
a, b = np.polyfit(x, y, 1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.plot(x_theor, y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
