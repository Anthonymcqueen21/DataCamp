'''
Converting data types

In this exercise, you'll see how ensuring all categorical variables in a DataFrame are of type category reduces memory usage.

The tips dataset has been loaded into a DataFrame called tips. This data contains information about how much a customer tipped, whether the customer was male or female, a smoker or not, etc.

Look at the output of tips.info() in the IPython Shell. You'll note that two columns that should be categorical - sex and smoker - are instead of type object, which is pandas' way of storing arbitrary strings. Your job is to convert these two columns to type category and note the reduced memory usage.

INSTRUCTIONS
100XP
-Convert the sex column of the tips DataFrame to type 'category' using the .astype() method.
-Convert the smoker column of the tips DataFrame.
-Print the memory usage of tips after converting the data types of the columns. Use the .info() method to do this.
'''
import pandas as pd

tips = pd.read_csv('../_datasets/tips.csv')


# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())
