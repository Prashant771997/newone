li = [1, 2, 3, 4]
li1 = []
li1.append(li[-1])
n = len(li)
i = 0
while i < (n - 1):
    li1.append(li[i])
    i += 1
print(li1)



