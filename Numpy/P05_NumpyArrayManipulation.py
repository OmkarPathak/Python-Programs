# Author: OMKAR PATHAK

# This example shows various array manipulation operations
import numpy as np

# numpy.reshape(array_to_reshape, tuple_of_new_shape) gives new shape (dimension) to our array
myArray = np.arange(0, 30, 2)
print(myArray)              # [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]

myArrayReshaped = myArray.reshape(5, 3)
print(myArrayReshaped)

# [[ 0  2  4]
#  [ 6  8 10]
#  [12 14 16]
#  [18 20 22]
#  [24 26 28]]

# numpy.ndarray.flat() returns an 1-D iterator
print(myArray.flat[5])      # 10

# numpy.ndarray.flatten() restores the reshaped array into a 1-D array
print(myArrayReshaped.flatten())

# numpy.tranpose() this helps to find the tranpose of the given array
print(myArrayReshaped.transpose())

# [[ 0  6 12 18 24]
#  [ 2  8 14 20 26]
#  [ 4 10 16 22 28]]

# numpy.swapaxes(array, axis1, axis2) interchanges the two axes of an array
originalArray = np.arange(8).reshape(2,2,2)
print(originalArray)

# [[[0 1]
#   [2 3]]
#  
#  [[4 5]
#   [6 7]]]

print(np.swapaxes(originalArray, 2, 0))

# [[[0 4]
#   [2 6]]
#  
#  [[1 5]
#   [3 7]]]

# numpy.rollaxis(arr, axis, start) rolls the specified axis backwards, until it lies in a specified position
print(np.rollaxis(originalArray, 2))

# [[[0 2]
#   [4 6]]
#  
#  [[1 3]
#   [5 7]]]

# numpy.resize(arr, shape) returns a new array with the specified size. If the new size is greater than
# the original, the repeated copies of entries in the original are contained

myArray = np.array([[1,2,3],[4,5,6]])
print(myArray)

# [[1 2 3]
#  [4 5 6]]

print(np.resize(myArray, (3, 2)))

# [[1 2]
#  [3 4]
#  [5 6]]

# numpy.append(array, values, axis)
myArray = np.array([[1,2,3],[4,5,6]])
print(myArray)

# [[1 2 3]
#  [4 5 6]]

print(np.append(myArray, [7, 8, 9]))

# [1 2 3 4 5 6 7 8 9]
