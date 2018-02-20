'''
Queries on a graph

Now that you know some basic properties of the graph and have practiced using NetworkX's drawing facilities to visualize components of it, it's time to explore how you can query it for nodes and edges. Specifically, you're going to look for "nodes of interest" and "edges of interest". To achieve this, you'll make use of the .nodes() and .edges() methods that Eric went over in the video. The .nodes() method returns a list of nodes, while the .edges() method returns a list of tuples, in which each tuple shows the nodes that are present on that edge. Recall that passing in the keyword argument data=True in these methods retrieves the corresponding metadata associated with the nodes and edges as well.

You'll write list comprehensions to effectively build these queries in one line. For a refresher on list comprehensions, refer to Part 2 of DataCamp's Python Data Science Toolbox course. Here's the recipe for a list comprehension:

[ output expression for iterator variable in iterable if predicate expression ].

You have to fill in the _iterable_ and the _predicate expression_. Feel free to prototype your answer by exploring the graph in the IPython Shell before submitting your solution.

INSTRUCTIONS
100XP
Use a list comprehension to get a list of nodes from the graph T that have the 'occupation' label of 'scientist'.
The output expression n has been specified for you, along with the iterator variables n and d. Your task is to fill in the iterable and the conditional expression.
Use the .nodes() method of T access its nodes, and be sure to specify data=True to obtain the metadata for the nodes.
The iterator variable d is a dictionary. The key of interest here is 'occupation' and value of interest is 'scientist'.
Use a list comprehension to get a list of edges from the graph T that were formed for at least 6 years, i.e., from before 1 Jan 2010.
Your task once again is to fill in the iterable and conditional expression.
Use the .edges() method of T to access its edges. Be sure to obtain the metadata for the edges as well.
The dates are stored as datetime.date objects in the metadata dictionary d, under the key 'date'. To access the date 1 Jan 2009, for example, the dictionary value would be date(2009, 1, 1).
'''
# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in T.nodes(data=True) if d['occupation'] == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in T.edges(data=True) if d['date'] < date(2010, 1, 1)]
