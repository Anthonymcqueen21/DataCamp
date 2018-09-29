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

# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()
