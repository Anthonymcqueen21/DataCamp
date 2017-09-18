'''
List of lists
100xp
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group
some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas
of the rooms in your house, you can create a list of lists. The script on the right can already
give you an idea.

Don't get confused here: "hallway" is a string, while hall is a variable that represents the float
11.25 you specified earlier.

Instructions
Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter
these in order!
Print out house; does this way of structuring your data make more sense?
Print out the type of house. Are you still dealing with a list?
'''
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(house)
print(type(house))
