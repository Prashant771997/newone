##prime numbers in an interval
x = int(input("enter the lower limit:"))
y =  int(input("enter the upper limit:"))
li = []
for i in range(x, y + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        li.append(i)
print("the primt numbers are:", li)
