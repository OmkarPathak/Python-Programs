def binarySearchCountLess(arr, n, key): 

	left = 0
	right = n 

	mid = 0
	while (left < right): 
	
		mid = (right + left)//2
		if (arr[mid] == key): 
		
			while (mid + 1<n and arr[mid + 1] == key): 
				mid+= 1
			break
		
		elif (arr[mid] > key): 
			right = mid 
		else: 
			left = mid + 1
	
	while (mid > -1 and arr[mid] > key): 
		mid-= 1

	return mid + 1

def main():
    t = int(input())
    for _ in range(t):
        n, x, p, k = [int(y) for y in input().split()]
        a = [int(y) for y in input().split()]
        a.sort()
        if n <= 5:
            count = 0
            if a[p-1] == x:
                print(0)
            else:
                for i in range(n+1):
                    a[k-1] = x
                    a.sort()
                    count += 1
                    if a[p-1] == x:
                        print(count)
                        break
                if a[p-1] != x:
                    print(-1)
        else:        
            if a[p - 1] == x:
                res = 0
            else:
                if p < k:
                    if a[p-1] < x:
                        res = -1
                    else:
                        ind = binarySearchCountLess(a, n, x)
                        res = p - ind
                elif p > k:
                    if a[p - 1] > x:
                        res = -1
                    else:
                        ind = binarySearchCountLess(a, n, x)
                        if a[ind - 1] != x:
                            ind += 1
                        else:
                            while True:
                                if a[ind - 2] == x:
                                    ind -= 1
                                else:
                                    break
                        res = ind - p
                else:
                    if x < a[p-1]:
                        ind = binarySearchCountLess(a, n, x)
                        res = p - ind
                    else:
                        ind = binarySearchCountLess(a, n, x)
                        if a[ind - 1] != x:
                            ind += 1
                        res = ind - p
            print(res)
    return 0

main()
