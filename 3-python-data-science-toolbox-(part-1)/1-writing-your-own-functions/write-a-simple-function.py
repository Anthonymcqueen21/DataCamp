'''
Write a simple function
100xp
In the last video, Hugo described the basics of how to define a function.
You will now write your own function!

Define a function, shout(), which simply prints out a string with three
exclamation marks '!!!' at the end. The code for the square() function that we
wrote earlier is found below. You can use it as a pattern to define shout().

def square():
    new_value = 4 ** 2
    return new_value
Note that the function body is indented 4 spaces already for you. Function bodies
need to be indented by a consistent number of spaces and the choice of 4 is common.

Instructions
-Complete the function header by adding the appropriate function name, shout.
-In the function body, concatenate the string, 'congratulations' with another string,
'!!!'. Assign the result to shout_word.
-Print the value of shout_word.
-Call the shout function.
'''
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()
