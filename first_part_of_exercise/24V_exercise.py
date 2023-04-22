
number_list = []

while True:
    number = input(
        "Enter your number to add it to list, enter 'end' to stop this programm : ")
    if number == "end":
        break
    else:
        number_list.append(number)

for i in number_list:
    if int(i) % 2 == 0:
        print(i)
    else:
        pass
