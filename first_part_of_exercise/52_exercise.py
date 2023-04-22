
for i in [4.95, 9.95, 14.95, 19.95, 24.95]:
    discount = i * 0.6
    msg = f"Initial price is {i:.2f}. Discount is 60% for this product and it's {discount:.2f}. New price is {i-discount:.2f}"
    print(msg)
