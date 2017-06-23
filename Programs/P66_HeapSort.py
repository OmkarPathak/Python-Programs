# Author: OMKAR PATHAK

#  Approach:
#  Heap sort happens in two phases. In the first phase, the array
#  is transformed into a heap. A heap is a binary tree where
#  1) each node is greater than each of its children
#  2) the tree is perfectly balanced
#  3) all leaves are in the leftmost position available.
#  In phase two the heap is continuously reduced to a sorted array:
#  1) while the heap is not empty
#  - remove the top of the head into an array
#  - fix the heap.

#  Time Complexity of Solution:
#  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).

def HeapSort(alist):
    heapify(alist)              # create the heap
    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        shiftDown(alist, 0, end - 1)
        end -= 1

def heapify(alist):
    ''' This function helps to maintain the heap property '''
    # start = (len(alist) - 2) // 2         (faster execution)
    start = len(alist) // 2
    while start >= 0:
        shiftDown(alist, start, len(alist) - 1)
        start -= 1

def shiftDown(alist, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and alist[root] < alist[child]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            return

if __name__ == '__main__':
    alist = [12, 2, 4, 5, 2, 3]
    HeapSort(alist)
    print('Sorted Array:',alist)
