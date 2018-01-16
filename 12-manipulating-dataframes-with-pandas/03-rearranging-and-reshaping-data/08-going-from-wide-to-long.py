'''
Going from wide to long

You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns. In this exercise, you will practice doing this.

The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.

INSTRUCTIONS
70XP
Define a DataFrame skinny where you melt the 'visitors' and 'signups' columns of users into a single column.
Print skinny to verify the results. Note the value column that had the cell values in users.
'''
# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday','city'])

# Print skinny
print(skinny)
