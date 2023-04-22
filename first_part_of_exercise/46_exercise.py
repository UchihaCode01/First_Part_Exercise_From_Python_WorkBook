
letter = str(input("Enter the cell letter : "))
number = int(input("Enter the cell number : "))

if letter == "A" or letter == "C" or letter == "E" or letter == "G":
    if number % 2 != 0:
        print(f"The cell {letter}{number} is black.")
    elif number % 2 == 0:
        print(f"The cell {letter}{number} is white.")
elif letter == "B" or letter == "D" or letter == "F" or letter == "H":
    if number % 2 != 0:
        print(f"The cell {letter}{number} is white.")
    elif number % 2 == 0:
        print(f"The cell {letter}{number} is black.")
else:
    print("This is unknown cell.")
