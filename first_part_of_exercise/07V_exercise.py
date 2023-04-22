
number = int(input("Enter the number: "))
figure = int(input("Enter the figure : "))

sum = 0

while number > 0:
    if number % 10 == figure:
        sum += 1
    number //= 10
print(f"You can see the figure {figure} in number {sum} times")
