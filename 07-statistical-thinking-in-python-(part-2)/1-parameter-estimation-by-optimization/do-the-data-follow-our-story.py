'''
Do the data follow our story?

You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data.
Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential
distribution describes the observed data.

It may be helpful to remind yourself of the function you created in the previous course to compute the
ECDF, as well as the code you wrote to plot it.

INSTRUCTIONS
100XP
-Compute an ECDF from the actual time between no-hitters (nohitter_times). Use the ecdf() function you 
wrote in the prequel course.
-Create a CDF from the theoretical samples you took in the last exercise (inter_nohitter_time).
-Plot x_theor and y_theor as a line using plt.plot(). Then overlay the ECDF of the real data x and y 
as points. To do this, you have to specify the keyword arguments marker = '.' and linestyle = 'none' 
in addition to x and y inside plt.plot().
-Set a 2% margin on the plot.
-Show the plot.
'''
import numpy as np
import matplotlib.pyplot as plt

# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, 10000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(tau*2, 10000)

# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)

# Plot these CDFs as lines
_ = plt.plot(x_half, y_half)
_ = plt.plot(x_double, y_double)

# Show the plot
plt.show()
