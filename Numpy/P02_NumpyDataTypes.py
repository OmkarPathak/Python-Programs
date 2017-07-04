# Author: OMKAR PATHAK

# Data type	  Description
# bool_	      Boolean (True or False) stored as a byte
# int_	      Default integer type (same as C long; normally either int64 or int32)
# intc	      Identical to C int (normally int32 or int64)
# intp	      Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8	      Byte (-128 to 127)
# int16	      Integer (-32768 to 32767)
# int32	      Integer (-2147483648 to 2147483647)
# int64	      Integer (-9223372036854775808 to 9223372036854775807)
# uint8	      Unsigned integer (0 to 255)
# uint16	  Unsigned integer (0 to 65535)
# uint32	  Unsigned integer (0 to 4294967295)
# uint64	  Unsigned integer (0 to 18446744073709551615)
# float_	  Shorthand for float64.
# float16	  Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32	  Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64	  Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_	  Shorthand for complex128.
# complex64	  Complex number, represented by two 32-bit floats (real and imaginary components)
# complex128  Complex number, represented by two 64-bit floats (real and imaginary components)

import numpy as np

# while creating a numpy array, any data type from above can be explicitly specified.
myArray = np.arange(10)
print(myArray)          # [0 1 2 3 4 5 6 7 8 9]

myArray = np.array(myArray, dtype = np.float32)
print(myArray)          # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

myArray = np.array(myArray, dtype = np.complex64)
print(myArray)          # [ 0.+0.j  1.+0.j  2.+0.j  3.+0.j  4.+0.j  5.+0.j  6.+0.j  7.+0.j  8.+0.j  9.+0.j]
