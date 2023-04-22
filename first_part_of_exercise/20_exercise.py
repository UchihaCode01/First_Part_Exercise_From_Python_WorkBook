
P = int(input("Enter the pressure in pascals : "))
V = int(input("Enter the volume in litres : "))
T = int(input("Enter the temperature in Celsius : "))

T = T + 273.15 
R = 8.314

n = (P * V) / (R * T)

print(f"The amount of gas in moles is equal to : {n :.2f}")
