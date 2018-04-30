'''
Estimate Order of Model: Information Criteria

Another tool to identify the order of a model is to look at the Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC). These measures compute the goodness of fit with the estimated parameters, but apply a penalty function on the number of parameters in the model. You will take the AR(2) simulated data from the last exercise, saved as simulated_data_2, and compute the BIC as you vary the order, p, in an AR(p) from 0 to 6.

INSTRUCTIONS
70XP
Import the ARMA module for estimating the parameters and computing BIC.
Initialize a numpy array BIC, which we will use to store the BIC for each AR(p) model.
Loop through order p for p = 0,...,6.
For each p, fit the data to an AR model of order p.
For each p, save the value of BIC using the .bic attribute (no parentheses) of res.
Plot BIC as a function of p (for the plot, skip p=0 and plot for p=1,...6).
'''
# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA

# Fit the data to an AR(p) for p = 0,...,6 , and save the BIC
BIC = np.zeros(7)
for p in range(7):
    mod = ARMA(simulated_data_2, order=(p,0))
    res = mod.fit()
# Save BIC for AR(p)    
    BIC[p] = res.bic
    
# Plot the BIC as a function of p
plt.plot(range(1,7), BIC[1:7], marker='o')
plt.xlabel('Order of AR Model')
plt.ylabel('Baysian Information Criterion')
plt.show()