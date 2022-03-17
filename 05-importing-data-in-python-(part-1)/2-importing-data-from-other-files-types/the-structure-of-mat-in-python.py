'''
The structure of .mat in Python
100xp
Here, you'll discover what is in the MATLAB dictionary that you loaded in the 
previous exercise.

The file 'albeck_gene_expression.mat' is already loaded into the variable mat.
The following libraries have already been imported as follows:

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

Once again, this file contains gene expression data from the Albeck Lab at UCDavis.
You can find the data and some great documentation here.

Instructions
-Use the method .keys() on the dictionary mat to print the keys. Most of these keys
(in fact the ones that do NOT begin and end with '__') are variables from the
corresponding MATLAB environment.
-Print the type of the value corresponding to the key 'CYratioCyt' in mat. Recall
that mat['CYratioCyt'] accesses the value.
-Print the shape of the value corresponding to the key 'CYratioCyt' using the numpy
function shape().
-Execute the entire script to see some oscillatory gene expression data!
'''
# Import package
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load MATLAB file: mat
mat = scipy.io.loadmat('../_datasets/albeck_gene_expression.mat')

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
