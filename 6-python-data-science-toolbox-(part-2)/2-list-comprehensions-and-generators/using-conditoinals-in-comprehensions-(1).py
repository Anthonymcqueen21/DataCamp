'''
Using conditionals in comprehensions (1)
100xp

You've been using list comprehensions to build lists of values, sometimes using operations
to create these values.

An interesting mechanism in list comprehensions is that you can also create lists with
values that meet only a certain condition. One way of doing this is by using conditionals
on iterator variables. In this exercise, you will do exactly that!

Recall from the video that you can apply a conditional statement to test the iterator
variable by adding an if statement in the optional predicate expression part after the
for statement in the comprehension:

[ output expression for iterator variable in iterable if predicate expression ].

You will use this recipe to write a list comprehension for this exercise. You are given a
list of strings fellowship and, using a list comprehension, you will create a list that
only includes the members of fellowship that have 7 characters or more.

Instructions
-Use member as the iterator variable in the list comprehension. For the conditional, use
len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.
'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)
