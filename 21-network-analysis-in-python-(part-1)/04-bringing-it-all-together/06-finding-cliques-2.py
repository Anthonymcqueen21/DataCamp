'''
Finding cliques (II)

Great work! Let's continue by finding a particular maximal clique, and then plotting that clique.

INSTRUCTIONS
100XP
Find the author(s) that are part of the largest maximal clique, and plot the subgraph of that/one of those clique(s) using a CircosPlot. To do this:
Use the nx.find_cliques() function to calculate the maximal cliques in G. Place this within the provided sorted() function to calculate the largest maximal clique.
Create the subgraph consisting of the largest maximal clique using the .subgraph() method and largest_clique.
Create the CircosPlot object using the subgraph G_lc (without any other arguments) and plot it.
'''
# Import necessary modules
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Find the author(s) that are part of the largest maximal clique: largest_clique
largest_clique = sorted(nx.find_cliques(G), key=lambda x:len(x))[-1]

# Create the subgraph of the largest_clique: G_lc
G_lc = G.subgraph(largest_clique)

# Create the CircosPlot object: c
c = CircosPlot(G_lc)

# Draw the CircosPlot to the screen
c.draw()
plt.show()
