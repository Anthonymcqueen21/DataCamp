'''
Looking at a Regression's R-Squared

R-squared measures how closely the data fit the regression line, so the R-squared in a simple regression is related to the correlation between the two variables. In particular, the magnitude of the correlation is the square root of the R-squared and the sign of the correlation is the sign of the regression coefficient.

In this exercise, you will start using the statistical package statsmodels, which performs much of the statistical modeling and testing that is found in R and software packages like SAS and MATLAB.

You will take two series, x and y, compute their correlation, and then regress y on x using the function OLS() in the statsmodels.api library. Most linear regressions contain a constant term which is the intercept (the α
α
 in the regression yt=α+βxt+ϵt
y
t
=
α
+
β
x
t
+
ϵ
t
). To include a constant using the function OLS(), you need to add a column of 1's to the right hand side of the regression.

The module statsmodels.api has been imported for you as sm.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Compute the correlation between x and y using the .corr() method.
Regress y on x by first converting the Series x to a DataFrame and adding a constant to it using sm.add_constant(). Then fit the regression using sm.OLS(y,x).fit().
Print out the results of the regression and compare the R-squared with the correlation.
'''
# Import the statsmodels module
import statsmodels.api as sm

# Compute correlation of x and y
correlation = x.corr(y)
print("The correlation between x and y is %4.2f" %(correlation))

# Convert the Series x to a DataFrame and name the column x
x = pd.DataFrame(x, columns=['x'])

# Add a constant to the DataFrame x
x = sm.add_constant(x)

# Fit the regression of y on x
result = sm.OLS(y,x).fit()

# Print out the results and look at the relationship between R-squared and the correlation above
print(result.summary())
