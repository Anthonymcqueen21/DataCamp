'''
Baseball player's BMI
100xp
The MLB also offers to let you analyze their weight data. Again, both are available as regular
Python lists: height and weight. height is in inches and weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert height to
a numpy array with the correct units is already available in the workspace. Follow the instructions
step by step and finish the game!

Instructions
-Create a numpy array from the weight list with the correct units. Multiply by 0.453592 to go from
pounds to kilograms. Store the resulting numpy array as np_weight_kg.
-Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
BMI=weight(kg)height(m)2
Save the resulting numpy array as bmi.
-Print out bmi.
'''
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])