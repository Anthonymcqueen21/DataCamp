'''
Type conversion
100xp
Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to summarize
the results in a string. Assuming the floats savings and result are defined, you can try something
like this:

print("I started with $" + savings + " and now have $" + result + ". Awesome!")
This will not work, though, as you cannot simply sum strings and floats.

To fix the error, you'll need to explicitly convert the types of your variables. More specifically,
you'll need str(), to convert a value into a string. str(savings), for example, will convert the
float savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any
type.

Instructions
Hit Submit Answer to run the code on the right. Try to understand the error message.
Fix the code on the right such that the printout runs without errors; use the function str() to
convert the variables to strings.
Convert the variable pi_string to a float and store this float as a new variable, pi_float.
'''
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
