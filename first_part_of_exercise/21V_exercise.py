
number = int(input("Enter the number : "))

star = "#"
space = " "

for i in range(number+1):

    if i >= 1 and i < number:

        for j in range(number - 2):
            print(star + space * (number - 2) + star)
            break

    else:
        print(star * number)
