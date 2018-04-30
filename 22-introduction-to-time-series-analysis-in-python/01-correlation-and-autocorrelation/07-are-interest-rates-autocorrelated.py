'''
Are Interest Rates Autocorrelated?

When you look at daily changes in interest rates, the autocorrelation is close to zero. However, if you resample the data and look at annual changes, the autocorrelation is negative. This implies that while short term changes in interest rates may be uncorrelated, long term changes in interest rates are negatively autocorrelated. A daily move up or down in interest rates is unlikely to tell you anything about interest rates tomorrow, but a move in interest rates over a year can tell you something about where interest rates are going over the next year. And this makes some economic sense: over long horizons, when interest rates go up, the economy tends to slow down, which consequently causes interest rates to fall, and vice versa.

The DataFrame daily_data contains daily data of 10-year interest rates from 1962 to 2017.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Create a new column, change_rates of changes in daily rates using the .diff() method.
Compute the autocorrelation of change_rates using the .autocorr() method.
Use the .resample() method with arguments rule='A' to convert to annual frequency and how='last'.
Create a new column of rate changes, diff_rates and compute the autocorrelation, as above.
'''
# Compute the daily change in ingterest rates
daily_data['change_rates'] = daily_data.diff()

# Compute and print the autocorrelation of daily changes
autocorrelation_daily = daily_data['change_rates'].autocorr()
print("The autocorrelation of daily interest rate changes is %4.2f" %(autocorrelation_daily))

# Convert the daily data to annual data
annual_data = daily_data['US10Y'].resample(rule='A', how='last')

# Repeat above for annual data
annual_data['diff_rates'] = annual_data.diff()
autocorrelation_annual = annual_data['diff_rates'].autocorr()
print("The autocorrelation of annual interest rate changes is %4.2f" %(autocorrelation_annual))