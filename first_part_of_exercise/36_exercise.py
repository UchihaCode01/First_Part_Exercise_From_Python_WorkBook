
human_age = float(input("Enter your age : "))

BABY_MULTIPLIER = 10.5
ADULT_MULTIPLIER = 4

dog_years = 0

if human_age < 0:
    print("You haven't been born yet.")
elif human_age <= 2:
    dog_years = BABY_MULTIPLIER * human_age
elif human_age > 2:
    baby_years = BABY_MULTIPLIER * 2
    human_age -= 2
    print(human_age)

    dog_years = baby_years + (human_age * ADULT_MULTIPLIER)


print(f"Dog age is {dog_years}")
