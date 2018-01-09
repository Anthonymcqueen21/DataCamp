'''
Pop quiz about errors
50xp
In the video, Hugo talked about how errors happen when functions are supplied
arguments that they are unable to work with. In this exercise, you will identify
which function call raises an error and what type of error is raised.

Take a look at the following function calls to len():

len('There is a beast in every man and it stirs when you put a sword in his hand.')

len(['robb', 'sansa', 'arya', 'eddard', 'jon'])

len(525600)

len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
Which of the function calls raises an error and what type of error is raised?

Possible Answers
-The call len('There is a beast in every man and it stirs when you put a sword in his
hand.') raises a TypeError.
-The call len(['robb', 'sansa', 'arya', 'eddard', 'jon']) raises an IndexError.
-The call len(525600) raises a TypeError.
-The call len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey')) raises a NameError.
'''
# The call len(525600) raises a TypeError.