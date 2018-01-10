'''
String parsing with regular expressions

In the video, Dan introduced you to the basics of regular expressions, which are powerful ways of
defining patterns to match strings. This exercise will get you started with writing them.

When working with data, it is sometimes necessary to write a regular expression to look for
properly entered values. Phone numbers in a dataset is a common field that needs to be checked
for validity. Your job in this exercise is to define a regular expression to match US phone
numbers that fit the pattern of xxx-xxx-xxxx.

The regular expression module in python is re. When performing pattern matching on data,
since the pattern will be used for a match across multiple rows, it's better to compile the
pattern first using re.compile(), and then use the compiled pattern to match values.

INSTRUCTIONS
100XP
Import re.
-Compile a pattern that matches a phone number of the format xxx-xxx-xxxx.
-Use \d{x} to match x digits. Here you'll need to use it three times: twice to match 3 digits,
and once to match 4 digits.
-Place the regular expression inside re.compile().
-Using the .match() method on prog, check whether the pattern matches the string '123-456-7890'.
-Using the same approach, now check whether the pattern matches the string '1123-456-7890'.
'''
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result = prog.match('1123-456-7890')
print(bool(result))
