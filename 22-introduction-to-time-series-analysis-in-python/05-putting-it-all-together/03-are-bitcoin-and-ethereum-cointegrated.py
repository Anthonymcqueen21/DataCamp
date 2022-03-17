'''
Are Bitcoin and Ethereum Cointegrated?

Cointegration involves two steps: regressing one time series on the other to get the cointegration vector, and then perform an ADF test on the residuals of the regression. In the last example, there was no need to perform the first step since we implicitly assumed the cointegration vector was (1,−1)
(
1
,
−
1
)
. In other words, we took the difference between the two series (after doing a units conversion). Here, you will do both steps.

You will regress the value of one crytocurrency, bitcoin (BTC), on another cryptocurrency, ethereum (ETH). If we call the regression coeffiecient b
b
, then the cointegration vector is simply (1,−b)
(
1
,
−
b
)
. Then perform the ADF test on BTC −b
−
b
 ETH. Bitcoin and Ethereum prices are pre-loaded in DataFrames BTC and ETH.

Bitcoin data are in DataFrame BTC and Ethereum data are in ETH.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import the statsmodels module for regression and the adfuller function
Add a constant to the ETH DataFrame using sm.add_constant()
Fit the regression using sm.OLS(y,x).fit() and save the results in result. The intercept is in result.params[0] and the slope in result.params[1]
Run ADF test on BTC −b
−
b
 ETH
 '''
# Import the statsmodels module for regression and the adfuller function
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# Regress BTC on ETH
ETH = sm.add_constant(ETH)
result = sm.OLS(BTC,ETH).fit()

# Compute ADF
b = result.params[1]
adf_stats = adfuller(BTC['Price'] - b*ETH['Price'])
print("The p-value for the ADF test is ", adf_stats[1])
# The data suggests that Bitcoin and Ethereum are cointegrated