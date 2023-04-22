
month = str(input("Enter the month name with the capital letter : "))

if month == "February":
    print("February can have either 28 days or 29 days. It all depends on whether the year is a leap year or not.")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("This month has 30 days.")
elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("This month has 31 days.")
else:
    print("This function is not available.")
