'''
NumPy Side Effects
50xp
As Filip explained before, numpy is great for doing vector arithmetic. If you compare its
functionality with regular Python lists, however, some things have changed.

First of all, numpy arrays cannot contain elements with different types. If you try to build
such a list, some of the elements' types are changed to end up with a homogeneous list. This
is known as type coercion.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for
regular Python lists and numpy arrays.

Have a look at this line of code:

np.array([True, 1, 2]) + np.array([3, 4, False])
Can you tell which code chunk builds the exact same Python object? The numpy package is already
imported as np, so you can start experimenting in the IPython Shell straight away!

Possible Answers
-np.array([True, 1, 2, 3, 4, False])
-np.array([4, 3, 0]) + np.array([0, 2, 2])
-np.array([1, 1, 2]) + np.array([3, 4, -1])
-np.array([0, 1, 2, 3, 4, 5])
'''
 np.array([4, 3, 0]) + np.array([0, 2, 2])
 