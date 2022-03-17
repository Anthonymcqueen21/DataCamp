'''
Dictionary to DataFrame (2)
100xp
The Python code that solves the previous exercise is included on the right.
Have you noticed that the row labels (i.e. the labels for the different observations)
were automatically set to integers from 0 up to 6?

To solve this a list row_labels has been created. You can use it to specify the row
labels of the cars DataFrame. You do this by setting the index attribute of cars,
that you can access as cars.index.

Instructions
-Hit Submit Answer to see that, indeed, the row labels are not correctly set.
-Specify the row labels by setting cars.index equal to row_labels.
-Print out cars again and check if the row labels are correct this time.
'''
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
