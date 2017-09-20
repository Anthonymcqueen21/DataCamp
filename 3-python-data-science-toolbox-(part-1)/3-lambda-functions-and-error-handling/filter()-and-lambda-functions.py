'''
Filter() and lambda functions
100xp

In the previous exercise, you used lambda functions to anonymously embed an
operation within map(). You will practice this again in this exercise by using
a lambda function with filter(), which may be new to you! The function filter()
offers a way to filter out elements from a list that don't satisfy certain criteria.

Your goal in this exercise is to use filter() to create, from an input list of
strings, a new list that contains only strings that have more than 6 characters.

Instructions
-In the filter() call, pass a lambda function and the list of strings, fellowship.
The lambda function should check if the number of characters in a string member is
greater than 6; use the len() function to do this. Assign the resulting filter
object to result.
-Convert result to a list and print out the list.
'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6 , fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)
