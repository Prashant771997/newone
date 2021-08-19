def large(arr):
    lar = arr[0]
    for i in arr:
        if i > lar:
            lar = i
    return lar
arr = [50, 20, 100, 25, 60]
ans = large(arr)
print("the largest number is:", ans)
