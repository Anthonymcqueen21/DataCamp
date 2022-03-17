'''
How About Stock Returns?

In the last exercise, you showed that Amazon stock prices, contained in the DataFrame AMZN follow a random walk. In this exercise. you will do the same thing for Amazon returns (percent change in prices) and show that the returns do not follow a random walk.

INSTRUCTIONS
100XP
Import the adfuller module from statsmodels.
Create a new DataFrame of AMZN returns by taking the percent change of prices using the method .pct_change().
Eliminate the NaN in the first row of returns using the .dropna() method on the DataFrame.
Run the Augmented Dickey-Fuller test on the Adj Close column of the returns DataFrame, and print out the p-value in `results[1].
'''
# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller

# Create a DataFrame of AMZN returns
AMZN_ret = AMZN.pct_change()

# Eliminate the NaN in the first row of returns
AMZN_ret = AMZN_ret.dropna()

# Run the ADF test on the return series and print out the p-value
results = adfuller(AMZN_ret['Adj Close'])
print('The p-value of the test on returns is: ' + str(results[1]))