'''
Add conditionals
100xp
The while loop that corrects the offset is a good start, but what if offset is negative?
You can try to run the sample code on the right where offset is initialized to -6,
but your sessions will be disconnected. The while loop will never stop running,
because offset will be further decreased on every run. offset != 0 will never become
False and the while loop continues forever.

Fix things by putting an if-else statement inside the while loop.

Instructions
-Inside the while loop, replace offset = offset - 1 by an if-else statement:
    -If offset > 0, you should decrease offset by 1.
    -Else, you should increase offset by 1.
If you've coded things correctly, hitting Submit Answer should work this time.
'''
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
