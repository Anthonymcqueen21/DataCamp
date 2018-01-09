'''
The keyword nonlocal and nested functions
100xp
Let's once again work further on your mastery of scope! In this exercise,
you will use the keyword nonlocal within a nested function to alter the value
of a variable defined in the enclosing scope.

Instructions
-Assign to echo_word the string word, concatenated with itself.
-Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
-Alter echo_word to echo_word concatenated with '!!!'.
-Call the function echo_shout(), passing it a single argument 'hello'.
'''
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    
    #Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        #Use echo_word in nonlocal scope
        nonlocal echo_word
        
        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    #Print echo_word
    print(echo_word)

#Call function echo_shout() with argument 'hello'    
echo_shout('hello')