'''
Many-to-1 data merge

In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. That is, one of the keys in the merge is not unique.

Here, the two DataFrames site and visited have been pre-loaded once again. Note that this time, visited has multiple entries for the site column. Confirm this by exploring it in the IPython Shell.

The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be different.

INSTRUCTIONS
100XP
-Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous exercise.
-Print the merged DataFrame and then hit 'Submit Answer' to see the different output produced by this merge!
'''
# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print m2o
print(m2o)
