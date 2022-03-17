'''
Compare the ACF for Several AR Time Series

The autocorrelation function decays exponentially for an AR time series at a rate of the AR parameter. For example, if the AR parameter, ϕ=+0.9
ϕ
=
+
0.9
, the first-lag autocorrelation will be 0.9, the second-lag will be (0.9)2=0.81
(
0.9
)
2
=
0.81
, the third-lag will be (0.9)3=0.729
(
0.9
)
3
=
0.729
, etc. A smaller AR parameter will have a steeper decay, and for a negative AR parameter, say -0.9, the decay will flip signs, so the first-lag autocorrelation will be -0.9, the second-lag will be (−0.9)2=0.81
(
−
0.9
)
2
=
0.81
, the third-lag will be (−0.9)3=−0.729
(
−
0.9
)
3
=
−
0.729
, etc.

The object simulated_data_1 is the simulated time series with an AR parameter of +0.9, simulated_data_2 is for an AR paramter of -0.9, and simulated_data_3 is for an AR parameter of 0.3

INSTRUCTIONS
100XP
Compute the autocorrelation function for each of the three simulated datasets using the plot_acf function with 20 lags (and supress the confidence intervals by setting alpha=1).
'''
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf

# Plot 1: AR parameter = +0.9
plot_acf(simulated_data_1, alpha=1, lags=20)
plt.show()

# Plot 2: AR parameter = -0.9
plot_acf(simulated_data_2, alpha=1, lags=20)
plt.show()

# Plot 3: AR parameter = +0.3
plot_acf(simulated_data_3, alpha=1, lags=20)
plt.show()