'''
Pivoting duplicate values

So far, you've used the .pivot_table() method when there are multiple index values you want to
hold constant during a pivot. In the video, Dan showed you how you can also use pivot tables to
deal with duplicate values by providing an aggregation function through the aggfunc parameter.
Here, you're going to combine both these uses of pivot tables.

Let's say your data collection method accidentally duplicated your dataset. Such a dataset, in
which each row is duplicated, has been pre-loaded as airquality_dup. In addition, the
airquality_melt DataFrame from the previous exercise has been pre-loaded. Explore their shapes
in the IPython Shell by accessing their .shape attributes to confirm the duplicate rows present
in airquality_dup.

You'll see that by using .pivot_table() and the aggfunc parameter, you can not only reshape your
data, but also remove duplicates. Finally, you can then flatten the columns of the pivoted
DataFrame using .reset_index().

NumPy and pandas have been imported as np and pd respectively.

INSTRUCTIONS
100XP
-Pivot airquality_dup by using .pivot_table() with the rows indexed by 'Month' and 'Day', the columns indexed by 'measurement', and the values populated with 'reading'. Use np.mean for the aggregation function.
-Flatten airquality_pivot by resetting its index.
-Print the head of airquality_pivot and then the original airquality DataFrame to compare their structure.
'''

