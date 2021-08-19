n = int(input("please enter a valid number: "))
sum = 0
num = n
while n > 0:
    d = n % 10
    sum = sum + pow(d, 4)
    n = n//10
if sum == num:
    print("amstrong number")
else:
    print("other number")
    

