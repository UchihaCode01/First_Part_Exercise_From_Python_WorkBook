
number = input("Enter the number : ")
base = int(input("Specify the number system : "))

decimal = int(number, base)

print(f"The number in the decimal number system {decimal}")
print(f"The number in the binary number system {bin(decimal)}")
print(f"The number in the octal number system {oct(decimal)}")
print(f"The number in the hexadecimal number system {hex(decimal)}")
