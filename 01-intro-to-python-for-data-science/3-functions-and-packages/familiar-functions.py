'''
Familiar functions
100xp
Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist
easier. You already know two such functions: print() and type(). You've also used the functions
str(), int(), bool() and float() to switch between data types. These are built-in functions as well.

Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result,
you can use the following:

result = type(3.0)
The general recipe for calling functions is thus:

output = function_name(input)

Instructions
-Use print() in combination with type() to print out the type of var1.
-Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
-Use int() to convert var2 to an integer. Store the output as out2.
'''
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
