'''
Dictionaries for data science
100xp

For this exercise, you'll use what you've learned about the zip() function and combine two
lists into a dictionary.

These lists are actually extracted from a bigger dataset file of world development indicators
from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists
that you'll be working with.

The first list feature_names contains header names of the dataset and the second list row_vals
contains actual values of a row from the dataset, corresponding to each of the header names.

Instructions
-Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the
result to zipped_lists.
-Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists.
Assign the resulting dictionary to rs_dict.
'''
# Pre-defined lists
feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB',
                'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT',
                '1960', '133.56090740552298']

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)
