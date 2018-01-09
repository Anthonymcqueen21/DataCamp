'''
Resetting the index of a DataFrame

After pivoting airquality_melt in the previous exercise, you didn't quite get back the original
DataFrame.

What you got back instead was a pandas DataFrame with a hierarchical index (also known as a
MultiIndex).

Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence,
they allow you to group columns or rows by another variable - in this case, by 'Month' as
well as 'Day'.

There's a very simple method you can use to get back the original DataFrame from the pivoted
DataFrame: .reset_index(). Dan didn't show you how to use this method in the video, but you're
now going to practice using it in this exercise to get back the original DataFrame from
airquality_pivot, which has been pre-loaded.

INSTRUCTIONS
100XP
-Print the index of airquality_pivot by accessing its .index attribute. This has been done for you.
-Reset the index of airquality_pivot using its .reset_index() method.
-Print the new index of airquality_pivot.
-Print the head of airquality_pivot.
'''
# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())