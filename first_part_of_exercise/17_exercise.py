
m = float(input("Enter mass of water : "))
dT = float(input("Enter the desired temperature of change : "))

C = 4.186
q = m * C * dT

print("The amount of enegry needed to heat the water is : ", q, "joules")

kWh = q / 3600000
cost = kWh * 0.089

print("Cost of accompanying water heating is : ", cost, "dollars")
