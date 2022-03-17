'''
Characterizing the network (II)

Let's continue recalling what you've learned before about node importances, by plotting the degree distribution of a network. This is the distribution of node degrees computed across all nodes in a network.

INSTRUCTIONS
100XP
Plot the degree distribution of the GitHub collaboration network G. Recall that there are four steps involved here:
Calculating the degree centrality of G.
Using the .values() method of G and converting it into a list.
Passing the list of degree distributions to plt.hist().
Displaying the histogram with plt.show().
'''
# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx 

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()
