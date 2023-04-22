import math

s1 = float(input("The A-side of triangle is : "))
s2 = float(input("The B-side of triangle is : "))
s3 = float(input("The C-side of triangle is : "))

s = (s1+s2+s3)/2
area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print("The area of triangle is : ", area)
