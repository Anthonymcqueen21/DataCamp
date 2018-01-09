'''
Customizing melted data

When melting DataFrames, it would be better to have column names more meaningful than variable
and value.

The default names may work in certain situations, but it's best to always have data that is self
explanatory.

You can rename the variable column by specifying an argument to the var_name parameter, and the
value column by specifying an argument to the value_name parameter. You will now practice doing
exactly this. The DataFrame airquality has been pre-loaded for you.

INSTRUCTIONS
100XP
-Print the head of airquality.
-Melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows, with the default
variable column renamed to 'measurement' and the default value column renamed to 'reading'.
You can do this by specifying, respectively, the var_name and value_name parameters.
-Print the head of airquality_melt.
'''
import pandas as pd

airquality = pd.read_csv('../_datasets/airquality.csv')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
