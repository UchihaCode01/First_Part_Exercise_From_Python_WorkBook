
month = input("Enter the name of month : ")
number = int(input("Enter the number : "))

if month == "March" or month == "April" or month == "May" or month == "June":
    if month == "March" and (number > 0 and number <= 19):
        print("This is still winter.")
    elif month == "March" and (number >= 20 and number <= 31):
        print("This is spring.")
    elif month == "April" and (number > 0 and number <= 30):
        print("This is spring.")
    elif month == "May" and (number > 0 and number <= 31):
        print("This is spring.")
    elif month == "June" and (number > 0 and number < 21):
        print("This is still spring.")
elif month == "June" or month == "July" or month == "August" or month == "September":
    if month == "June" and (number >= 21 and number <= 30):
        print("This is summer.")
    elif month == "July" and (number > 0 and number <= 31):
        print("This is spring.")
    elif month == "August" and (number > 0 and number <= 31):
        print("This is spring.")
    elif month == "September" and (number > 0 and number < 22):
        print("This is still summer.")
elif month == "September" or month == "October" or month == "November" or month == "December":
    if month == "September" and (number >= 22 and number <= 30):
        print("This is autumn.")
    elif month == "October" and (number > 0 and number <= 31):
        print("This is autumn.")
    elif month == "November" and (number > 0 and number <= 30):
        print("This is autumn.")
    elif month == "December" and (number > 0 and number < 21):
        print("This is still autumn.")
elif month == "December" or month == "January" or month == "February":
    if month == "December" and (number >= 21 and number <= 31):
        print("This is winter.")
    elif month == "January" and (number > 0 and number <= 31):
        print("This is winter.")
    elif month == "February" and (number > 0 and number <= 29):
        print("This is winter.")
else:
    print("This is impossible!")
