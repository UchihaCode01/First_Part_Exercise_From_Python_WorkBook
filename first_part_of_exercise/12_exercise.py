import math

t1 = math.radians(float(input(" Write your first longitude : ")))
g1 = math.radians(float(input(" Write your first latitude : ")))
print(f"\n Your first coordinates is {t1 :.2f},", f"{g1 :.2f}")

t2 = math.radians(float(input(" Write your second longitude : "))) 
g2 = math.radians(float(input(" Write your second latitude : ")))
print(f"\n Your second coordinates is {t2 :.2f},", f"{g2 :.2f}")


distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print(f"\n Your distance is : ", distance, "kilometrs")
