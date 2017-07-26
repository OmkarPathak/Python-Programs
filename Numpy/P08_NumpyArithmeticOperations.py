# Author: OMKAR PATHAK

import numpy as np

firstArray = np.arange(12).reshape(3, 4)
print(firstArray)

secondArray = np.arange(4)
print(secondArray)

# adding above two arrays (NOTE: array shapes should be same)
print(np.add(firstArray, secondArray))

# subtracting above two arrays
print(np.subtract(firstArray, secondArray))

# multiplying above two arrays
print(np.multiply(firstArray, secondArray))

# dividing the above two arrays
print(np.divide(firstArray, secondArray))

# numpy.power(): returns array element raised to the specified value result
array = np.array([1, 2, 3])
print(np.power(array, 2))       # [1 4 9]
