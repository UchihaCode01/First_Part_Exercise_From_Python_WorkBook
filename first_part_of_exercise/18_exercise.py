import math

r = float(input("Enter radius of your circle : "))
area = math.pi * (r ** 2)

height = float(input("Enter height of your cylinder : "))

volume = area * height

print(f"Volume of your cylinder is : {volume :.1f}")
