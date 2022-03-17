'''
Grouping and aggregating

The Olympic medal data for the following exercises comes from The Guardian. It comprises records of all events held at the Olympic games between 1896 and 2012.

Suppose you have loaded the data into a DataFrame medals. You now want to find the total number of medals awarded to the USA per edition. To do this, filter the 'USA' rows and use the groupby() function to put the 'Edition' column on the index:

USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')
Given the goal of finding the total number of USA medals awarded per edition, what column should you select and which aggregation method should you use?

INSTRUCTIONS
50XP
Possible Answers
USA_edition_grouped['City'].mean()
press 1

USA_edition_grouped['Athlete'].sum()
press 2

USA_edition_grouped['Medal'].count()
press 3

USA_edition_grouped['Gender'].first()
press 4
'''
# USA_edition_grouped['Medal'].count()