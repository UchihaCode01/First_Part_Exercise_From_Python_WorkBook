
side_a = float(input("Enter the lenght of first side : "))
side_b = float(input("Enter the lenght of second side : "))
side_c = float(input("Enter the lenght of third side : "))

if side_a == side_b == side_c:
    print("This is an equilateral triangle.")
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("This is an isosceles triangle.")
elif side_a != side_b and side_b != side_c and side_c != side_a:
    print("This is a scalene triangle.")
