'''
Calculations with variables
100xp
Remember how you calculated the money you ended up with after 7 years of investing $100? You did something like this:

100 * 1.10 ** 7
Instead of calculating with the actual values, you can use variables instead. The savings variable you've created in the previous exercise represents the $100 you started with. It's up to you to create a new variable to represent 1.10 and then redo the calculations!

Instructions
Create a variable factor, equal to 1.10.
Use savings and factor to calculate the amount of money you end up with after 7 years. Store the result in a new variable, result.
Print out the value of result.
'''
# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.10

# Calculate result
years = 7
result = (savings * factor ** years)

# Print out result
print(result)
