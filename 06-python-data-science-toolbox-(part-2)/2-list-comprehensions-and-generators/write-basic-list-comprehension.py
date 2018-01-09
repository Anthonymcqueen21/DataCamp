'''
Write a basic list comprehension
50xp
In this exercise, you will practice what you've learned from the video about writing
list comprehensions. You will write a list comprehension and identify the output that
will be produced.

The following list has been pre-loaded in the environment.

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
How would a list comprehension that produces a list of the first character of each string
in doctor look like? Note that the list comprehension uses doc as the iterator variable.
What will the output be?

Possible Answers
-The list comprehension is [for doc in doctor: doc[0]] and produces the list ['h', 'c', 'c', 't', 'w'].
-The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
-The list comprehension is [doc[0] in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
'''
# The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].