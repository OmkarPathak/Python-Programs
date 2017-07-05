# Author: OMKAR PATHAK

# These are the various attributes provided by NumPy.

import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# ndarray.size returns the number of items in the array
print(myArray.size)             # 9

# ndarray.shape returns a tuple consisting of array dimensions
print(myArray.shape)            # (3, 3)

# ndarray.ndim returns the number of array dimensions
print(myArray.ndim)             # 2

# ndarray.itemsize returns the memory size of each element in the array
print(myArray.itemsize)         # 8
