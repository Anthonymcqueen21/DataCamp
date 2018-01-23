'''
Build a Query to Determine the Average Age by Population

In this exercise, you will use the func.sum() and group_by() methods to first determine the average age weighted by the population in 2008, and then group by sex.

As Jason discussed in the video, a weighted average is calculated as the sum of the product of the weights and averages divided by the sum of all the weights.

For example, the following statement determines the average age weighted by the population in 2000:

stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2000 * census.columns.age) /
                func.sum(census.columns.pop2000)).label('average_age')
               ])
INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import select from sqlalchemy.
Build a statement to:
Select sex from the census table.
Select the average age weighted by the population in 2008 (pop2008). See the example given in the assignment text to see how you can do this. Label this average age calculation as 'average_age'.
Group the query by sex.
Execute the query and store it as results.
Loop over results and print the sex and average_age for each record.
'''
# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2008 * census.columns.age) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for result in results:
    print(result.sex, result.average_age)