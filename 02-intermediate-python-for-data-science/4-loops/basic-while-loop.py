'''
Basic while loop
100xp
Below you can find the example from the video where the error variable, initially equal to 50.0,
is divided by 4 and printed out on every run:

error = 50.0
while error > 1 :
    error = error / 4
    print(error)
This example will come in handy, because it's time to build a while loop yourself! We're going to
code a while loop that implements a very basic control system for a inverted pendulum. If there's
an offset from standing perfectly straight, the while loop will incrementally fix this offset.

Instructions
-Create the variable offset with an initial value of 8.
-Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
    -Print out the sentence "correcting...".
    -Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
    -Finally, print out offset so you can see how it changes.
'''
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
