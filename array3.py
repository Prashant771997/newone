def rotate(arr, d):
    tmp = []
    n = len(arr)
    i = 0
    arr1 = []
    while i < d:
        tmp.append(arr[i])
        i += 1
    while d < n:
        arr1.append(arr[d])
        d += 1
    for j in tmp:
        arr1.append(j)
    return arr1


arr = [1, 2, 3, 4, 5, 6, 7]
ans = rotate(arr, 2)
print(ans)