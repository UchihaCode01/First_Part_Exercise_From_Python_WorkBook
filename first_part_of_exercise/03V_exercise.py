
num = int(input("Enter the number which you need to multiplie : "))

total = ""

for i in range(1, 10+1):
    total += f'{num} * {i} = {i*num} \n'

print(total)
