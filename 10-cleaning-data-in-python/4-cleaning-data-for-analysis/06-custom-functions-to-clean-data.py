'''
Custom functions to clean data

You'll now practice writing functions to clean data.

The tips dataset has been pre-loaded into a DataFrame called tips. It has a 'sex' column that contains the values 'Male' or 'Female'. Your job is to write a function that will recode 'Male' to 1, 'Female' to 0, and return np.nan for all entries of 'sex' that are neither 'Male' nor 'Female'.

Recoding variables like this is a common data cleaning task. Functions provide a mechanism for you to abstract away complex bits of code as well as reuse code. This makes your code more readable and less error prone.

As Dan showed you in the videos, you can use the .apply() method to apply a function across entire rows or columns of DataFrames. However, note that each column of a DataFrame is a pandas Series. Functions can also be applied across Series. Here, you will apply your function over the 'sex' column.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Define a function named recode_sex() that has one parameter: sex_value.
    -If sex_value equals 'Male', return 1.
    -Else, if sex_value equals 'Female', return 0.
    -If sex_value does not equal 'Male' or 'Female', return np.nan. NumPy has been pre-imported for you.
-Apply your recode_sex() function over tips.sex using the .apply() method to create a new column: 'sex_recode'. Note that when passing in a function inside the .apply() method, you don't need to specify the parentheses after the function name.
-Hit 'Submit Answer' and take note of the new 'sex_recode' column in the tips DataFrame!
'''
import pandas as pd
import re

tips = pd.read_csv('../_datasets/tips.csv')

# Define recode_sex()
def recode_sex(sex_value):

    # Return 1 if sex_value is 'Male'
    if sex_value == 'Male':
        return 1
    
    # Return 0 if sex_value is 'Female'    
    elif sex_value == 'Female':
        return 0
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['sex_recode'] = tips.sex.apply(recode_sex)

# Print the first five rows of tips
print(tips.head())
