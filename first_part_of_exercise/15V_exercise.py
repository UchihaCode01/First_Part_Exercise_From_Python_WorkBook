
number = int(input("Enter your number of minutes : "))

days = (number // 60) % 24
hours = (number // 60) % 24
minutes = number % 60

print(
    f"Amount of days is {days}, and hours is {hours}, and minutes is {minutes}.")
