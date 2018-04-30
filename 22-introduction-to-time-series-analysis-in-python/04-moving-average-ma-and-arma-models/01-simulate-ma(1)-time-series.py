'''
Simulate MA(1) Time Series

You will simulate and plot a few MA(1) time series, each with a different parameter, θ
θ
, using the arima_process module in statsmodels, just as you did in the last chapter for AR(1) models. You will look at an MA(1) model with a large positive θ
θ
 and a large negative θ
θ
.

As in the last chapter, when inputting the coefficients, you must include the zero-lag coefficient of 1, but unlike the last chapter on AR models, the sign of the MA coefficients is what we would expect. For example, for an MA(1) process with θ=−0.9
θ
=
−
0.9
, the array representing the MA parameters would be ma = np.array([1, -0.9])

INSTRUCTIONS
100XP
Import the class ArmaProcess in the arima_process module.
Plot the simulated MA(1) processes
Let ma1 represent an array of the AR parameters [1, θ
θ
] as explained above. The AR parmater array will contain just the lag-zero coeffienct of one.
With parameters ar1 and ma1, create an instance of the class ArmaProcess(ar,ma) called MA_object1.
Simulate 1000 data points from the object you just created, MA_object1, using the method .generate_sample(). Plot the simulated data in a subplot.
Repeat for the other MA parameter.
'''
# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess

# Plot 1: MA parameter = -0.9
plt.subplot(2,1,1)
ar1 = np.array([1])
ma1 = np.array([1, -0.9])
MA_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = MA_object1.generate_sample(nsample=1000)
plt.plot(simulated_data_1)

# Plot 2: MA parameter = +0.9
plt.subplot(2,1,2)
ar2 = np.array([1])
ma2 = np.array([1, 0.9])
MA_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = MA_object2.generate_sample(nsample=1000)
plt.plot(simulated_data_2)

plt.show()
