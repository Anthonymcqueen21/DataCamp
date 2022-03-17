'''
Visualizing using Arc plots

Following on what you've learned about the nxviz API, now try making an ArcPlot of the network. Two keyword arguments that you will try here are node_order='keyX' and node_color='keyX', in which you specify a key in the node metadata dictionary to color and order the nodes by.

matplotlib.pyplot has been imported for you as plt.

INSTRUCTIONS
100XP
Import ArcPlot from nxviz.
Create an un-customized ArcPlot of T. To do this, use the ArcPlot() function with just T as the argument.
Create another ArcPlot of T in which the nodes are ordered and colored by the 'category' keyword. You'll have to specify the node_order and node_color parameters to do this. For both plots, be sure to draw them to the screen and display them with plt.show().
'''
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import ArcPlot

# Create the un-customized ArcPlot object: a
a = ArcPlot(T)

# Draw a to the screen
a.draw()

# Display the plot
plt.show()

# Create the customized ArcPlot object: a2
a2 = ArcPlot(T, node_order= 'category', node_color= 'category')

# Draw a2 to the screen
a2.draw()

# Display the plot
plt.show()
