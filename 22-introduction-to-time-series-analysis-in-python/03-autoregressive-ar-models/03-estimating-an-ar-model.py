'''
Estimating an AR Model

You will estimate the AR(1) parameter, ϕ
ϕ
, of one of the simulated series that you generated in the earlier exercise. Since the parameters are known for a simulated series, it is a good way to understand the estimation routines before applying it to real data.

For simulated_data_1 with a true ϕ
ϕ
 of 0.9, you will print out the estimate of ϕ
ϕ
. In addition, you will also print out the entire output that is produced when you fit a time series, so you can get an idea of what other tests and summary statistics are available in statsmodels.

INSTRUCTIONS
100XP
Import the class ARMA in the module statsmodels.tsa.arima_model.
Create an instance of the ARMA class called mod using the simulated data simulated_data_1 and the order (p,q) of the model (in this case, for an AR(1)), is order=(1,0).
Fit the model mod using the method .fit() and save it in a results object called res.
Print out the entire summmary of results using the .summary() method.
Just print out an estimate of the constant and ϕ
ϕ
 using the .params attribute (no parentheses).
 '''
 # Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Fit an AR(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(1,0))
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for phi
print("When the true phi=0.9, the estimate of phi (and the constant) are:")
print(res.params)