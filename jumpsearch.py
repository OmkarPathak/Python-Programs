import math
def jump_search(arr,search):
    low = 0
    interval = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),interval):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            return i
        else:
            break # bigger number is found
    c=low
    for j in arr[low:]:
        if j==search:
            return c
        c+=1
    return "Not found"

arr = [ i for i in range(1,200,15)]
res = jump_search(arr, 196)
print(res)
