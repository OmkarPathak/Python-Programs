# Author: OMKAR PATHAK

# This program illustrates how to create an adarray from numerical ranges

import numpy as np

# ndarray.arange(start, stop, step, dtype)
# Creates a numpy array from 1 to 20
myArray = np.arange(1, 21)
print(myArray)                      # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

# Specifying data type of each element
myArray = np.arange(10, dtype = 'float')
print(myArray)                      # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

# Specifying steps to jump in between two elements
myArray = np.arange(1, 21, 2)
print(myArray)                      # [ 1  3  5  7  9 11 13 15 17 19]

# ndarray.linspace(start, stop, num, endpoint,  retstep, dtype)
# Shows 5 equal intervals between 10 to 20
myArray = np.linspace(10, 20, 5)
print(myArray)                      # [ 10.   12.5  15.   17.5  20. ]

# if endpoint is set to false the last number inn STOP parameter is not executed
myArray = np.linspace(10, 20, 5, endpoint = False)
print(myArray)                      # [ 10.  12.  14.  16.  18.]

# ndarray.lopspace returns an ndarray object that contains the numbers that are evenly spaced
# on a log scale.
# ndarray.logscale(start, stop, num, endpoint, base, dtype)
# default base is 10
myArray = np.logspace(1.0, 3.0, num = 10)
print(myArray)

# [   10.            16.68100537    27.82559402    46.41588834    77.42636827
#    129.1549665    215.443469     359.38136638   599.48425032  1000.        ]

myArray = np.logspace(1.0, 3.0, num = 10, base = 2)
print(myArray)

# [ 2.          2.33305808  2.72158     3.1748021   3.70349885  4.32023896
#   5.0396842   5.87893797  6.85795186  8.        ]
