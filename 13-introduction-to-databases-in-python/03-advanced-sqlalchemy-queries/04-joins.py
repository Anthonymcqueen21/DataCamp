'''
Joins

If you aren't selecting columns from both tables or the two tables don't have a defined relationship, you can still use the .join() method on a table to join it with another table and get extra data related to our query. The join() takes the table object you want to join in as the first argument and a condition that indicates how the tables are related to the second argument. Finally, you use the .select_from() method on the select statement to wrap the join clause. For example, in the video, Jason executed the following code to join the census table to the state_fact table such that the state column of the census table corresponded to the name column of the state_fact table.

stmt = stmt.select_from(
    census.join(
        state_fact, census.columns.state == 
        state_fact.columns.name)
INSTRUCTIONS
100XP
Build a statement to select ALL the columns from the census and state_fact tables. To select ALL the columns from two tables employees and sales, for example, you would use stmt = select([employees, sales]).
Append a select_from to stmt to join the census table to the state_fact table by the state column in census and the name column in the state_fact table.
Execute the statement to get the first result and save it as result. This code is already written.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!
'''
# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))
