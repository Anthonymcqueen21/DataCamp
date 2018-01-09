'''
Write your own generator expressions
100xp
You are familiar with what generators and generator expressions are, as well as its
difference from list comprehensions. In this exercise, you will practice building
generator expressions on your own.

Recall that generator expressions basically have the same syntax as list comprehensions,
except that it uses parentheses () instead of brackets []; this should make things feel
familiar! Furthermore, if you have ever iterated over a dictionary with .items(), or used
the range() function, for example, you have already encountered and used generators before,
without knowing it! When you use these functions, Python creates generators for you
behind the scenes.

Now, you will start simple by creating a generator object that produces numeric values.

Instructions
-Create a generator object that will produce values from 0 to 30. Assign the result to
result and use num as the iterator variable in the generator expression.
-Print the first 5 values by using next() appropriately in print().
-Print the rest of the values by using a for loop to iterate over the generator object.
'''
# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
