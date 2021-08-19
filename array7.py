str1 = str(input("enter any string: "))
str2 = ''
n = len(str1)
for i in str1[ : : -1]:
    str2 += i

if str1 == str2:
    print("yes!")
    print(str2)
else:
    print("no!")
