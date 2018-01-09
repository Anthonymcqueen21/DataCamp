'''
Error handling by raising an error
100xp

Another way to raise an error is by using raise. In this exercise, you will
add a raise statement to the shout_echo() function you defined before to raise
an error message when the value supplied by the user to the echo argument is
less than 0.

The call to shout_echo() uses valid argument values. To test and see how the
raise statement works, simply change the value for the echo argument to a
negative value. Don't forget to change it back to valid values to move on to
the next exercise!

Instructions
-Complete the if statement by checking if the value of echo is less than 0.
-In the body of the if statement, add a raise statement that raises the error
message 'echo must be greater than 0' when the value supplied by the user to
echo is less than 0.
'''
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)
