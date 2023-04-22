
steps = int(input("Enter the number : "))

for i in range(1, steps+1):
    spaces = " " * (steps-i)
    hashes = "#" * i
    print(f"{spaces}{hashes}")
