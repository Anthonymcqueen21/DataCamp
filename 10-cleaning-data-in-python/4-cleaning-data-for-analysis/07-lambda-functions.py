'''
Lambda functions

You'll now be introduced to a powerful Python feature that will help you clean your data more effectively: lambda functions. Instead of using the def syntax that you used in the previous exercise, lambda functions let you make simple, one-line functions.

For example, here's a function that squares a variable used in an .apply() method:

def my_square(x):
    return x ** 2

df.apply(my_square)
The equivalent code using a lambda function is:

df.apply(lambda x: x ** 2)
The lambda function takes one parameter - the variable x. The function itself just squares x and returns the result, which is whatever the one line of code evaluates to. In this way, lambda functions can make your code concise and Pythonic.

The tips dataset has been pre-loaded into a DataFrame called tips. Your job is to clean its 'total_dollar' column by removing the dollar sign. You'll do this using two different methods: With the .replace() method, and with regular expressions. The regular expression module re has been pre-imported.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Use the .replace() method inside a lambda function to remove the dollar sign from the 'total_dollar' column of tips.
    -You need to specify two arguments to the .replace() method: The string to be replaced ('$'), and the string to replace it by ('').
    -Apply the lambda function over the 'total_dollar' column of tips.
-Use a regular expression to remove the dollar sign from the 'total_dollar' column of tips.
    -The pattern has been provided for you: It is the first argument of the re.findall() function.
    -Complete the rest of the lambda function and apply it over the 'total_dollar' column of tips. Notice that because re.findall() returns a list, you have to slice it in order to access the actual value.
Hit 'Submit Answer' to verify that you have removed the dollar sign from the column.
'''
import pandas as pd
import re

tips = pd.read_csv('../_datasets/tips.csv')

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())

