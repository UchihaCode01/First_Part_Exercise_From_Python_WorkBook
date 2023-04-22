
number = int(input("Enter your number : "))

hundreds = number // 100
number = number % 100

decimals = number // 10
number = number % 10

number = number

total = hundreds + decimals + number
print(total)
