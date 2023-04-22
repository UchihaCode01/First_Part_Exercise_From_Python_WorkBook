import math

r = float(input("Write your radius : "))

area = math.pi * (r**2)
volume = (4/3) * (math.pi * (r**3))

print("Radius circle area", r, "is", area)
print("Sphere volume with radius", r, "is", volume)
