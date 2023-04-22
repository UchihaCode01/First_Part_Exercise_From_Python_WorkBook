
number = int(input("Enter the number of the month : "))
month = input("Enter the name of the month : ")

if number == 1 and month == "January":
    print("This is New Year's Day.")
elif number == 1 and month == "July":
    print("This is the Day of Canada.")
elif number == 25 and month == "December":
    print("This is Cristmas.")
else:
    print("There are no holidays in this date.")
