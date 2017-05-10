#  Author: OMKAR PATHAK

#  Approach:
#  Counting sort, like radix sort and bucket sort,
#  is an integer based algorithm (i.e. the values of the input
#  array are assumed to be integers). Hence counting sort is
#  among the fastest sorting algorithms around, in theory. The
#  particular distinction for counting sort is that it creates
#  a bucket for each value and keep a counter in each bucket.
#  Then each time a value is encountered in the input collection,
#  the appropriate counter is incremented. Because counting sort
#  creates a bucket for each value, an imposing restriction is
#  that the maximum value in the input array be known beforehand.

#  Implementation notes:
#  1] Since the values range from 0 to k, create k+1 buckets.
#  2] To fill the buckets, iterate through the input list and
#  each time a value appears, increment the counter in its
#  bucket.
#  3] Now fill the input list with the compressed data in the
#  buckets. Each bucket's key represents a value in the
#  array. So for each bucket, from smallest key to largest,
#  add the index of the bucket to the input array and
#  decrease the counter in said bucket by one; until the
#  counter is zero.

#  Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
#  where n is the size of the input array and k means the
#  values range from 0 to k.

def countingSort(myList):
    maxValue = 0
    for i in range(len(myList)):
        if myList[i] > maxValue:
            maxValue = myList[i]

    buckets = [0] * (maxValue + 1)

    for i in myList:
        buckets[i] += 1

    i = 0
    for j in range(maxValue + 1):
         for a in range(buckets[j]):
             myList[i] = j
             i += 1

    return myList

if __name__ == '__main__':
    sortedList = countingSort([1,23,4,5,6,7,8])
    print(sortedList)
