'''
Changing index of a DataFrame

As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.

A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)]. This is equivalent to the following code:

cubes = []
for i in range(10):
    cubes.append(i**3)
Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.

INSTRUCTIONS
100XP
Create a list new_idx with the same elements as in sales.index, but with all characters capitalized.
Assign new_idx to sales.index.
Print the sales dataframe. This has been done for you, so hit 'Submit Answer' and to see how the index changed.
'''
# Create the list of new indexes: new_idx
new_idx = [i.upper() for i in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
