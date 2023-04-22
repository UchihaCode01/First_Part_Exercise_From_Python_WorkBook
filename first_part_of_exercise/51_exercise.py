number = 0
count = 0

while True:
    user_number = input("Enter your number : ")

    if user_number == "end":
        break
    elif int(user_number) == 0 and number == 0:
        print("The first number should be more than 0 : ")
    elif int(user_number) > 0 or int(user_number) < 0:
        number += int(user_number)
        count += 1


arithmetic_mean = number / count

print("The arithmetic mean of the numbers you entered is : ", arithmetic_mean)
