
distance = int(input("Write your distance in feet : "))

distance_in_inches = distance * 12
distance_in_yards = distance / 3
distance_in_miles = distance / 5280

print(f"Your distance in inch is {distance_in_inches :.4f}")
print(f"Your distance in yard is {distance_in_yards :.4f}")
print(f"Your distance in miles is {distance_in_miles :.4f}")
