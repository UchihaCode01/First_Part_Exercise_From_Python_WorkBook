
order_amount = float(input(" Введите сумму заказа : "))
tax_calculation = order_amount * 0.20
tip_calculation = tax_calculation * 0.18
sum_of_order = order_amount + tax_calculation + tip_calculation
print(f"\n Сумма заказа составляет : {order_amount :.2f}")
print(f"\n Налог составляет : {tax_calculation :.2f}")
print(f"\n Чаевые составляют : {tip_calculation :.2f}")
print(f"\n Сумма к оплате составляет : {sum_of_order :.2f}")