'''
Square Brackets (1)
100xp
In the video, you saw that you can index and select Pandas DataFrames in many different ways.
The simplest, but not the most powerful way, is to use square brackets.

In the sample code on the right, the same cars data is imported from a CSV files as a Pandas DataFrame.
To select only the cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']]
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.

Instructions
-Use single square brackets to print out the country column of cars as a Pandas Series.
-Use double square brackets to print out the country column of cars as a Pandas DataFrame.
-Use double square brackets to print out a DataFrame with both the country and drives_right
columns of cars, in this order.
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])
