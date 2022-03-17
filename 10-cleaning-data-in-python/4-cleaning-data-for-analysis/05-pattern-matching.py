'''
Pattern matching

In this exercise, you'll continue practicing your regular expression skills. For each provided string, your job is to write the appropriate pattern to match it.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Write patterns to match:
    -A telephone number of the format xxx-xxx-xxxx. You already did this in a previous exercise.
    -A string of the format: A dollar sign, an arbitrary number of digits, a decimal point, 2 digits.
        -Use \$ to match the dollar sign, \d* to match an arbitrary number of digits, \. to match the decimal point, and \d{x} to match x number of digits.
-A capital letter, followed by an arbitrary number of alphanumeric characters.
    -Use [A-Z] to match any capital letter followed by \w* to match an arbitrary number of alphanumeric characters.
'''
import re

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='^\$\d*\.\d{2}$', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='w*', string='Australia'))
print(pattern3)
