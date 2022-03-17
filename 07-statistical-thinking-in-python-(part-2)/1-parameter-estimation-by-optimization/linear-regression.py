'''
Linear regression

We will assume that fertility is a linear function of the female illiteracy rate. That is, f=ai+b, where 
a is the slope and b is the intercept. We can think of the intercept as the minimal fertility rate,
probably somewhere between one and two. The slope tells us how the fertility rate varies with illiteracy.
We can find the best fit line using np.polyfit().

Plot the data and the best fit line. Print out the slope and intercept. (Think: what are their units?)

INSTRUCTIONS
100XP
-Compute the slope and intercept of the regression line using np.polyfit(). Remember, fertility is on the y-axis and illiteracy on the x-axis.
-Print out the slope and intercept from the linear regression.
-To plot the best fit line, create an array x that consists of 0 and 100 using np.array(). Then, compute the theoretical values of y based on your regression parameters. I.e., y = a * x + b.
-Plot the data and the regression line on the same plot. Be sure to label your axes.
-Hit 'Submit Answer' to display your plot.
'''

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, 1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()
