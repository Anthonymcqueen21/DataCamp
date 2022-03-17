'''
Functions with multiple default arguments
100xp

You've now defined a function that uses a default argument - don't stop there just yet!
You will now try your hand at defining a function with more than one default argument and
then calling this function in various ways.

After defining the function, you will call it by supplying values to all the default arguments
of the function. Additionally, you will call the function by not passing a value to one of the
default arguments - see how that changes the output of your function!

Instructions
-Complete the function header with the function name shout_echo. It accepts an argument word1,
a default argument echo with default value 1 and a default argument intense with default value
False, in that order.
-In the body of the if statement, capitalize the string object echo_word by applying the method
.upper() on it.
-Call shout_echo() with the string, "Hey", the value 5 for echo and the value True for intense.
Assign the result to with_big_echo.
-Call shout_echo() with the string "Hey" and the value True for intense. Assign the result to
big_no_echo.
'''
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', 5, True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)
