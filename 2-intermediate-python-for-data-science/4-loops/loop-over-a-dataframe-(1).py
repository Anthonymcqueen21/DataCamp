'''
Loop over DataFrame (1)
100xp
Iterating over a Pandas DataFrame is typically done with the iterrows() method.
Used in a for loop, every observation is iterated over and on every iteration the
row label and actual row contents are available:

for lab, row in brics.iterrows() :
    ...
In this and the following exercises you will be working on the cars DataFrame.
It contains information on the cars per capita and whether people drive right or
left for seven countries in the world.

Instructions
-Write a for loop that iterates over the rows of cars and on each iteration perform
two print() calls: one to print out the row label and one to print out all of the
rows contents.
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
