
souvenir = int(input("How much souvenirs do you have?"))
trinket = int(input("How much trinkets do you have?"))

weight_of_souvenir = 75 * souvenir
weight_of_trinket = 112 * trinket
sum_of_weight = weight_of_souvenir + weight_of_trinket

print("Your parcel weighs : ", sum_of_weight, "grams")