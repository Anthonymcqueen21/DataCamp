'''
Baseball players' height
100xp
You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for
some more statistics on the height of the main players. They pass along data on more than a
thousand players, which is stored as a regular Python list: height. The height is expressed in
inches. Can you make a numpy array out of it and convert the units to meters?

height is already available and the numpy package is loaded, so you can start straight away
(Source: stat.ucla.edu).

Instructions
-Create a numpy array from height. Name this new array np_height.
-Print np_height.
-Multiply np_height with 0.0254 to convert all height measurements from inches to meters.
Store the new values in a new array, np_height_m.
-Print out np_height_m and check if the output makes sense.
'''
# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
