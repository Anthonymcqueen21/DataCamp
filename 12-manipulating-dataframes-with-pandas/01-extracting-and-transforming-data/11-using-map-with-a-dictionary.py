'''
Using .map() with a dictionary

The .map() method is used to transform values according to a Python dictionary look-up. In this exercise you'll practice this method while returning to working with the election DataFrame, which has been pre-loaded for you.

Your job is to use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' column to the values 'blue' and 'red', and assign the output to the new column 'color'.

INSTRUCTIONS
100XP
Create a dictionary with the key:value pairs 'Obama':'blue' and 'Romney':'red'.
Use the .map() method on the 'winner' column using the red_vs_blue dictionary you created.
Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to see the new column!
'''
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(red_vs_blue)

# Print the output of election.head()
print(election.head())
