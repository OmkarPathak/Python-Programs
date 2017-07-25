# Author: OMKAR PATHAK

import numpy as np

angles = np.array([0, 30, 45, 60, 90, 180, 360])

# Convert to radians by multiplying with pi/180
# for getting sine of angles
print(np.sin(angles * np.pi/180))

# for getting cosine of angles
print(np.cos(angles * np.pi/180))

# for getting tangent of angles
print(np.tan(angles * np.pi/180))

# for computing inverse of trigonometric functions
sine = np.sin(angles * np.pi/180)
sineinv = np.arcsin(sine)
# computing angle from inverse
print(np.degrees(sineinv))

# for rounding the values
print(np.around(sine, 4))       # [ 0.      0.5     0.7071  0.866   1.      0.     -0.    ]

# for rounding to previous integer
print(np.floor(sine))           # [ 0.  0.  0.  0.  1.  0. -1.]

# for rounding to next integer
print(np.ceil(sine))            # [ 0.  1.  1.  1.  1.  1. -0.]
