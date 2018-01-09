'''
Customize further: elif
100xp
It's also possible to have a look around in the bedroom. The sample code contains an
elif part that checks if room equals "bed". In that case, "looking around in the bedroom."
is printed out.

It's up to you now! Make a similar addition to the second control structure to further
customize the messages for different values of area.

Instructions
Add an elif to the second control structure such that "medium size, nice!" is printed out
if area is greater than 10.
'''
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
