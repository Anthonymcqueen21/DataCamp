'''
Finding important collaborators

Almost there! You'll now look at important nodes once more. Here, you'll make use of the degree_centrality() and betweenness_centrality() functions in NetworkX to compute each of the respective centrality scores, and then use that information to find the "important nodes". In other words, your job in this exercise is to find the user(s) that have collaborated with the most number of users.

INSTRUCTIONS
70XP
Compute the degree centralities of G. Store the result as deg_cent.
Compute the maximum degree centrality. Since deg_cent is a dictionary, you'll have to use the .values() method to get a list of its values before computing the maximum degree centrality with max().
Identify the most prolific collaborators using a list comprehension:
Iterate over the degree centrality dictionary deg_cent that was computed earlier using its .items() method. What condition should be satisfied if you are seeking to find user(s) that have collaborated with the most number of users? Hint: It has do to with the maximum degree centrality.
Hit 'Submit Answer' to see who the most prolific collaborator(s) is/are!
'''
# Compute the degree centralities of G: deg_cent
deg_cent = nx.degree_centrality(G)

# Compute the maximum degree centrality: max_dc
max_dc = max(deg_cent.values())

# Find the user(s) that have collaborated the most: prolific_collaborators
prolific_collaborators = [n for n, dc in deg_cent.items() if deg_cent == max_dc]

# Print the most prolific collaborator(s)
print(prolific_collaborators)