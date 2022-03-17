'''
Compute number of neighbors for each node

How do you evaluate whether a node is an important one or not? There are a few ways to do so, and here, you're going to look at one metric: the number of neighbors that a node has.

Every NetworkX graph G exposes a .neighbors(n) method that returns a list of nodes that are the neighbors of the node n. To begin, use this method in the IPython Shell on the Twitter network T to get the neighbors of of node 1. This will get you familiar with how the function works. Then, your job in this exercise is to write a function that returns all nodes that have m neighbors.

INSTRUCTIONS
100XP
Write a function called nodes_with_m_nbrs() that has two parameters - G and m - and returns all nodes that have m neighbors. To do this:
Iterate over all nodes in G (not including the metadata).
Use the len() function together with the .neighbors() method to calculate the total number of neighbors that node n in graph G has.
If the number of neighbors of node n is equal to m, add n to the set nodes using the .add() method.
After iterating over all the nodes in G, return the set nodes.
Use your nodes_with_m_nbrs() function to retrieve all the nodes that have 6 neighbors in the graph T.
'''
# Define nodes_with_m_nbrs()
def nodes_with_m_nbrs(G, m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()
    
    # Iterate over all nodes in G
    for n in G.nodes():
    
        # Check if the number of neighbors of n matches m
        if len(G.neighbors(n)) == m:
        
            # Add the node n to the set
            nodes.add(n)
            
    # Return the nodes with m neighbors
    return nodes

# Compute and print all nodes in T that have 6 neighbors
six_nbrs = nodes_with_m_nbrs(T, 6)
print(six_nbrs)
