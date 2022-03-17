'''
Recommending co-editors who have yet to edit together

Finally, you're going to leverage the concept of open triangles to recommend users on GitHub to collaborate!

INSTRUCTIONS
100XP
Compile a list of GitHub users that should be recommended to collaborate with one another. To do this:
In the first for loop, iterate over all the nodes in G, including the metadata (by specifying data=True).
In the second for loop, iterate over all the possible triangle combinations, which can be identified using the combinations() function with a size of 2.
If n1 and n2 do not have an edge between them, a collaboration between these two nodes (users) should be recommended, so increment the (n1), (n2) value of the recommended dictionary in this case. You can check whether or not n1 and n2 have an edge between them using the .has_edge() method.
Using a list comprehension, identify the top 10 pairs of users that should be recommended to collaborate. The iterable should be the key-value pairs of the recommended dictionary (which can be accessed with the .items() method), while the conditional should be satisfied if count is greater than the top 10 in all_counts. Note that all_counts is sorted in ascending order, so you can access the top 10 with all_counts[-10].
'''
# Import necessary modules
from itertools import combinations
from collections import defaultdict

# Initialize the defaultdict: recommended
recommended = defaultdict(int)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):
    
        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):
        
            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)
