'''
Nested Functions II
100xp

Great job, you've just nested a function within another function. One other pretty cool
reason for nesting functions is the idea of a closure. This means that the nested or inner
function remembers the state of its enclosing scope when called. Thus, anything defined
locally in the enclosing scope is available to the inner function even when the outer
function has finished execution.

Let's move forward then! In this exercise, you will complete the definition of the inner
function inner_echo() and then call echo() a couple of times, each with a different argument.
Complete the exercise and see what the output will be!

Instructions
-Complete the function header of the inner function with the function name inner_echo()
and a single parameter word1.
-Complete the function echo() so that it returns inner_echo.
-We have called echo(), passing 2 as an argument, and assigned the resulting function to
twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function
to thrice.
-Hit Submit to call twice() and thrice() and print the results.
'''
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
