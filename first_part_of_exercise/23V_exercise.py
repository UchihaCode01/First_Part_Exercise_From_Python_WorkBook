import math

first_num = int(input("Enter the first number : "))
second_num = int(input("Enter the second number : "))

sqrt = []

for i in range(first_num, second_num):
    sqrt.append(math.sqrt(i))

print(sqrt)
