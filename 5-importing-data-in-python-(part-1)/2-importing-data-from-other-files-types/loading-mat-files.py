'''
Loading .mat files
100xp
In this exercise, you'll figure out how to load a MATLAB file using scipy.io.loadmat()
and you'll discover what Python datatype it yields.

The file 'albeck_gene_expression.mat' is in your working directory. This file contains
gene expression data from the Albeck Lab at UC Davis. You can find the data and some
great documentation here.

Instructions
-Import the package scipy.io.
-Load the file 'albeck_gene_expression.mat' into the variable mat; do so using the
function scipy.io.loadmat().
-Use the function type() to print the datatype of mat to the IPython shell.
'''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('../_datasets/albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
