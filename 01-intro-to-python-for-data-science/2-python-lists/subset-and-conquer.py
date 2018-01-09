'''
Subset and conquer
100xp
Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and
then selects "b" from it. Remember that this is the second element, so it has index 1. You can also
use negative indexing.

x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
Remember the areas list from before, containing both strings and floats? Its definition is already
in the script. Can you add the correct code to do some Python subsetting?

Instructions
Print out the second element from the areas list, so 11.25.
Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
Select the number representing the area of the living room and print it out.
'''
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
