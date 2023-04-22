
first_class = int(input("Enter amount of childrens in first class : "))
second_class = int(input("Enter amount of childrens in second class : "))
third_class = int(input("Enter amount of childrens in third class : "))

total_childrens = first_class + second_class + third_class

pairs = total_childrens // 2
single = total_childrens % 2

total_student_desks = pairs + single

print(f"We must to buy {total_student_desks} student desks.")
