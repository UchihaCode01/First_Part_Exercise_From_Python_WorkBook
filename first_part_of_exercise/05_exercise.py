
number_of_litres_bottles = int(input("Введите сколько у вас бутылок объемом 1 литр или меньше?"))
print(number_of_litres_bottles)
number_of_other_bottles = int(input("Введите сколько у вас бутылок объемом больше 1 литра?"))
print(number_of_other_bottles)

x = 0.10 * number_of_litres_bottles
y = 0.25 * number_of_other_bottles
sum = x + y
print(f"${sum :.2f}")