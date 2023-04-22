import math

s = float(input("Enter the length of side : "))
n = float(input("Enter the number of sides : "))

area = (n * s**2) / (4 * math.tan(math.pi/n))

print(f"The area of polygon : {area :.2f}")
