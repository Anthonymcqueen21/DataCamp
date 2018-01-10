'''
Building DataFrames with broadcasting

You can implicitly use 'broadcasting', a feature of NumPy, when creating pandas DataFrames. In this exercise, you're going to create a DataFrame of cities in Pennsylvania that contains the city name in one column and the state name in the second. We have imported the names of 15 cities as the list cities.

Your job is construct a DataFrame from the list of cities and the string 'PA'.

INSTRUCTIONS
100XP
-Make a string object with the value 'PA' and assign it to state.
-Construct a dictionary with 2 key:value pairs: 'state':state and 'city':cities.
-Construct a pandas DataFrame from the dictionary you created and assign it to df.
'''
# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
