class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if head is None:
        return head
    if M == 0:
        return None
    temp = head
    prev = None
    cnt = 0
    while temp is not None:
        if(cnt == M):
            break
        cnt += 1
        prev = temp
        temp = temp.next
    cnt = 0
    while temp is not None:
        if(cnt == N):
            break
        cnt += 1
        temp = temp.next
        
    prev.next = skipMdeleteN(temp, M, N)
    return head
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


arr=list(int(i) for i in input().strip().split(' '))

l = ll(arr[:-1])
m=int(input())
n=int(input())

l = skipMdeleteN(l, m, n)
printll(l) 
