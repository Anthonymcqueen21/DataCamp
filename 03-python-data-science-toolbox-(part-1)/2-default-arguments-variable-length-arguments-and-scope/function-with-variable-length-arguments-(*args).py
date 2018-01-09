'''
Function with variable-length arguments (*args)
100xp

Flexible arguments enable you to pass a variable number of arguments to a function.
In this exercise, you will practice defining a function that accepts a variable number
of string arguments.

The function you will define is gibberish() which can accept a variable number of string
values. Its return value is a single string composed of all the string arguments concatenated
together in the order they were passed to the function call. You will call the function with
a single string argument and see how the output changes with another call using more than one
string argument. Recall from the previous video that, within the function definition, args is
a tuple.

Instructions
-Complete the function header with the function name gibberish. It accepts a single flexible
argument *args.
-Initialize a variable hodgepodge to an empty string.
-Return the variable hodgepodge at the end of the function body.
-Call gibberish() with the single string, "luke". Assign the result to one_word.
-Hit the Submit button to call gibberish() with multiple arguments and to print the value
to the Shell.
'''
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)
