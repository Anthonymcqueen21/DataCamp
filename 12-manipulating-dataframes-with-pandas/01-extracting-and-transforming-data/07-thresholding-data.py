'''
Thresholding data

In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county. Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.

As before, the DataFrame is available to you as election with the index set to 'county'.

INSTRUCTIONS
100XP
Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.
Print the filtered DataFrame. This has been done for you, so hit 'Submit Answer' to see it!
'''
# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)
