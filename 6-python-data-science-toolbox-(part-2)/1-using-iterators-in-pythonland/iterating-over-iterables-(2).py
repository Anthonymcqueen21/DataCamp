'''
Iterating over iterables (2)
100xp

One of the things you learned about in this chapter is that not all iterables are actual lists.
A couple of examples that we looked at are strings and the use of the range() function. In this
exercise, we will focus on the range() function.

You can use range() in a for loop as if it's a list to be iterated over:

for i in range(5):
    print(i)

Recall that range() doesn't actually create the list; instead, it creates a range object with
an iterator that produces the values until it reaches the limit (in the example, until the value
4). If range() created the actual list, calling it with a value of 10^100 may not work, especially
since a number as big as that may go over a regular computer's memory. The value 10^100 is actually
what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

Your task for this exercise is to show that calling range() with 10^100 won't actually pre-create
the list.

-Instructions
-Create an iterator object small_value over range(3) using the function iter().
-Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the
loop variable.
-Create an iterator object googol over range(10 ** 100).
'''
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
