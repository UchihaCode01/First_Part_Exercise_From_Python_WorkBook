
denomination = int(input("Enter the denomination of banknote : "))

if denomination == 1:
    print(f"You can see George Washington on the ${denomination} banknote.")
elif denomination == 2:
    print(f"You can see Thomas Jefferson on the ${denomination} banknote.")
elif denomination == 5:
    print(f"You can see Abraham Lincoln on the ${denomination} banknote.")
elif denomination == 10:
    print(f"You can see Alexander Hamilton on the ${denomination} banknote.")
elif denomination == 20:
    print(f"You can see Andrew Jackson on the ${denomination} banknote.")
elif denomination == 50:
    print(f"You can see Ulysses Grant on the ${denomination} banknote.")
elif denomination == 100:
    print(f"You can see Benjamin Franklin on the ${denomination} banknote.")
else:
    print("This banknote doesn't exist.")
