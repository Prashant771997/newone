def find(li):
    x = 3
    k = 3
    n = len(li)
    a = n // k
    i = 0
    l = 0
    count = 0
    while i < a:
        j = l
        while j < n:
            if li[j] == x:
                print("present")
                count += 1
                break
            else:
                j += 1
        l += k
        i += 1
    if count == a:
        print("present in all lists:")
    else:
        print("not present in all")



li = [1, 2, 3, 5, 3, 1, 6, 7, 3, 11, 14, 3]
find(li)