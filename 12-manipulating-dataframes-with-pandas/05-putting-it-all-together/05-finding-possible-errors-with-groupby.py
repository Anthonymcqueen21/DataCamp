'''
Finding possible errors with .groupby()

You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.

You will see that there is only one suspicious row: This is likely a data error.

The DataFrame is available to you as medals.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Group medals by 'Event_gender' and 'Gender'.
Create a medal_count_by_gender DataFrame with a group count using the .count() method.
Print medal_count_by_gender. This has been done for you, so hit 'Submit Answer' to view the result.
'''
# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender', 'Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)
