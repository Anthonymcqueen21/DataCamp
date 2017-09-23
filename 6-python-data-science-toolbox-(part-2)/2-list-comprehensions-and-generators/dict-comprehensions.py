'''
Dict comprehensions
100xp

Comprehensions aren't relegated merely to the world of lists. There are many other
objects you can build using comprehensions, such as dictionaries, pervasive objects
in Data Science. You will create a dictionary using the comprehension syntax for this
exercise. In this case, the comprehension is called a dict comprehension.

Recall that the main difference between a list comprehension and a dict comprehension
is the use of curly braces {} instead of []. Additionally, members of the dictionary
are created using a colon :, as in key:value.

You are given a list of strings fellowship and, using a dict comprehension, create a
dictionary with the members of the list as the keys and the length of each string as
the corresponding values.

Instructions
Create a dict comprehension where the key is a string in fellowship and the value is
the length of the string. Remember to use the syntax key:value in the output expression
part of the comprehension to create the members of the dictionary. Use member as the
iterator variable.
'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new list
print(new_fellowship)
