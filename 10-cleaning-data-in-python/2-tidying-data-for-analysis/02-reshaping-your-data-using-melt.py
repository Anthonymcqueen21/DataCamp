'''
Reshaping your data using melt

Melting data is the process of turning columns of your data into rows of data. Consider the
DataFrames from the previous exercise. In the tidy DataFrame, the variables Ozone, Solar.R,
Wind, and Temp each had their own column. If, however, you wanted these variables to be in
rows instead, you could melt the DataFrame. In doing so, however, you would make the data 
untidy! This is important to keep in mind: Depending on how your data is represented, you
will have to reshape it differently.

In this exercise, you will practice melting a DataFrame using pd.melt(). There are two parameters
you should be aware of: id_vars and value_vars. The id_vars represent the columns of the data you
do not want to melt (i.e., keep it in its current shape), while the value_vars represent the
columns you do wish to melt into rows. By default, if no value_vars are provided, all columns
not set in the id_vars will be melted. This could save a bit of typing, depending on the number
of columns that need to be melted.

The (tidy) DataFrame airquality has been pre-loaded. Your job is to melt its Ozone, Solar.R,
Wind, and Temp columns into rows. Later in this chapter, you'll learn how to bring this melted
DataFrame back into a tidy form.

INSTRUCTIONS
100XP
-Print the head of airquality.
-Use pd.melt() to melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows. Do
this by using id_vars to specify the columns you do not wish to melt: 'Month' and 'Day'.
-Print the head of airquality_melt.
'''
import pandas as pd

airquality = pd.read_csv('../_datasets/airquality.csv')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'])

# Print the head of airquality_melt
print(airquality_melt.head())
