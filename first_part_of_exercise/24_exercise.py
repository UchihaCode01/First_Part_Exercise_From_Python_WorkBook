
days = int(input("Enter amount of days : "))
hours = int(input("Enter amount of hours : "))
minutes = int(input("Enter amount of minutes : "))
seconds = int(input("Enter amount of seconds : "))

hours_in_days = days * 24
minutes_in_hours = (hours + hours_in_days) * 60
seconds_in_minutes = (minutes_in_hours + minutes) * 60
total_seconds = seconds + seconds_in_minutes


print("Total amount in second is : ", total_seconds)
