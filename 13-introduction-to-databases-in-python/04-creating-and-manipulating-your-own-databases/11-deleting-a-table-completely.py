'''
eleting a Table Completely

You're now going to practice dropping individual tables from a database with the .drop() method, as well as all tables in a database with the .drop_all() method!

As Spider-Man's Uncle Ben (as well as Jason, in the video!) said: With great power, comes great responsibility. Do be careful when deleting tables, as it's not simple or fast to restore large databases! Remember, you can check to see if a table exists with the .exists() method.

This is the final exercise in this chapter: After this, you'll be ready to apply everything you've learned to a case study in the final chapter of this course!

INSTRUCTIONS
0XP
INSTRUCTIONS
0XP
Drop the state_fact table by applying the method .drop() to it and passing it the argument engine (in fact, engine will be the sole argument for every function/method in this exercise!)
Check to see if state_fact exists via print. Use the .exists() method with engine as the argument.
Drop all the tables via the metadata using the .drop_all() method.
Use a print statement to check if the census table exists.
'''
# Drop the state_fact tables
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
