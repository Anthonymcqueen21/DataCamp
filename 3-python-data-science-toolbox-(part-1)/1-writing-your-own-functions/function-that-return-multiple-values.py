'''
Function that return multiple values
100xp

In the previous exercise, you constructed tuples, assigned tuples to variables,
and unpacked tuples. Here you will return multiple values from a function using
tuples. Let's now update our shout() function to return multiple values.
Instead of returning just one string, we will return two strings with the
string !!! concatenated to each.

Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!

Instructions
-Modify the function header such that the function name is now shout_all, and it accepts
two parameters, word1 and word2, in that order.
-Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2,
respectively.
-Construct a tuple shout_words, composed of shout1 and shout2.
-Call shout_all() with the strings 'congratulations' and 'you' and assign the result to
yell1 and yell2 (remember, shout_all returns 2 variables!).
'''

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)
