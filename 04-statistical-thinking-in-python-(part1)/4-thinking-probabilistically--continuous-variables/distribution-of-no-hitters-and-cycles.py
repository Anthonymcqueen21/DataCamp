'''
Distribution of no-hitters and cycles
100xp

Now, you'll use your sampling function to compute the waiting time to observer
a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is
764 games, and the mean waiting time for hitting the cycle is 715 games.

Instructions
-Use your successive_poisson() function to draw 100,000 out of the distribution
of waiting times for observing a no-hitter and a hitting of the cycle.
-Plot the PDF of the waiting times using the step histogram technique of a previous
exercise. Don't forget the necessary keyword arguments. You should use bins=100,
normed=True, and histtype='step'.
-Label the axes.
-Show your plot.
'''
import numpy as np
import matplotlib.pyplot as plt

def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2

# Draw samples of waiting times: waiting_times
waiting_times = np.array(successive_poisson(764, 715, 100000))

# Make the histogram
_ = plt.hist(waiting_times, bins=100, normed=True, histtype='step')

# Label axes
_ = plt.xlabel('x')
_ = plt.ylabel('y')

# Show the plot
plt.show()
