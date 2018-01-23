'''
Build a Query to Determine the Percentage of Population by Gender and State

In this exercise, you will write a query to determine the percentage of the population in 2000 that comprised of women. You will group this query by state.

INSTRUCTIONS
0XP
INSTRUCTIONS
0XP
Import case, cast and Float from sqlalchemy.
Define a statement to select state and the percentage of females in 2000.
Inside func.sum(), use case() to select females (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
To get the percentage, divide the number of females in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
Group the query by state.
Execute the query and store it as results.
Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.
'''
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)
