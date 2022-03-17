'''
Greater and less than
100xp
In the video, Filip also talked about the less than and greater than signs, < and > in Python.
You can combine them with an equals sign: <= and >=. Pay attention: <= is valid syntax,
but =< is not.

All Python expressions in the following code chunk evaluate to True:

3 < 4
3 <= 4
"alpha" <= "beta"

Remember that for string comparison, Python determines the relationship based on alphabetical order.

Instructions
-Write Python expressions, wrapped in a print() function, to check whether:
    -x is greater than or equal to -10. x has already been defined for you.
    -"test" is less than or equal to y. y has already been defined for you.
    -True is greater than False.
'''
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
print(True > False)
