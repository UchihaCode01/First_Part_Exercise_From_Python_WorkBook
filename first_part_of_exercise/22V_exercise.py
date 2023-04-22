import textwrap

num = int(input("Enter the first operand : "))
mult = int(input("Enter the second operand : "))

for number in range(1, num):
    print(f"{number : 3}".ljust(3), end="")
print("\n", "-" * 30)

for number_of_multiplie in range(1, mult):
    print(f"{number_of_multiplie : 1}|", end="")
    for result_of_multiplie in range(1, mult):
        print(f"{number_of_multiplie * result_of_multiplie : 3}", end="")
    print()
