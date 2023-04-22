
amount_of_bread = int(input("How much loafs of bread did you buy yesterday? "))

cost_per_loaf = 3.49
cost_per_yesterday_loaf = cost_per_loaf * 0.60

total_cost = amount_of_bread * cost_per_yesterday_loaf

print(f"The cost per loaf of bread is : {cost_per_loaf:.2f}")
print(f"The cost of yesterday's loaf of bread is : {cost_per_yesterday_loaf:.2f}")
print(f"The total cost of yesterday's bread is : {total_cost:.2f}")
