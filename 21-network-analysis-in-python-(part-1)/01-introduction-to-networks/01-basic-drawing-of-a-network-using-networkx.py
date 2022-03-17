'''
Basic drawing of a network using NetworkX

NetworkX provides some basic drawing functionality that works for small graphs. We have selected a subset of nodes from the graph for you to practice using NetworkX's drawing facilities. It has been pre-loaded as T_sub.

INSTRUCTIONS
100XP
Import matplotlib.pyplot as plt and networkx as nx.
Draw T_sub to the screen by using the nx.draw() function, and don't forget to also use plt.show() to display it.
'''
# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Draw the graph to screen
nx.draw(T_sub)
plt.show()
