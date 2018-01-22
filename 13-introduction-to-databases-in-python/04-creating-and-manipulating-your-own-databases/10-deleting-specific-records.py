'''
Deleting specific records

By using a where() clause, you can target the delete statement to remove only certain records. For example, Jason deleted all columns from the employees table that had id 3 with the following delete statement:

delete(employees).where(employees.columns.id == 3) 
Here you'll delete ALL rows which have 'M' in the sex column and 36 in the age column. We have included code at the start which computes the total number of these rows. It is important to make sure that this is the number of rows that you actually delete.

INSTRUCTIONS
0XP
INSTRUCTIONS
0XP
Build a delete statement to remove data from the census table. Save it as stmt_del.
Append a where clause to stmt_del that contains an and_ to filter for rows which have 'M' in the sex column AND 36 in the age column.
Execute the delete statement.
Hit 'Submit Answer' to print the rowcount of the results, as well as to_delete, which returns the number of rows that should be deleted. These should match and this is an important sanity check!
'''
# Build a statement to count records using the sex column for Men (M) age 36: stmt
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(stmt).scalar()

# Build a statement to delete records for Men (M) age 36: stmt
stmt_del = delete(census)

# Append a where clause to target man age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)
