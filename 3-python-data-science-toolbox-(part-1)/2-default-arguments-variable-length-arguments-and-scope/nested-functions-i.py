'''
Nested Functions I
100xp

You've learned in the last video about nesting functions within functions.
One reason why you'd like to do this is to avoid writing out the same computations
within functions repeatedly. There's nothing new about defining nested functions:
you simply define it as you would a regular function with def and embed it inside
another function!

In this exercise, inside a function three_shouts(), you will define a nested function
inner() that concatenates a string object with !!!. three_shouts() then returns a tuple
of three elements, each a string concatenated with !!! using inner(). Go for it!

Instructions
-Complete the function header of the nested function with the function name inner()
and a single parameter word.
-Complete the return value: each element of the tuple should be a call to inner(),
passing in the parameters from three_shouts() as arguments to each call.
'''
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2) ,inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
