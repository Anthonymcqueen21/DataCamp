'''
Working with numeric data

If you expect the data type of a column to be numeric (int or float), but instead it is of type
object, this typically means that there is a non numeric value in the column, which also signifies
bad data.

You can use the pd.to_numeric() function to convert a column into a numeric data type. If the
function raises an error, you can be sure that there is a bad value within the column. You can
either use the techniques you learned in Chapter 1 to do some exploratory data analysis and find
the bad value, or you can choose to ignore or coerce the value into a missing value, NaN.

A modified version of the tips dataset has been pre-loaded into a DataFrame called tips. For
instructional purposes, it has been pre-processed to introduce some 'bad' data for you to clean.
Use the .info() method to explore this. You'll note that the total_bill and tip columns, which
should be numeric, are instead of type object. Your job is to fix this.

INSTRUCTIONS
100XP
-Use pd.to_numeric() to convert the 'total_bill' column of tips to a numeric data type.
Coerce the errors to NaN by specifying the keyword argument errors='coerce'.
-Convert the 'tip' column of 'tips' to a numeric data type exactly as you did for the
'total_bill' column.
-Print the info of tips to confirm that the data types of 'total_bill' and 'tips' are numeric.
'''
import pandas as pd

tips = pd.read_csv('../_datasets/tips.csv')

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())
