'''
Pivot data

Pivoting data is the opposite of melting it. Remember the tidy form that the airquality DataFrame
was in before you melted it? You'll now begin pivoting it back into that form using the
.pivot_table() method!

While melting takes a set of columns and turns it into a single column, pivoting will create a
new column for each unique value in a specified column.

.pivot_table() has an index parameter which you can use to specify the columns that you don't
want pivoted: It is similar to the id_vars parameter of pd.melt(). Two other parameters that
you have to specify are columns (the name of the column you want to pivot), and values (the
values to be used when the column is pivoted). The melted DataFrame airquality_melt has been
pre-loaded for you.

INSTRUCTIONS
100XP
-Print the head of airquality_melt.
-Pivot airquality_melt by using .pivot_table() with the rows indexed by 'Month' and 'Day', the columns indexed by 'measurement', and the values populated with 'reading'.
-Print the head of airquality_pivot.
'''
import pandas as pd

airquality = pd.read_csv('../_datasets/airquality.csv')

airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
