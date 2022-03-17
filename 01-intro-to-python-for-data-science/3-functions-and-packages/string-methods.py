'''
String Methods
100xp
Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If
you want to discover them in more detail, you can always type help(str) in the IPython Shell.

A string room has already been created for you to experiment with.

Instructions
-Use the upper() method on room and store the result in room_up. Use the dot notation.
-Print out room and room_up. Did both change?
-Print out the number of o's on the variable room by calling count() on room and passing the
letter "o" as an input to the method. We're talking about the variable room, not the word "room"!
'''
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count('o'))