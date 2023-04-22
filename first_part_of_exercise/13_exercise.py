
change = int(input("Write your change : "))

toonie = change // 200
change = change % 200

loonie = change // 100
change = change % 100

quarter = change // 25
change = change % 25

dime = change // 10
change = change % 10

nickel = change // 5
change = change % 5

change = change

print(f"Your change in toonie is : {toonie} ")
print(f"Your change in loonie is : {loonie} ")
print(f"Your change in quarter is : {quarter} ")
print(f"Your change in dime is : {dime} ")
print(f"Your change in nickel is : {nickel} ")
print(f"Your change in penny is : {change} ")

