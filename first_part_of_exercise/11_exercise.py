
mpg_name = float(input("Write your fuel consumption in MPG : "))
km_name = (100 * 3.7854118) / (mpg_name * 1.609344)

print(f"{mpg_name :.2f}", "miles per gallon ", "=", f"{km_name :.2f}", "litres per 100 kilometres" )
