'''
Create list with different types
100xp
A list can contain any Python type. Although it's not really common, a list can also contain a mix
of Python types including strings, floats, booleans, etc.

The printout of the previous exercise wasn't really satisfying. It's just a list of numbers
representing the areas, but you can't tell which area corresponds to which part of your house.

The code on the right is the start of a solution. For some of the areas, the name of the
corresponding room is already placed in front. Pay attention here! "bathroom" is a string,
while bath is a variable that represents the float 9.50 you specified earlier.

Instructions
Finish the line of code that creates the areas list such that the list first contains the name
of each room as a string and then its area. More specifically, add the strings "hallway", "kitchen"
and "bedroom" at the appropriate locations.

Print areas again; is the printout more informative this time?
'''
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

