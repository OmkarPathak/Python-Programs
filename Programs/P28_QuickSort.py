#Author: OMKAR PATHAK
#This program illustrates an example of quick sort

#  Quicksort works by selecting an element called a pivot and splitting
#  the array around that pivot such that all the elements in, say, the
#  left sub-array are less than pivot and all the elements in the right
#  sub-array are greater than pivot. The splitting continues until the
#  array can no longer be broken into pieces. That's it. Quicksort is
#  done.

#  Best = Average = O(nlog(n)); Worst = O(n^2

def quickSort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quickSort(myList, start, pivot-1)
        quickSort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
            print('Now left is:',left)
        while myList[right] >= pivot and right >=left:
            right = right -1
            print('now righht is:',right)
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:',quickSort(List, 0, len(List) - 1))
