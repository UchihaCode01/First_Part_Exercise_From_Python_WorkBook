
rub = int(input("Enter your amount in rubley : "))
kop = int(input("Enter your amount in kopeyki : "))
amount = int(input("Enter your amont of cookies : "))

price = (rub * 100) + kop
total = price * amount

price_in_rub = total // 100
price_in_kop = total % 100

print(f"You must pay : {price_in_rub} rubley {price_in_kop} kopeyok. ")
