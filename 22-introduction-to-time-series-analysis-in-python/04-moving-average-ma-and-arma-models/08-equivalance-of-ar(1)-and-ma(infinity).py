'''
Equivalence of AR(1) and MA(infinity)

To better understand the relationship between MA models and AR models, you will demonstrate that an AR(1) model is equivalent to an MA(∞
∞
) model with the appropriate parameters.

You will simulate an MA model with parameters 0.8,0.82,0.83,…
0.8
,
0.8
2
,
0.8
3
,
…
 for a large number (30) lags and show that it has the same Autocorrelation Function as an AR(1) model with ϕ=0.8
ϕ
=
0.8
.

INSTRUCTIONS
100XP
Import the modules for simulating data and plotting the ACF from statsmodels
Use a list comprehension to build a list with exponentially decaying MA parameters: 1,0.8,0.82,0.83,…
1
,
0.8
,
0.8
2
,
0.8
3
,
…
Simulate 5000 observations of the MA(30) model
Plot the ACF of the simulated series
'''



# import the modules for simulating data and plotting the ACF
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf

# Build a list MA parameters
ma = [0.8**i for i in range(30)]

# Simulate the MA(30) model
ar = np.array([1])
AR_object = ArmaProcess(ar, ma)
simulated_data = AR_object.generate_sample(nsample=5000)

# Plot the ACF
plot_acf(simulated_data, lags=30)
plt.show()