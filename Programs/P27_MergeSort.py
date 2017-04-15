#Author: OMKAR PATHAK
#This program gives an example of Merge sort

#   Merge sort is a divide and conquer algorithm. In the divide and
#   conquer paradigm, a problem is broken into pieces where each piece
#   still retains all the properties of the larger problem -- except
#   its size. To solve the original problem, each piece is solved
#   individually; then the pieces are merged back together.

#  Best = Average = Worst = O(nlog(n))

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a,b)

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:',mergeSort(List))
