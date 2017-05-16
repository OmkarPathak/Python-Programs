# Author: OMKAR PATHAK

# PASCAL TRAINGLE: To build the triangle, start with "1" at the top, then continue placing numbers
# below it in a triangular pattern. Each number is the numbers directly above it added together.

# generates the nth row of Pascal's Triangle
def pascalRow(n):
    if n == 0:
        return [1]
    else:
        N = pascalRow(n-1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]

# create a triangle of n rows
def pascalTriangle(n):
    triangle = []
    for i in range(n):
        triangle.append(pascalRow(i))
    return triangle

if __name__ == '__main__':
    for i in pascalTriangle(7):
        print(i)

    # OUTPUT:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
