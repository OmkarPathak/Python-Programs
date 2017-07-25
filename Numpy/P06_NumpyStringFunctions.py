# Author: OMKAR PATHAK

import numpy as np

abc = ['abc']
xyz = ['xyz']

# string concatenation
print(np.char.add(abc, xyz))    # ['abcxyz']

print(np.char.add(abc, 'pqr'))  # ['abcpqr']

# string multiplication
print(np.char.multiply(abc, 3)) # ['abcabcabc']

# numpy.char.center: This function returns an array of the required width so that the input string is
# centered and padded on the left and right with fillchar.

print(np.char.center(abc, 20, fillchar = '*'))  # ['********abc*********']

# numpy.char.capitalize(): This function returns the copy of the string with the first letter capitalized.
print(np.char.capitalize('hello world'))        # Hello world

# numpy.char.title(): This function returns a title cased version of the input string with the first letter
# of each word capitalized.
print(np.char.title('hello how are you?'))      # Hello How Are You?

# numpy.char.lower(): This function returns an array with elements converted to lowercase. It calls
# str.lower for each element.
print(np.char.lower(['HELLO','WORLD']))         # ['hello' 'world']

# numpy.char.upper(): This function calls str.upper function on each element in an array to return
# the uppercase array elements.
print(np.char.upper('hello'))                   # HELLO

# numpy.char.split(): This function returns a list of words in the input string. By default, a whitespace
# is used as a separator
print(np.char.split('Omkar Pathak'))            # ['Omkar', 'Pathak']
print(np.char.split('2017-02-11', sep='-'))     # ['2017', '02', '11']

# numpy.char.join(): This method returns a string in which the individual characters are joined by
# separator character specified.
print(np.char.join(':','dmy'))                  # d:m:y
