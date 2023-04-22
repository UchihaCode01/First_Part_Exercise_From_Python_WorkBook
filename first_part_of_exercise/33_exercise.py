import math

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

total = first_number + second_number + third_number

minimal = min(first_number, second_number, third_number)
maximum = max(first_number, second_number, third_number)
middle = total - maximum - minimal

print("Your minimal number is : ", minimal)
print("Ypur middle number is : ", middle)
print("Your maximum nuber is : ", maximum)
