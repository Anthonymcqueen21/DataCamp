'''
Operations with other types
100xp
Filip mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

Instructions
Calculate the product of savings and factor. Store the result in year1.
What do you think the resulting type will be? Find out by printing out the type of year1.
Calculate the sum of desc and desc and store the result in a new variable doubledesc.
Print out doubledesc. Did you expect this?
'''
# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of factor and savings to year1
year1 = (savings * factor)

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)