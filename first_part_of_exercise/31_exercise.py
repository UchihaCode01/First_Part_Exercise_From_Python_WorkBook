
kPa = float(input("Enter the pressure value : "))

PSI = kPa / 6.89475729
TORR = (kPa * 760) / 101.325
ATM = kPa / 101.325


print(f"The pressure value in PSI is : {PSI:.4f}")
print(f"The pressure value in TORR is : {TORR:.4f}")
print(f"The pressure value in ATM is : {ATM:.4f}")

