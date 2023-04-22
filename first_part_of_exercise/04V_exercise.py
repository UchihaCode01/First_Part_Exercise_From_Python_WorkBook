
totalgrade = 0

for total in range(4):
    grade = float(input("Enter your grade from exam : "))

    totalgrade += grade

print(f"Total grade is : {totalgrade:.2f}", end="\n")
