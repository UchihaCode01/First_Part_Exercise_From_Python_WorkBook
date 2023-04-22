
Ta = float(input("Enter the temperature : "))
V = float(input("Enter the wind speed : "))

WGI = 13.12 + 0.6215 * Ta - 11.37 * V**0.16 + 0.3965 * Ta * V**0.16

print("Air cooling coeficient is ", round(WGI))

