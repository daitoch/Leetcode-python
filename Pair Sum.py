arr = [2,-6,2,5, 2 ]
s = 5
arr.sort()
res = []
for i in range(len(arr)):
	for j in range(i, len(arr)):
		if (arr[i] + arr[j]) == s:
			res.append([arr[i], arr[j]])
print(res)