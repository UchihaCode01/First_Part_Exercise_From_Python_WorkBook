

number = int(input("Enter your number : "))

four_digit = number // 1000
triple_digit = (number % 1000) // 100
double_digit = (number % 100) // 10
single_digit = number % 10

sum = four_digit + triple_digit + double_digit + single_digit

print("The sum of your number is : ", sum)

