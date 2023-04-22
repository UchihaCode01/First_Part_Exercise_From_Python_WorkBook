
number = int(input("Enter an integer number : "))
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10

print("Sum of your number is : ", sum)
