'''
Changing the output in generator expressions
100xp

Great! At this point, you already know how to write a basic generator expression.
In this exercise, you will push this idea a little further by adding to the output
expression of a generator expression. Because generator expressions and list
comprehensions are so alike in syntax, this should be a familiar task for you!

You are given a list of strings lannister and, using a generator expression, create
a generator object that you will iterate over to print its values.

Instructions
-Write a generator expression that will generate the lengths of each string in
lannister. Use person as the iterator variable. Assign the result to lengths.
-Supply the correct iterable in the for loop for printing the values in the generator
object.
'''
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
