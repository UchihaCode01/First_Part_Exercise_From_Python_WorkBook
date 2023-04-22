
number_list = []

while True:
    number = input(
        "Enter your number to add it to list, enter 'end' to stop this programm : ")
    if number == "end":
        break
    else:
        number_list.append(number)


odd = []
even = []

for i in number_list:
    if int(i) % 2 == 0:
        odd.append(i)

    elif int(i) % 2 == 1:
        even.append(i)

print(len(odd))
print(len(even))
