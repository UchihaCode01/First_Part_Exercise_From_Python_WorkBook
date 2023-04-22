
deposit = float(input("Enter the amount of your initial deposit : "))
interest_rate = 0.04

deposit = deposit + (deposit*interest_rate)
print(f"Amount on your account after first year is : {deposit :.2f}")
deposit = deposit + (deposit*interest_rate)
print(f"Amount on your account after second year is : {deposit :.2f}")
deposit = deposit + (deposit*interest_rate)
print(f"Amount on your account after third year is : {deposit :.2f}")
