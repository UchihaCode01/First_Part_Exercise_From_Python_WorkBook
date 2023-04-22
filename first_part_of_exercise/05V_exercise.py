
number = 0

while True:
    user_input = input("Enter the number : ")

    if user_input == "end":
        break
    else:
        number += int(user_input)

print(number)
