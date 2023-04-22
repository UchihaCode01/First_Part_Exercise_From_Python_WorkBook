
magnitude = float(input("Enter the magnitude on the Richter scale: "))

if magnitude < 2.0:
    print("Minimal earthquake")
elif magnitude >= 2.0 and magnitude < 3.0:
    print("Very weak earthquake")
elif magnitude >= 3.0 and magnitude < 4.0:
    print("Weak earthquake")
elif magnitude >= 4.0 and magnitude < 5.0:
    print("Intermediate earthquake")
elif magnitude >= 5.0 and magnitude < 6.0:
    print("Moderate earthquake")
elif magnitude >= 6.0 and magnitude < 7.0:
    print("Strong earthquake")
elif magnitude >= 7.0 and magnitude < 8.0:
    print("Very strong earthquake")
elif magnitude >= 8.0 and magnitude < 10.0:
    print("Huge earthquake")
else:
    print("Destructive earthquake")
