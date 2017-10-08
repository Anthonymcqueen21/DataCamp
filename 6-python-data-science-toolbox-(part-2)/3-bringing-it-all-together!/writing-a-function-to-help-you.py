'''
Writing a function to help you
100xp

Suppose you needed to repeat the same process done in the previous exercise to many,
many rows of data. Rewriting your code again and again could become very tedious,
repetitive, and unmaintainable.

In this exercise, you will create a function to house the code you wrote earlier to
make things easier and much more concise. Why? This way, you only need to call the
function and supply the appropriate lists to create your dictionaries! Again, the
lists feature_names and row_vals are preloaded and these contain the header names of
the dataset and actual values of a row from the dataset, respectively.

Instructions
-Define the function lists2dict() with two parameters: first is list1 and second is list2.
-Return the resulting dictionary rs_dict in lists2dict().
-Call the lists2dict() function with the arguments feature_names and row_vals. Assign
the result of the function call to rs_fxn.
'''
# Pre-defined lists
feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB',
                'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', 
                '1960', '133.56090740552298']

# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)
