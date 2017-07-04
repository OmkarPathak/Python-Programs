# Author: OMKAR PATHAK

# NumPy (Numeric Python) is a Python package used for building multi dimensional arrays and performing
# various operations

# In this program we will walk through various concepts and see available functions in the NumPy package.

# For installing: pip3 install numpy

import numpy as np

# we have a function arange() which makes an array of the specified dimension. Example:
myArray = np.arange(20)
print(myArray)              # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

# an array from 10 to 20
myArray = np.arange(10, 20) # [10 11 12 13 14 15 16 17 18 19]
print(myArray)

# an array from 10 to 20 with 2 steps
myArray = np.arange(10, 20, 2)
print(myArray)              # [10 12 14 16 18]

# reshape() helps to reshape our NumPy array
myArray = np.arange(20)
# syntax: reshape(number_of_rows, number_of_columns)
myArray = myArray.reshape(4, 5)
print(myArray)

# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

myArray = myArray.reshape(10, 2)
print(myArray)

# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]
#  [12 13]
#  [14 15]
#  [16 17]
#  [18 19]]

# shape returns the shape of the array. The length of shape tuple is called as rank (or dimension)
print(myArray.shape)        # (10, 2)

# ndim returns the dimension (rank) of the array
print(myArray.ndim)         # 2

# size returns the total number of elements in the array
print(myArray.size)         # 20

# to check the data we have dtype.
print(myArray.dtype)        # int64

# zeros creates an array will all zeros
myArray = np.zeros((3, 4))
print(myArray)

# [[ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]]

# ones creates an array with all ones
myArray = np.ones((3, 4))
print(myArray)

# [[ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]]

# numpy random module helps to initialize array with random values
myArray = np.random.rand(3, 4)
print(myArray)

# [[ 0.54808903  0.08750717  0.23886267  0.93589283]
#  [ 0.90750146  0.31197039  0.54013725  0.91092763]
#  [ 0.38827674  0.04647878  0.15997665  0.94909537]]
