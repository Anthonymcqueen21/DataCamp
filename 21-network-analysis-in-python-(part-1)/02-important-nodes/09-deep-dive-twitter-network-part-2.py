'''
Deep dive - Twitter network part II

Next, you're going to do an analogous deep dive on betweenness centrality! Just a few hints to help you along: remember that betweenness centrality is computed using nx.betweenness_centrality(G).

INSTRUCTIONS
100XP
Write a function find_node_with_highest_bet_cent(G) that returns the node(s) with the highest betweenness centrality.
Compute the betweenness centrality of G.
Compute the maximum betweenness centrality using the max() function on list(bet_cent.values()).
Iterate over the degree centrality dictionary, bet_cent.items().
If the degree centrality value v of the current node k is equal to max_bc, add it to the set of nodes.
Use your function to find the node(s) that has the highest betweenness centrality in T.
Write an assertion statement that you've got the right node. This has been done for you, so hit 'Submit Answer' to see the result!
'''
# Define find_node_with_highest_bet_cent()
def find_node_with_highest_bet_cent(G):

    # Compute betweenness centrality: bet_cent
    bet_cent = nx.betweenness_centrality(G)
    
    # Compute maximum betweenness centrality: max_bc
    max_bc = max(list(bet_cent.values()))
    
    nodes = set()
    
    # Iterate over the betweenness centrality dictionary
    for k, v in bet_cent.items():
    
        # Check if the current value has the maximum betweenness centrality
        if v == max_bc:
        
            # Add the current node to the set of nodes
            nodes.add(k)
            
    return nodes

# Use that function to find the node(s) that has the highest betweenness centrality in the network: top_bc
top_bc = find_node_with_highest_bet_cent(T)

# Write an assertion statement that checks that the node(s) is/are correctly identified.
for node in top_bc:
    assert nx.betweenness_centrality(T)[node] == max(nx.betweenness_centrality(T).values())