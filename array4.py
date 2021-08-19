arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
tmp = arr[0]
arr[0] = arr[n - 1]
arr[n - 1] = tmp
print(arr)

