'''
Functions with one default argument
100xp

In the previous chapter, you've learned to define functions with more than one parameter
and then calling those functions by passing the required number of arguments. In the last
video, Hugo built on this idea by showing you how to define functions with default arguments.
You will practice that skill in this exercise by writing a function that uses a default argument
and then calling the function a couple of times.

Instructions
-Complete the function header with the function name shout_echo. It accepts an argument word1
and a default argument echo with default value 1, in that order.
-Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
-Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
-Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo.
Assign the result to with_echo.
'''
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)
