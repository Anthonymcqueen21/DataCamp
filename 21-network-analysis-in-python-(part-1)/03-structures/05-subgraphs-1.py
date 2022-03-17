'''
Subgraphs I

There may be times when you just want to analyze a subset of nodes in a network. To do so, you can copy them out into another graph object using G.subgraph(nodes), which returns a new graph object (of the same type as the original graph) that is comprised of the iterable of nodes that was passed in.

matplotlib.pyplot has been imported for you as plt.

INSTRUCTIONS
100XP
Write a function get_nodes_and_nbrs(G, nodes_of_interest) that extracts the subgraph from graph G comprised of the nodes_of_interest and their neighbors.
In the first for loop, iterate over nodes_of_interest and append the current node n to nodes_to_draw.
In the second for loop, iterate over the neighbors of n, and append all the neighbors nbr to nodes_to_draw.
Use the function to extract the subgraph from T comprised of nodes 29, 38, and 42 (contained in the pre-defined list nodes_of_interest) and their neighbors. Save the result as T_draw.
Draw the subgraph T_draw to the screen.
'''
nodes_of_interest = [29, 38, 42]  # provided.

# Define get_nodes_and_nbrs()
def get_nodes_and_nbrs(G, nodes_of_interest):
    """
    Returns a subgraph of the graph `G` with only the `nodes_of_interest` and their neighbors.
    """
    nodes_to_draw = []
    
    # Iterate over the nodes of interest
    for n in nodes_of_interest:
    
        # Append the nodes of interest to nodes_to_draw
        nodes_to_draw.append(n)
        
        # Iterate over all the neighbors of node n
        for nbr in G.neighbors(n):
        
            # Append the neighbors of n to nodes_to_draw
            nodes_to_draw.append(nbr)
            
    return G.subgraph(nodes_to_draw)

# Extract the subgraph with the nodes of interest: T_draw
T_draw = get_nodes_and_nbrs(T, nodes_of_interest)

# Draw the subgraph to the screen
nx.draw(T_draw)
plt.show()