'''
Writing list comprehensions
100xp

You now have all the knowledge necessary to begin writing list comprehensions! Your job
in this exercise is to write a list comprehension that produces a list of the squares of
the numbers ranging from 0 to 9.

Instructions
-Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable,
write a list comprehension that produces a list of numbers consisting of the squared values of i.
'''
# Create list comprehension: squares
squares = [i ** 2 for i in range(10)]

print(squares)