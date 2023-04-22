
number = 0

for number in range(1, 50):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", number)
    elif number % 3 == 0:
        print("Fizz", number)
    elif number % 5 == 0:
        print("Buzz", number)
