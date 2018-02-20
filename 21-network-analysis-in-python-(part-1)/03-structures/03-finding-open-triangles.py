'''
Finding open triangles

Let us now move on to finding open triangles! Recall that they form the basis of friend recommendation systems; if "A" knows "B" and "A" knows "C", then it's probable that "B" also knows "C".

INSTRUCTIONS
70XP
Write a function node_in_open_triangle() that has two parameters - G and n - and identifies whether a node is present in an open triangle with its neighbors.
In the for loop, iterate over all possible triangle relationship combinations.
If the nodes n1 and n2 do not have an edge between them, set in_open_triangle to True, break out from the if statement and return in_open_triangle.
Use this function to count the number of open triangles that exist in T.
In the for loop, iterate over all the nodes in T.
If the current node n is in an open triangle, increment num_open_triangles.
'''
from itertools import combinations

# Define node_in_open_triangle()
def node_in_open_triangle(G, n):
    """
    Checks whether pairs of neighbors of node `n` in graph `G` are in an 'open triangle' relationship with node `n`.
    """
    in_open_triangle = False
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):
    
        # Check if n1 and n2 do NOT have an edge between them
        if not G.has_edge(n1, n2):
        
            in_open_triangle = True
            
            break
            
    return in_open_triangle

# Compute the number of open triangles in T
num_open_triangles = 0

# Iterate over all the nodes in T
for n in T.nodes():

    # Check if the current node is in an open triangle
    if node_in_open_triangle(T, n):
    
        # Increment num_open_triangles
        num_open_triangles += 1
        
print(num_open_triangles)