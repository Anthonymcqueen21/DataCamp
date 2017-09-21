'''
Using File to import HDF5 files
50xp
The h5py package has been imported in the environment and the file LIGO_data.hdf5 is loaded in the object h5py_file.

What is the correct way of using the h5py function, File(), to import the file in h5py_file into an object, h5py_data, for reading only?

Possible Answers
-h5py_data = File(h5py_file, 'r')
-h5py_data = h5py.File(h5py_file, 'r')
-h5py_data = h5py.File(h5py_file, read)
-h5py_data = h5py.File(h5py_file, 'read')
'''
import h5py

filename = '../_datasets/LIGO_data.hdf5'

h5py_data = h5py.File(filename, 'r')

print(type(h5py_data))
