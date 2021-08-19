x = int(input("please enter a valid number:"))
first = 0
second = 1
for i in range(1, x - 1):
    third = first + second
    first = second
    second = third
print("the number is: ", third)
