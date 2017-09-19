'''
Blend it all together
100xp
In the last few exercises you've learned everything there is to know about heights
and weights of baseball players. Now it's time to dive into another sport: soccer.

You've contacted FIFA for some data and they handed you two lists. The lists are the
following: positions = ['GK', 'M', 'A', 'D', ...] heights = [191, 184, 185, 180, ...]
Each element in the lists corresponds to a player. The first list, positions, contains
strings representing each player's position. The possible positions are: 'GK' (goalkeeper),
'M' (midfield), 'A' (attack) and 'D' (defense). The second list, heights, contains integers
representing the height of the player in cm. The first player in the lists is a goalkeeper
and is pretty tall (191 cm).

You're fairly confident that the median height of goalkeepers is higher than that of other
players on the soccer field. Some of your friends don't believe you, so you are determined
to show them using the data you received from FIFA and your newly acquired Python skills.

Instructions
-Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights
and np_positions.
-Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions
== 'GK' as an index for np_heights. Assign the result to gk_heights.
-Extract all the heights of all the other players. This time use np_positions != 'GK' as an
index for np_heights. Assign the result to other_heights.
-Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
-Do the same for the other players. Print out their median height. Replace None with the correct code.
'''
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)


# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']


# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
