'''
Using * and zip to 'unzip'
100xp

You know how to use zip() as well as how to print out values from a zip object. Excellent!

Let's play around with zip() a little more. There is no unzip function for doing the
reverse of what zip() does. We can, however, reverse what has been zipped together by
using zip() with a little help from *! * unpacks an iterable such as a list or a tuple
into positional arguments in a function call.

In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().

Two tuples of strings, mutants and powers have been pre-loaded.

Instructions
-Create a zip object by using zip() on mutants and powers, in that order. Assign the result to z1.
-Print the tuples in z1 by unpacking them into positional arguments using the * operator
in a print() call.
-Because the previous print() call would have exhausted the elements in z1, recreate the
zip object you defined earlier and assign the result again to z1.
-'Unzip' the tuples in z1 by unpacking them into positional arguments using the * operator
in a zip() call. Assign the results to result1 and result2, in that order.
-The last print() statements prints the output of comparing result1 to mutants and result2
to powers. Click Submit Answer to see if the unpacked result1 and result2 are equivalent to
mutants and powers, respectively.
'''
# Provided lists
mutants = ['charles xavier', 'bobby drake',
           'kurt wagner', 'max eisenhardt', 'kitty pride']
powers = ['telepathy', 'thermokinesis',
          'teleportation', 'magnetokinesis', 'intangibility']

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
