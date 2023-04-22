
num_a = int(input("Enter the first number : "))
num_b = int(input("Enter the second number : "))

for diff in range(num_a, num_b):
    if diff % 5 == 0:
        print(diff)
    elif diff < 5:
        print("There is no number between these numbers that is divisible by 5.")
