'''
Forecasting with MA Model

As you did with AR models, you will use MA models to forecast in-sample and out-of-sample data using statsmodels.

For the simulated series simulated_data_1 with θ=−0.9
θ
=
−
0.9
, you will plot in-sample and out-of-sample forecasts. One big difference you will see between out-of-sample forecasts with an MA(1) model and an AR(1) model is that the MA(1) forecasts more than one period in the future are simply the mean of the sample.

INSTRUCTIONS
100XP
Import the class ARMA in the module statsmodels.tsa.arima_model
Create an instance of the ARMA class called mod using the simulated data simulated_data_1 and the (p,q) order of the model (in this case, for an MA(1), order=(0,1)
Fit the model mod using the method .fit() and save it in a results object called res
Plot the in-sample and out-of-sample forecasts of the data using the .plot_predict() method
Start the forecast 10 data points before the end of the 1000 point series at 990, and end the forecast 10 data points after the end of the series at point 1010
'''
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Forecast the first MA(1) model
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()
res.plot_predict(start=990, end=1010)
plt.show()