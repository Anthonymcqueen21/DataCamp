'''
Grouping by multiple columns

In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.

The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.

Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.

The DataFrame has been pre-loaded as titanic.

INSTRUCTIONS
0XP
Group by the 'pclass' column and save the result as by_class.
Aggregate the 'survived' column of by_class using .count(). Save the result as count_by_class.
Print count_by_class. This has been done for you.
Group titanic by the 'embarked' and 'pclass' columns. Save the result as by_mult.
Aggregate the 'survived' column of by_mult using .count(). Save the result as count_mult.
Print count_mult. This has been done for you, so hit 'Submit Answer' to view the result.
'''
# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)
