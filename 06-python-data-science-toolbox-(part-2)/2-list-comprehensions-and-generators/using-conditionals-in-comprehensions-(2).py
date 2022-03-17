'''
Using conditionals in comprehensions (2)
100xp

In the previous exercise, you used an if conditional statement in the predicate
expression part of a list comprehension to evaluate an iterator variable. In this
exercise, you will use an if-else statement on the output expression of the list.

You will work on the same list, fellowship and, using a list comprehension and an
if-else conditional statement in the output expression, create a list that keeps
members of fellowship with 7 or more characters and replaces others with an empty
string. Use member as the iterator variable in the list comprehension.

Instructions
In the output expression, keep the string as-is if the number of characters is >= 7,
else replace it with an empty string - that is, '' or "".
'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else member.replace(
    member, '') for member in fellowship]

# Print the new list
print(new_fellowship)
