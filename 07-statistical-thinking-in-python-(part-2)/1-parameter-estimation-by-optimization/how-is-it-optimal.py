'''
How is it optimal?

The function np.polyfit() that you used to get your regression parameters finds the optimal slope and
intercept. It is optimizing the sum of the squares of the residuals, also known as RSS (for residual
sum of squares). In this exercise, you will plot the function that is being optimized, the RSS, versus
the slope parameter a. To do this, fix the intercept to be what you found in the optimization. Then,
plot the RSS vs. the slope. Where is it minimal?

INSTRUCTIONS
100XP
-Specify the values of the slope for which to compute the RSS. Use np.linspace() to get 200 points
in the range between 0 and 0.1. For example, to get 100 points in the range between 0 and 0.5, you
could use np.linspace() like so: np.linspace(0, 0.5, 100).
-Initialize an array, rss, to contain the RSS using np.empty_like() and the array you created above.
The empty_like() function returns a new array with the same shape and type as a given array 
(in this case, a_vals).
-Write a for loop to compute the sum of RSS of the slope. Hint: the RSS is given by 
np.sum((y_data - a * x_data - b)**2). The variable b you computed in the last exercise is already in 
your namespace. Here, fertility is the y_data and illiteracy the x_data.
-Plot the RSS (rss) versus slope (a_vals).
Hit 'Submit Answer' to see the plot!
'''
import numpy as np
import matplotlib.pyplot as plt

# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a*illiteracy - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()
