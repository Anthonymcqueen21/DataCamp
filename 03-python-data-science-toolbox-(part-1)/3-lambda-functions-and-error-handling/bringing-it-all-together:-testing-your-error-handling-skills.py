'''
Bringing it all together: testing your error handling skills
50xp
You have just written error handling into your count_entries() function so that, when the user passes the function a column (as 2nd argument) NOT contained in the DataFrame (1st argument), a ValueError is thrown. You're now going to play with this function: it is loaded into pre-exercise code, as is the DataFrame tweets_df. Try calling count_entries(tweets_df, 'lang') to confirm that the function behaves as it should. Then call count_entries(tweets_df, 'lang1'): what is the last line of the output?

Possible Answers
-'ValueError: The DataFrame does not have the requested column.'
-'ValueError: The DataFrame does not have a lang1 column.'
-'TypeError: The DataFrame does not have the requested column.'
'''
# ValueError: The DataFrame does not have a lang1 column.
