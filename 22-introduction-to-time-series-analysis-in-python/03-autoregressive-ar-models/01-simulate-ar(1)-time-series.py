'''
Simulate AR(1) Time Series

You will simulate and plot a few AR(1) time series, each with a different parameter, ϕ
ϕ
, using the arima_process module in statsmodels. In this exercise, you will look at an AR(1) model with a large positive ϕ
ϕ
 and a large negative ϕ
ϕ
, but feel free to play around with your own parameters.

There are a few conventions when using the arima_process module that require some explanation. First, these routines were made very generally to handle both AR and MA models. We will cover MA models next, so for now, just ignore the MA part. Second, when inputting the coefficients, you must include the zero-lag coefficient of 1, and the sign of the other coefficients is opposite what we have been using (to be consistent with the time series literature in signal processing). For example, for an AR(1) process with ϕ=0.9
ϕ
=
0.9
, the array representing the AR parameters would be ar = np.array([1, -0.9])

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import the class ArmaProcess in the arima_process module.
Plot the simulated AR procesees:
Let ar1 represent an array of the AR parameters [1, −ϕ
−
ϕ
] as explained above. For now, the MA parmater array, ma1, will contain just the lag-zero coefficient of one.
With parameters ar1 and ma1, create an instance of the class ArmaProcess(ar,ma) called AR_object1.
Simulate 1000 data points from the object you just created, AR_object1, using the method .generate_sample(). Plot the simulated data in a subplot.
Repeat for the other AR parameter.
'''
# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess

# Plot 1: AR parameter = +0.9
plt.subplot(2,1,1)
ar1 = np.array([1, -0.9])
ma1 = np.array([1])
AR_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = AR_object1.generate_sample(nsample=1000)
plt.plot(simulated_data_1)

# Plot 2: AR parameter = -0.9
plt.subplot(2,1,2)
ar2 = np.array([1, 0.9])
ma2 = np.array([1])
AR_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = AR_object2.generate_sample(nsample=1000)
plt.plot(simulated_data_2)
plt.show()
