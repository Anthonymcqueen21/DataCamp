'''
The keyword global
100xp
Let's work more on your mastery of scope. In this exercise, you will use the keyword
global within a function to alter the value of a variable defined in the global scope.

Instructions
-Use the keyword global to alter the object team in the global scope.
-Change the value of team in the global scope to the string "justice league".
Assign the result to team.
-Hit the Submit button to see how executing your newly defined function change_team()
changes the value of the name team!
'''
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

