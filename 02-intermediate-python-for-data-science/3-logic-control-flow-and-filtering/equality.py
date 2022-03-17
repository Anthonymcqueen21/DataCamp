'''
Equality
100xp
To check if two Python values, or variables, are equal you can use ==.
To check for inequality, you need !=. As a refresher, have a look at the following
examples that all result in True. Feel free to try them out in the IPython Shell.

2 == (1 + 1)
"intermediate" != "python"
True != False
"Python" != "python"

When you write these comparisons in a script, you will need to wrap a print()
function around them to see the output.

Instructions
-In the editor on the right, write code to see if True equals False.
-Write Python code to check if -5 * 15 is not equal to 75.
-Ask Python whether the strings "pyscript" and "PyScript" are equal.
-What happens if you compare booleans and integers? Write code to see if True and 1 are equal.
'''
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print('pyscript' == 'PyScript')

# Compare a boolean with an integer
print(True == 1)
