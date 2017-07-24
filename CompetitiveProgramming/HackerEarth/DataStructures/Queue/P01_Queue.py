# You have to perform N operations on a queue of the following types: E x : Enqueue x in the queue and
# print the new size of the queue. D : Dequeue from the queue and print the element that is deleted and
# the new size of the queue separated by a space. If there is no element in the queue, then print −1 in
# place of the deleted element.
#
# Input format
# First line: N
# Next N lines: One of the above operations
#
# Output format
# Enqueue operation: Print the new size of the queue
# Dequeue operation: Print two integers, the deleted element and the new size of the queue. If the queue is
# empty, print −1 and the new size of the queue.
#
# Constraints
# 1≤N≤100
# 1≤x≤100
#
# SAMPLE INPUT
# 5
# E 2
# D
# D
# E 3
# D
#
# SAMPLE OUTPUT
# 1
# 2 0
# -1 0
# 1
# 3 0

def enqueue(myList, element):
  myList.insert(0, element)

def dequeue(myList):
  if len(myList) > 0:
    return myList.pop()
  else:
    return -1

myList = []

for _ in range(int(input())):
    userInput = input().split()
    if userInput[0] == 'E':
      enqueue(myList, int(userInput[1]))
      print(len(myList))
    else:
      deleted = dequeue(myList)
      print(deleted, len(myList))
