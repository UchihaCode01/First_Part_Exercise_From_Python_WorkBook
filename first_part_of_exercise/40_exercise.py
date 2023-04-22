
decibels = float(
    input("Enter the number of decibels here in this format '00.00' : "))

if decibels < 40.00:
    print("You can sleep peacfully.")
elif decibels == 40.00:
    print("This volume level is like a quiet room.")
elif decibels > 40.00 and decibels < 70.00:
    print("This volume level is in the range of a quiet room and alarm clock.")
elif decibels == 70.00:
    print("This volume level is like an alarm clock.")
elif decibels > 70.00 and decibels < 106.00:
    print("This volume level is in the range of an alarm clock and a gas lawnmower.")
elif decibels == 106.00:
    print("This volume level is like a gas lawnmower.")
elif decibels > 106.00 and decibels < 130.00:
    print("This volume level is in the range of a gas lawnmower and a sledgehammer.")
elif decibels == 130.00:
    print("This volume level is like a sledgehammer.")
else:
    print("This volume level can severely damage your hearing.")
