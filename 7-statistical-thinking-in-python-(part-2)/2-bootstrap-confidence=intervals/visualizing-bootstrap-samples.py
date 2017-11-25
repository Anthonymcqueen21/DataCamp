'''
Visualizing bootstrap samples

In this exercise, you will generate bootstrap samples from the set of annual rainfall data measured at
the Sheffield Weather Station in the UK from 1883 to 2015. The data are stored in the NumPy array
rainfall in units of millimeters (mm). By graphically displaying the bootstrap samples with an ECDF,
you can get a feel for how bootstrap sampling allows probabilistic descriptions of data.

INSTRUCTIONS
100XP
-Write a for loop to acquire 50 bootstrap samples of the rainfall data and plot their ECDF.
-Use np.random.choice() to generate a bootstrap sample from the NumPy array rainfall. Be sure that
the size of the resampled array is len(rainfall).
-Use the function ecdf() that you wrote in the prequel to this course to generate the x and y values
for the ECDF of the bootstrap sample bs_sample.
-Plot the ECDF values. Specify color='gray' (to make gray dots) and alpha=0.1 (to make them
semi-transparent, since we are overlaying so many) in addition to the marker='.' and linestyle='none'
keyword arguments.
-Use ecdf() to generate x and y values for the ECDF of the original rainfall data available in the
array rainfall.
-Plot the ECDF values of the original data.
Hit 'Submit Answer' to visualize the samples!
'''
import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

rainfall = np.array([   875.5,   648.2,   788.1,   940.3,   491.1,   743.5,   730.1,
                        686.5,   878.8,   865.6,   654.9,   831.5,   798.1,   681.8,
                        743.8,   689.1,   752.1,   837.2,   710.6,   749.2,   967.1,
                        701.2,   619. ,   747.6,   803.4,   645.6,   804.1,   787.4,
                        646.8,   997.1,   774. ,   734.5,   835. ,   840.7,   659.6,
                        828.3,   909.7,   856.9,   578.3,   904.2,   883.9,   740.1,
                        773.9,   741.4,   866.8,   871.1,   712.5,   919.2,   927.9,
                        809.4,   633.8,   626.8,   871.3,   774.3,   898.8,   789.6,
                        936.3,   765.4,   882.1,   681.1,   661.3,   847.9,   683.9,
                        985.7,   771.1,   736.6,   713.2,   774.5,   937.7,   694.5,
                        598.2,   983.8,   700.2,   901.3,   733.5,   964.4,   609.3,
                        1035.2,   718. ,   688.6,   736.8,   643.3,  1038.5,   969. ,
                        802.7,   876.6,   944.7,   786.6,   770.4,   808.6,   761.3,
                        774.2,   559.3,   674.2,   883.6,   823.9,   960.4,   877.8,
                        940.6,   831.8,   906.2,   866.5,   674.1,   998.1,   789.3,
                        915. ,   737.1,   763. ,   666.7,   824.5,   913.8,   905.1,
                        667.8,   747.4,   784.7,   925.4,   880.2,  1086.9,   764.4,
                        1050.1,   595.2,   855.2,   726.9,   785.2,   948.8,   970.6,
                        896. ,   618.4,   572.4,  1146.4,   728.2,   864.2,   793. ])

for _ in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
_ = plt.plot(x, y, marker='.')

# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly rainfall (mm)')
_ = plt.ylabel('ECDF')

# Show the plot
plt.show()
