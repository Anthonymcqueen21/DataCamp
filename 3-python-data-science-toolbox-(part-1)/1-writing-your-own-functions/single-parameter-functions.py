'''
Single-parameter functions
100xp
Congratulations! You have successfully defined and called your own function!
That's pretty cool.

In the previous exercise, you defined and called the function shout(), which
printed out a string concatenated with '!!!'. You will now update shout() by
adding a parameter so that it can accept and process any string argument passed
to it. Also note that shout(word), the part of the header that specifies the
function name and parameter(s), is known as the signature of the function.
You may encounter this term in the wild!

Instructions
-Complete the function header by adding the parameter name, word.
-Assign the result of concatenating word with '!!!' to shout_word.
-Print the value of shout_word.
-Call the shout() function, passing to it the string, 'congratulations'.
'''
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')
