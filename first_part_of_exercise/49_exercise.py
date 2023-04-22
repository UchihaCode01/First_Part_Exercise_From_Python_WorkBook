
year = int(input("Enter your year of birth : "))

animal = (year - 2000) % 12

if animal == 0:
    print("Your zodiac animal is Dragon.")
elif animal == 1:
    print("Your zodiac animal is Snake.")
elif animal == 2:
    print("Your zodiac animal is Horse.")
elif animal == 3:
    print("Your zodiac sign is Goat.")
elif animal == 4:
    print("Your zodiac sign is Monkey.")
elif animal == 5:
    print("Your zodiac sign is Rooster.")
elif animal == 6:
    print("Your zodiac sign is Dog.")
elif animal == 7:
    print("Your zodiac sign is Pig.")
elif animal == 8:
    print("Your zodiac sign is Rat.")
elif animal == 9:
    print("Your zodiac sign is Bull.")
elif animal == 10:
    print("Your zodiac sign is Tiger.")
else:
    print("Your zodiac sign is Rabbit.")
