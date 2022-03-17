'''
Writing a generator to load data in chunks (2)
100xp

In the previous exercise, you processed a file line by line for a given number of lines.
What if, however, you want to do this for the entire file?

In this case, it would be useful to use generators. Generators allow users to lazily evaluate
data. This concept of lazy evaluation is useful when you have to deal with very large datasets
because it lets you generate values in an efficient manner by yielding only chunks of data at a
time instead of the whole thing at once.

In this exercise, you will define a generator function read_large_file() that produces a generator
object which yields a single line from a file each time next() is called on it. The csv file
'world_dev_ind.csv' is in your current directory for your use.

Note that when you open a connection to a file, the resulting file object is already a generator!
So out in the wild, you won't have to explicitly create generator objects in cases such as this.
However, for pedagogical reasons, we are having you practice how to do this here with the
read_large_file() function. Go for it!

Instructions
-In the function read_large_file(), read a line from file_object by using the method readline().
Assign the result to data.
-In the function read_large_file(), yield the line read from the file data.
-In the context manager, create a generator object gen_file by calling your generator function
read_large_file() and passing file to it.
-Print the first three lines produced by the generator object gen_file using next().
'''

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
