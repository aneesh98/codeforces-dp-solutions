def maxsub(arr):
	maxlen = [0 for i in range(len(arr))]
	for i in range(len(arr) -1, -1, -1):
		if arr[i] <= arr[min(i+1, len(arr)-1)]:
			maxlen[i] = maxlen[min(i+1, len(arr) -1)] + 1
		else:
			maxlen[i] = 1
	return max(maxlen)

		

n = int(input())
arr = [int(num) for num in input().split()]
print(maxsub(arr))