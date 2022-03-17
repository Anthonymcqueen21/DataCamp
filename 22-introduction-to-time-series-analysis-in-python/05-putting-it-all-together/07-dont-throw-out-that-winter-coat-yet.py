'''
Don't Throw Out That Winter Coat Yet

Finally, you will forecast the temperature over the next 30 years using an ARMA(1,1) model, including confidence bands around that estimate. Keep in mind that the estimate of the drift will have a much bigger impact on long range forecasts than the ARMA parameters.

Earlier, you determined that the temperature data follows a random walk and you looked at first differencing the data. You will use the ARIMA module on the temperature data, pre-loaded in the DataFrame temp_NY, but the forecast would be the same as using the ARMA module on changes in temperature, and then using cumulative sums of these changes to get the temperature.

The data is in a DataFrame called temp_NY.

INSTRUCTIONS
100XP
Create an instance of the ARIMA class called mod for an integrated ARMA(1,1) model
The d in order(p,d,q) is one, since we first differenced once
Fit mod using the .fit() method and call the results res
Forecast the series using the plot_predict() method on res
Choose the start date as 1872-01-01 and the end date as 2046-01-01
'''
# Import the ARIMA module from statsmodels
from statsmodels.tsa.arima_model import ARIMA

# Forecast interest rates using an AR(1) model
mod = ARIMA(temp_NY, order=(1,1,1))
res = mod.fit()

# Plot the original series and the forecasted series
res.plot_predict(start='1872-01-01', end='2046-01-01')
plt.show()