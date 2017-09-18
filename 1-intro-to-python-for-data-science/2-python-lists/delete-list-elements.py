'''
Delete list elements
50xp
Finally, you can also remove elements from your list. You can do this with the del statement:

x = ["a", "b", "c", "d"]
del(x[1])
Pay attention here: as soon as you remove an element from a list, the indexes of the elements that
come after the deleted element all change!

The updated and extended version of areas that you've built in the previous exercises is coded below.

You can copy and paste this into the IPython Shell to play around with the result.

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
There was a mistake! The amount you won with the lottery is not that big after all and it looks like
the poolhouse isn't going to happen. You decide to remove the corresponding string and float from
the areas list.

The ; sign is used to place commands on the same line. The following two code chunks are equivalent:

# Same line
command1; command2

# Separate lines
command1
command2
Which of the code chunks will do the job for us?

Possible Answers
del(areas[10]); del(areas[11])
del(areas[10:11])
del(areas[-4:-2])
del(areas[-3]); del(areas[-4])
'''

areas = ["hallway", 11.25, "kitchen", 18.0,
         "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# del(areas[-4:-2])